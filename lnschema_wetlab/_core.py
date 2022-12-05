from datetime import datetime as datetime
from typing import Optional

from lndb_setup import settings
from lnschema_bionty import CellType, Disease, Species, Tissue
from lnschema_core import DObject, Project  # noqa
from lnschema_core._timestamps import CreatedAt, UpdatedAt
from lnschema_core._users import CreatedBy
from lnschema_core.dev.sqlmodel import schema_sqlmodel
from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship

from . import _name as schema_name
from ._link import (  # noqa
    BiosampleTechsample,
    DObjectBiosample,
    DObjectExperiment,
    DObjectReadout,
    ProjectExperiment,
)
from .dev import id as idg

SQLModel, prefix, schema_arg = schema_sqlmodel(schema_name)


class Treatment(SQLModel, table=True):  # type: ignore
    """Treatment."""

    id: str = Field(default_factory=idg.treatment, primary_key=True)
    external_id: str = Field(default=None, unique=True, index=True)
    name: str = Field(default=None, index=True)
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt


class BiosampleBase(SQLModel):  # type: ignore
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
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt


class TechsampleBase(SQLModel):  # type: ignore
    """Tech samples that are generated due to instrument units."""

    id: str = Field(default_factory=idg.techsample, primary_key=True)
    external_id: Optional[str] = Field(default=None, index=True, unique=True)
    name: Optional[str] = Field(default=None, index=True)
    batch: Optional[str] = None
    filepath_r1: Optional[str] = None
    filepath_r2: Optional[str] = None
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt


if "wetlab" in settings.instance.schema:

    class Biosample(BiosampleBase, table=True):  # type: ignore
        """Biological samples that are registered in experiments."""

        species: Species = Relationship()
        tissue: Tissue = Relationship()
        cell_type: CellType = Relationship()
        disease: Disease = Relationship()
        treatment: Treatment = Relationship()
        dobjects: DObject = Relationship(
            back_populates="biosamples",
            sa_relationship_kwargs=dict(secondary=DObjectBiosample.__table__),
        )

    DObject.biosamples = relationship(
        Biosample, back_populates="dobjects", secondary=DObjectBiosample.__table__
    )
    DObject.__sqlmodel_relationships__["biosamples"] = None

    class Techsample(TechsampleBase, table=True):  # type: ignore
        biosamples: Biosample = Relationship(
            back_populates="techsamples",
            sa_relationship_kwargs=dict(secondary=BiosampleTechsample.__table__),
        )

    Biosample.techsamples = relationship(
        Techsample, back_populates="biosamples", secondary=BiosampleTechsample.__table__
    )

else:
    Biosample = None  # type: ignore
    Techsample = None  # type: ignore


class Readout(SQLModel, table=True):  # type: ignore
    """Readout of experiments."""

    id: str = Field(default_factory=idg.readout, primary_key=True)
    efo_id: str = Field(default=None, unique=True, index=True)
    name: Optional[str] = None
    molecule: Optional[str] = None
    instrument: Optional[str] = None
    measurement: Optional[str] = None
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    dobjects: DObject = Relationship(
        back_populates="readouts",
        sa_relationship_kwargs=dict(secondary=DObjectReadout.__table__),
    )


DObject.readouts = relationship(
    Readout,
    back_populates="dobjects",
    secondary=DObjectReadout.__table__,
)
DObject.__sqlmodel_relationships__["readouts"] = None


class Experiment(SQLModel, table=True):  # type: ignore
    """Experiments."""

    id: str = Field(default_factory=idg.experiment, primary_key=True)
    external_id: str = Field(default=None, unique=True)
    name: str = Field(default=None, index=True)
    date: datetime = Field(default=None, index=True)
    experiment_type_id: str = Field(
        default=None, foreign_key="wetlab.experiment_type.id", index=True
    )
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    dobjects: DObject = Relationship(
        back_populates="experiments",
        sa_relationship_kwargs=dict(secondary=DObjectExperiment.__table__),
    )
    # projects: Project = Relationship(
    #     back_populates="experiments",
    #     sa_relationship_kwargs=dict(secondary=ProjectExperiment.__table__),
    # )


DObject.experiments = relationship(
    Experiment, back_populates="dobjects", secondary=DObjectExperiment.__table__
)
DObject.__sqlmodel_relationships__["experiments"] = None

# Project.experiments = relationship(
#     Experiment, back_populates="projects", secondary=ProjectExperiment.__table__
# )
# Project.__sqlmodel_relationships__["experiments"] = None


class ExperimentType(SQLModel, table=True):  # type: ignore
    """Experiment types."""

    __tablename__ = f"{prefix}experiment_type"

    id: str = Field(default_factory=idg.experiment_type, primary_key=True)
    name: str = Field(default=None, index=True)
    efo_id: str = Field(default=None, unique=True)
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
