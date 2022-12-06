from typing import Dict, List, Union

import pandas as pd
import sqlalchemy as sql
import sqlmodel as sqm


def parse_and_insert_df(df: pd.DataFrame, target_table: str) -> Dict[str, Dict]:
    added_entries = {"mappings": {}, "entries": {}}  # type: ignore
    try:
        mapper = map_cols_to_tables(df, target_table)
        added_entries = _add_columns(df, mapper)
        df = _populate_cols_with_pks(df, added_entries)
        df_entries = _add_dfs(df, target_table)
        added_entries["mappings"] = {
            **added_entries["mappings"],
            **df_entries["mappings"],
        }
        added_entries["entries"] = {**added_entries["entries"], **df_entries["entries"]}
    except Exception as e:
        _delete_added_entries(added_entries)
        raise e
    finally:
        import lamindb as ln

        ln.view()
    return added_entries


def add_from_column(
    pd_series: pd.Series, table: sqm.SQLModel, table_column: str
) -> Dict[str, Dict]:
    """Quick-insert entries into LaminDB from a DataFrame column.

    This only writes one single column of each entry into the database.
    """
    entries = pd_series.unique().tolist()
    table_name = str(table.__table__.name)
    added_entries = {"mappings": {}, "entries": {}}  # type: ignore
    added_entries["mappings"][pd_series.name] = (table_name, table_column)
    added_entries["entries"][table_name] = []
    for value in entries:
        try:
            db_entry = _add_or_fetch(table, table_column, value)
            added_entries["entries"][table_name] += [db_entry]
        except Exception as e:
            _delete_added_entries(added_entries)
            raise e
    return added_entries


def add_from_df(
    df: pd.DataFrame, table: sqm.SQLModel, column_map: dict = None
) -> Dict[str, Dict]:
    """Quick-insert all rows of a DataFrame as entries into LaminDB."""
    import lamindb as ln

    added_entries = {"mappings": {}, "entries": {}}  # type: ignore

    # Rename columns
    df_temp = df.copy()
    if column_map:
        df_temp = df_temp.rename(columns=column_map)
    df_temp = df_header_to_snake(df_temp)

    # Get the intersection between df and table columns
    df_temp = _rename_fk_of_target_pk(df_temp, table)
    common_fields = set(table.__fields__.keys()).intersection(df_temp.columns)
    common_df_as_records = df_temp[list(common_fields)].to_dict(orient="records")

    # Add df rows to db
    entries_to_add = [table(**row) for row in common_df_as_records]
    entries = ln.add(entries_to_add)
    added_entries["entries"][str(table.__table__.name)] = entries

    return added_entries


def str_to_snake(string: str) -> str:
    import re

    string = string.lower()
    string = re.sub("[ ]", "_", string)
    return string


def df_header_to_snake(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str_to_snake(x) for x in df.columns]
    return df


def get_sql_tables(table_name: str) -> List[sql.schema.Table]:
    """Get LaminDB sqlalchemy tables whose name perfectly match the input."""
    import lamindb as ln

    tables = ln.schema._core.get_db_metadata().sorted_tables
    matched = [tab for tab in tables if tab.name.split(".")[-1] == table_name]
    return matched


def get_sql_fk_tables(table_name: str) -> List[sql.schema.Table]:
    """Get all tables associated with the input table (by fk constraint)."""
    tables = get_sql_tables(table_name)
    fk_tables = []
    for table in tables:
        fk_tables += [fk.column.table for fk in table.foreign_keys]
    return fk_tables


def get_sqm_tables(name: str) -> sqm.main.SQLModelMetaclass:
    from functools import reduce
    from inspect import getmembers, isclass

    import lamindb as ln

    name_components = name.split(".")
    module = reduce(getattr, name_components[:-1], ln.schema)
    members = getmembers(module, isclass)
    for member in members:
        if name_components[-1] == member[0].lower():
            return member[1]


def get_pk_fk(table: sqm.SQLModel) -> Union[None, str]:
    """Gets the foreign key field of the input table's primary key."""
    pk = table.__table__.primary_key.columns.items()
    if len(pk) > 1:
        raise NotImplementedError(
            "Fetching of composite primary key's foreign key not yet implemented."
        )
    pk_fks = pk[0][1].foreign_keys
    if pk_fks:
        pk_fks = list(pk_fks)
        if len(pk_fks) > 1:
            raise NotImplementedError(
                "Composite primary key linking not yet implemented."
            )
        pk_fk = str(pk_fks[0].target_fullname)
        return pk_fk
    else:
        return None


def map_cols_to_tables(
    df: pd.DataFrame, target_table: str
) -> Dict[str, sql.schema.Table]:
    """Map df columns to LaminDB tables associated with columns from input table."""
    mapping = {}
    temp_df = df_header_to_snake(df)
    sample_fk_tables = get_sql_fk_tables(target_table)
    for column in temp_df.columns:
        for table in sample_fk_tables:
            if column in table.name:
                column = match_col_from_df(df, column)
                mapping[column] = table
    return mapping


def match_col_from_df(df: pd.DataFrame, target: str) -> str:
    """Matches dataframe column to target based on a perfect snake case string match."""
    snake_target = str_to_snake(target)
    snake_df = df_header_to_snake(df)
    try:
        match_index = snake_df.columns.get_loc(snake_target)
    except KeyError:
        raise KeyError(
            f"Could not match {target} to DataFrame columns {list(df.columns)}"
        )
    return df.columns[match_index]


def match_col_from_table(table: sql.schema.Table, substring: str) -> str:
    """Returns column name that contains the input substring."""
    table_cols = table.columns.keys()
    matched_columns = [str(s) for s in table_cols if substring in s]
    return matched_columns[0]


def _add_columns(df: pd.DataFrame, column_mapper: dict) -> Dict[str, Dict]:
    """Add mapped columns from DataFrame into LaminDB."""
    added_entries = {"mappings": {}, "entries": {}}  # type: ignore
    try:
        match_field = "name"
        for column, table in column_mapper.items():
            table_column = match_col_from_table(table, match_field)
            sqm_table = get_sqm_tables(table.name)
            entries = add_from_column(df[column], sqm_table, table_column)
            added_entries = _update_added_entries(added_entries, entries)
    except Exception as e:
        _delete_added_entries(added_entries)
        raise Exception("Failed at add_columns: ", e)
    return added_entries


def _add_dfs(df: pd.DataFrame, target_table: str) -> Dict[str, Dict]:
    """Add dataframe into LaminDB tables whose name match the input name."""
    df = df.copy()
    added_entries = {"mappings": {}, "entries": {}}  # type: ignore
    try:
        target_tables = get_sql_tables(target_table)
        for table in target_tables:
            sqm_table = get_sqm_tables(table.name)
            entries = add_from_df(df, sqm_table)
            added_entries = _update_added_entries(added_entries, entries)
            df[(table.name.lower() + ".id")] = [
                entry.id
                for table_entry in entries["entries"].values()
                for entry in table_entry
            ]
    except Exception as e:
        _delete_added_entries(added_entries)
        raise Exception("Failed at add_dfs: ", e)
    return added_entries


def _add_or_fetch(target_table: sqm.SQLModel, table_column: str, value):
    import lamindb as ln

    query_filter = {table_column: value}
    existing_entry = ln.select(target_table, **query_filter).one_or_none()
    if existing_entry is not None:
        return existing_entry
    else:
        return ln.add(target_table(**{table_column: value}))


def _delete_added_entries(added_entries: dict):
    import lamindb as ln

    for table_entries in added_entries["entries"].values():
        for entry in table_entries:
            ln.delete(entry)


def _populate_cols_with_pks(df, col_entries: dict) -> pd.DataFrame:
    """Populate and rename df columns based on column mappings and DB entries."""
    df = df.copy()
    for col, mapping in col_entries["mappings"].items():
        table, field = mapping
        entries = col_entries["entries"][table]
        id_mapper = {getattr(entry, field): entry.id for entry in entries}
        df[col] = df[col].map(id_mapper)
        df = df.rename(columns={col: f"{col} ID"})
    return df


def _rename_fk_of_target_pk(
    df: pd.DataFrame, target_table: sqm.SQLModel
) -> pd.DataFrame:
    df = df.copy()
    pk_fk = get_pk_fk(target_table)
    for col in df.columns:
        if col == pk_fk:
            df = df.rename(columns={col: "id"})
    return df


def _update_added_entries(added_entries: Dict, new_entries: Dict) -> Dict:
    added_entries["mappings"] = {**added_entries["mappings"], **new_entries["mappings"]}
    added_entries["entries"] = {**added_entries["entries"], **new_entries["entries"]}
    return added_entries
