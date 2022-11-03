from datetime import datetime as datetime
from typing import Optional  # noqa

from lnschema_core._timestamps import CreatedAt
from lnschema_core._users import CreatedBy
from lnschema_core.dev.sqlmodel import schema_sqlmodel
from sqlmodel import Field

from . import _name as schema_name
from .dev import id as idg

SQLModel, prefix, schema_arg = schema_sqlmodel(schema_name)


# fmt: off
class DObjectBiometa(SQLModel, table=True):  # type: ignore
    """Link :class:`~lnschema_wetlab.Biometa` and `DObject <https://lamin.ai/docs/lnschema-core/lnschema_core.DObject>`__."""  # noqa
# fmt: on

    __tablename__ = f"{prefix}dset_dobject"

    dobject_id: str = Field(foreign_key="core.dobject.id", primary_key=True)
    biometa_id: str = Field(foreign_key="wetlab.biometa.id", primary_key=True)


class Biometa(SQLModel, table=True):  # type: ignore
    """Metadata is a combination of biosample and experiment."""

    id: str = Field(default_factory=idg.biometa, primary_key=True)
    experiment_id: str = Field(default=None, foreign_key="wetlab.experiment.id", index=True)  # noqa
    biosample_id: str = Field(default=None, foreign_key="wetlab.biosample.id", index=True)  # noqa
    readout_id: str = Field(default=None, foreign_key="wetlab.readout.id", index=True)
    featureset_id: str = Field(default=None, foreign_key="wetlab.featureset.id", index=True)  # noqa
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt


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


class Treatment(SQLModel, table=True):  # type: ignore
    """Treatment."""

    id: str = Field(default_factory=idg.treatment, primary_key=True)
    external_id: str = Field(default=None, unique=True, index=True)
    name: str = Field(default=None, index=True)
    created_at: datetime = CreatedAt
