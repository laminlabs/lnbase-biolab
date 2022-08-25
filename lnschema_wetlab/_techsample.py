from typing import Optional

from sqlmodel import Field, SQLModel


class techsample(SQLModel, table=True):  # type: ignore
    """Tech samples that are generated due to instrument units."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None, index=True)
    batch: Optional[int] = None
