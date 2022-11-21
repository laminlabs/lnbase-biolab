from datetime import datetime as datetime
from typing import Optional  # noqa

from lnschema_core import DObject
from lnschema_core._timestamps import CreatedAt
from lnschema_core._users import CreatedBy
from lnschema_core.dev.sqlmodel import schema_sqlmodel
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship

from . import _name as schema_name
from ._biosample import Biosample
from .dev import id as idg

SQLModel, prefix, schema_arg = schema_sqlmodel(schema_name)

dobject_biometa = Table(
    f"{prefix}dobject_biometa",
    SQLModel.metadata,
    Column("dobject_id", ForeignKey("core.dobject.id"), primary_key=True),
    Column("biometa_id", ForeignKey("wetlab.biometa.id"), primary_key=True),
)


class Biometa(SQLModel, table=True):  # type: ignore
    """Metadata is a combination of biosample and experiment."""

    id: str = Field(default_factory=idg.biometa, primary_key=True)
    experiment_id: str = Field(
        default=None, foreign_key="wetlab.experiment.id", index=True
    )  # noqa
    biosample_id: str = Field(
        default=None, foreign_key="wetlab.biosample.id", index=True
    )  # noqa
    biosample: Biosample = Relationship()
    readout_id: str = Field(default=None, foreign_key="wetlab.readout.id", index=True)
    readout: "Readout" = Relationship()
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    dobjects: DObject = Relationship(
        back_populates="biometas",
        sa_relationship_kwargs=dict(secondary=dobject_biometa),
    )


DObject.biometas = relationship(
    Biometa, back_populates="dobjects", secondary=dobject_biometa
)


class Readout(SQLModel, table=True):  # type: ignore
    """Readout of experiments."""

    id: str = Field(default_factory=idg.readout, primary_key=True)
    efo_id: str = Field(default=None, unique=True, index=True)
    name: Optional[str] = None
    molecule: Optional[str] = None
    instrument: Optional[str] = None
    measurement: Optional[str] = None
    created_at: datetime = CreatedAt


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


class ProjectExperiment(SQLModel, table=True):  # type: ignore
    """Link table of project and experiment."""

    __tablename__ = f"{prefix}project_experiment"

    project_id: str = Field(foreign_key="core.project.id", primary_key=True)
    experiment_id: str = Field(foreign_key="wetlab.experiment.id", primary_key=True)


class ExperimentType(SQLModel, table=True):  # type: ignore
    """Experiment types."""

    __tablename__ = f"{prefix}experiment_type"

    id: str = Field(default_factory=idg.experiment_type, primary_key=True)
    name: str = Field(default=None, index=True)
    efo_id: str = Field(default=None, unique=True)
    created_at: datetime = CreatedAt
