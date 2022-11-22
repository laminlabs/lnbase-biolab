from lnschema_core import DObject
from lnschema_core.dev.sqlmodel import schema_sqlmodel
from sqlalchemy.orm import relationship
from sqlmodel import Field

from . import _name as schema_name
from ._core import Biosample, Experiment, Readout

SQLModel, prefix, schema_arg = schema_sqlmodel(schema_name)


class ProjectExperiment(SQLModel, table=True):  # type: ignore
    """Links `Project` and `Experiment`."""

    __tablename__ = f"{prefix}project_experiment"

    project_id: str = Field(foreign_key="core.project.id", primary_key=True)
    experiment_id: str = Field(foreign_key="wetlab.experiment.id", primary_key=True)


class BiosampleTechsample(SQLModel, table=True):  # type: ignore
    """Links for `Biosample` and `Techsample`."""

    __tablename__ = f"{prefix}biosample_techsample"

    biosample_id: str = Field(foreign_key="wetlab.biosample.id", primary_key=True)
    techsample_id: str = Field(foreign_key="wetlab.techsample.id", primary_key=True)


class DObjectExperiment(SQLModel, table=True):  # type: ignore
    """Links for `DObject` and `Experiment`."""

    __tablename__ = f"{prefix}dobject_experiment"

    dobject_id: str = Field(foreign_key="core.dobject.id", primary_key=True)
    experiment_id: str = Field(foreign_key="wetlab.experiment.id", primary_key=True)


class DObjectBiosample(SQLModel, table=True):  # type: ignore
    """Links for `DObject` and `Biosample`."""

    __tablename__ = f"{prefix}dobject_biosample"

    dobject_id: str = Field(foreign_key="core.dobject.id", primary_key=True)
    biosample_id: str = Field(foreign_key="wetlab.biosample.id", primary_key=True)


class DObjectReadout(SQLModel, table=True):  # type: ignore
    """Links for `DObject` and `Readout`."""

    __tablename__ = f"{prefix}dobject_readout"

    dobject_id: str = Field(foreign_key="core.dobject.id", primary_key=True)
    readout_id: str = Field(foreign_key="wetlab.readout.id", primary_key=True)


Experiment.dobjects = relationship(
    DObject, back_populates="experiments", secondary=DObjectExperiment.__table__
)
DObject.experiments = relationship(
    Experiment, back_populates="dobjects", secondary=DObjectExperiment.__table__
)
Biosample.dobjects = relationship(
    DObject, back_populates="biosamples", secondary=DObjectBiosample.__table__
)
DObject.biosamples = relationship(
    Biosample, back_populates="dobjects", secondary=DObjectBiosample.__table__
)
Readout.dobjects = relationship(
    DObject, back_populates="readouts", secondary=DObjectReadout.__table__
)
DObject.readouts = relationship(
    Readout,
    secondary=DObjectReadout.__table__,  # no back_populates as these can be many
)
