from typing import Optional

from sqlmodel import Field, SQLModel


class techsample(SQLModel, table=True):  # type: ignore
    """Tech samples that are generated due to instrument units."""

    id: Optional[int] = Field(default=None, primary_key=True)
    external_id: str = Field(default=None, index=True, unique=True)
    name: str = Field(default=None, index=True)
    batch: Optional[str] = None
    filepath_r1: Optional[str] = None
    filepath_r2: Optional[str] = None
