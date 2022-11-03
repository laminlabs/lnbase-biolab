from datetime import datetime as datetime
from typing import Optional

from lnschema_core._timestamps import CreatedAt
from lnschema_core._users import CreatedBy
from sqlmodel import Field, SQLModel


class version_vvhc(SQLModel, table=True):  # type: ignore
    """Wetlab schema module versions deployed in a given instance.

    Migrations of the schema module add rows to this table, storing the schema
    module version to which we migrated along with the user who performed the
    migration.
    """

    v: str = Field(primary_key=True)
    migration: Optional[str] = None
    user_id: str = CreatedBy
    created_at: datetime = CreatedAt


class migration_vvhc(SQLModel, table=True):  # type: ignore
    """Latest migration.

    This stores the reference to the latest migration script deployed.
    """

    version_num: Optional[str] = Field(primary_key=True)
