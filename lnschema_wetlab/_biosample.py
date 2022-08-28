from datetime import datetime as datetime
from typing import Optional

from sqlmodel import Field, SQLModel


def utcnow():
    return datetime.utcnow().replace(microsecond=0)


class biosample(SQLModel, table=True):  # type: ignore
    """Biological samples that are registered in experiments."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None, index=True)
    batch: Optional[int] = None
    species_id: int = Field(default=None, foreign_key="species.id")
    tissue_id: str = Field(default=None, foreign_key="tissue.id")
    cell_type_id: str = Field(default=None, foreign_key="cell_type.id")
    disease_id: str = Field(default=None, foreign_key="disease.id")
    cell_marker_id: str = Field(default=None, foreign_key="cell_marker.id")
    techsample_id: int = Field(default=None, foreign_key="techsample.id")
