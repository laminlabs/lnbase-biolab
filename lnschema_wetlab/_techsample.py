from datetime import datetime as datetime
from typing import Optional

from lnschema_core._timestamps import CreatedAt, UpdatedAt
from sqlmodel import Field, SQLModel

from . import id as idg


class techsample(SQLModel, table=True):  # type: ignore
    """Tech samples that are generated due to instrument units."""

    id: str = Field(default_factory=idg.techsample, primary_key=True)
    external_id: Optional[str] = Field(default=None, index=True, unique=True)
    name: Optional[str] = Field(default=None, index=True)
    batch: Optional[str] = None
    filepath_r1: Optional[str] = None
    filepath_r2: Optional[str] = None
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt
