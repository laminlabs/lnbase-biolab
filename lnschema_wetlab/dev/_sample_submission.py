from typing import Dict, List, Union

import pandas as pd
import sqlalchemy as sql
import sqlmodel as sqm


def parse_and_insert_df(df: pd.DataFrame, target_table: str) -> Dict[str, Dict]:
    added_entries = {"mappings": {}, "entries": {}}  # type: ignore
    try:
        # insert columns into relevant tables
        mapper = map_cols_to_tables(df, target_table)
        added_entries = _add_columns(df, mapper)
        df = _populate_cols_with_pks(df, added_entries)
        # insert dataframe into sample table
        sample_sqa = get_sample_table(target_table)
        sample_sqm = get_sqm_tables(sample_sqa.name)
        df_entries = add_from_df(df, sample_sqm)
        added_entries = _update_added_entries(added_entries, df_entries)
    except Exception as e:
        _delete_added_entries(added_entries)
        raise e
    return added_entries


def add_from_column(
    pd_series: pd.Series, table: sqm.SQLModel, table_column: str
) -> Dict[str, Dict]:
    """Quick-insert entries into LaminDB from a DataFrame column.

    This only writes one single column of each entry into the database.
    """
    import lamindb as ln

    entries = pd_series.unique().tolist()
    table_name = str(table.__table__.name)
    added_entries = {"mappings": {}, "entries": {}}  # type: ignore
    added_entries["mappings"][pd_series.name] = (table_name, table_column)
    added_entries["entries"][table_name] = []
    for value in entries:
        if value is None:
            continue
        try:
            entry_data = {table_column: value}
            db_entry = ln.add(table, **entry_data)
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
    df_temp = df_temp.fillna("None")

    # Get the intersection between df and table columns
    common_fields = set(table.__fields__.keys()).intersection(df_temp.columns)
    common_df_as_records = df_temp[list(common_fields)].to_dict(orient="records")

    # Add df rows to db
    entries = []
    for row in common_df_as_records:
        try:
            entries += [ln.add(table, **row)]
        except Exception as e:
            _delete_added_entries(added_entries)
            raise e

    # format return mappings and entries
    table_name = str(table.__table__.name)
    for field in common_fields:
        try:
            df_col = match_col_from_df(df, field)
            added_entries["mappings"][df_col] = (table_name, field)
        except KeyError:
            # ignore KeyError for intermediate field (pks with fk constraints)
            if field == "id":
                pass
    added_entries["entries"][table_name] = entries

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


def get_sample_table(sample: str) -> sql.schema.Table:
    """Get a single sqlalchemy table for the sample of interest."""
    tables = get_sql_tables(sample)
    if not tables:
        raise ValueError(f"Table {sample} does not exist.")
    elif len(tables) == 1:
        return tables[0]
    for table in tables:
        if "wetlab" not in table.name:
            return table


def get_sql_tables(table_name: str) -> List[sql.schema.Table]:
    """Get LaminDB sqlalchemy tables whose name perfectly match the input."""
    import lamindb as ln

    tables = ln.schema._core.get_db_metadata().sorted_tables
    matched = [tab for tab in tables if tab.name.split(".")[-1] == table_name]
    return matched


def get_sql_fk_tables(table: sql.schema.Table) -> List[sql.schema.Table]:
    """Get all tables associated with the input table (by fk constraint)."""
    return [fk.column.table for fk in table.foreign_keys]


def get_sqm_tables(name: str) -> sqm.main.SQLModelMetaclass:
    from functools import reduce
    from inspect import getmembers, isclass

    import lamindb as ln

    name_components = name.split(".")
    module = reduce(getattr, name_components[:-1], ln.schema)
    members = getmembers(module, isclass)
    for member in members:
        if name_components[-1] == _camel_to_snake(member[0]):
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
    sample_table = get_sample_table(target_table)
    sample_fk_tables = get_sql_fk_tables(sample_table)
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
        raise e
    return added_entries


def _camel_to_snake(string: str) -> str:
    import re

    return re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()


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
        # handle possible SQLModel casting
        for value in df[col].unique().tolist():
            if str(value) in id_mapper.keys():
                id_mapper[value] = id_mapper[str(value)]
        df[col] = df[col].map(id_mapper)
        df = df.rename(columns={col: f"{col} ID"})
    return df


def _update_added_entries(added_entries: Dict, new_entries: Dict) -> Dict:
    added_entries["mappings"] = {**added_entries["mappings"], **new_entries["mappings"]}
    added_entries["entries"] = {**added_entries["entries"], **new_entries["entries"]}
    return added_entries
