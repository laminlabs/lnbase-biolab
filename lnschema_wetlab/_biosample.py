from datetime import datetime as datetime
from typing import Optional

from lnschema_core._timestamps import CreatedAt, UpdatedAt
from sqlmodel import Field, SQLModel

from . import id as idg


class biosample(SQLModel, table=True):  # type: ignore
    """Biological samples that are registered in experiments."""

    id: str = Field(default_factory=idg.biosample, primary_key=True)
    external_id: Optional[str] = Field(default=None, index=True, unique=True)
    name: Optional[str] = Field(default=None, index=True)
    batch: Optional[str] = None
    species_id: Optional[str] = Field(
        default=None, foreign_key="species.id", index=True
    )
    tissue_id: Optional[str] = Field(default=None, foreign_key="tissue.id", index=True)
    cell_type_id: Optional[str] = Field(
        default=None, foreign_key="cell_type.id", index=True
    )
    disease_id: Optional[str] = Field(
        default=None, foreign_key="disease.id", index=True
    )
    cell_marker_id: Optional[str] = Field(
        default=None, foreign_key="cell_marker.id", index=True
    )
    treatment_id: Optional[str] = Field(
        default=None, foreign_key="treatment.id", index=True
    )
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt
