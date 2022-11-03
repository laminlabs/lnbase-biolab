from datetime import datetime as datetime
from typing import Optional

from lnschema_core._timestamps import CreatedAt, UpdatedAt
from lnschema_core.dev.sqlmodel import schema_sqlmodel
from sqlmodel import Field

from . import _name as schema_name
from .dev import id as idg

SQLModel, prefix, schema_arg = schema_sqlmodel(schema_name)


class Biosample(SQLModel, table=True):  # type: ignore
    """Biological samples that are registered in experiments."""

    id: str = Field(default_factory=idg.biosample, primary_key=True)
    external_id: Optional[str] = Field(default=None, index=True, unique=True)
    name: Optional[str] = Field(default=None, index=True)
    batch: Optional[str] = None
    species_id: Optional[str] = Field(
        default=None, foreign_key="bionty.species.id", index=True
    )
    tissue_id: Optional[str] = Field(
        default=None, foreign_key="bionty.tissue.id", index=True
    )
    cell_type_id: Optional[str] = Field(
        default=None, foreign_key="bionty.cell_type.id", index=True
    )
    disease_id: Optional[str] = Field(
        default=None, foreign_key="bionty.disease.id", index=True
    )
    treatment_id: Optional[str] = Field(
        default=None, foreign_key="wetlab.treatment.id", index=True
    )
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt
