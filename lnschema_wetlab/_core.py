from datetime import datetime as datetime
from typing import Optional  # noqa

from lnschema_core._timestamps import CreatedAt
from lnschema_core._users import CreatedBy
from sqlmodel import Field, SQLModel

from . import id as idg


# fmt: off
class dobject_biometa(SQLModel, table=True):  # type: ignore
    """Link :class:`~lnschema_wetlab.biometa` and `dobject <https://lamin.ai/docs/lnschema-core/lnschema_core.dobject>`__."""  # noqa
# fmt: on

    dobject_id: str = Field(foreign_key="dobject.id", primary_key=True)
    biometa_id: str = Field(foreign_key="biometa.id", primary_key=True)


class biometa(SQLModel, table=True):  # type: ignore
    """Metadata is a combination of biosample and experiment."""

    id: str = Field(default_factory=idg.biometa, primary_key=True)
    experiment_id: str = Field(default=None, foreign_key="experiment.id", index=True)
    biosample_id: str = Field(default=None, foreign_key="biosample.id", index=True)
    readout_id: str = Field(default=None, foreign_key="readout.id", index=True)
    featureset_id: str = Field(default=None, foreign_key="featureset.id", index=True)
    created_at: datetime = CreatedAt


class readout(SQLModel, table=True):  # type: ignore
    """Readout of experiments."""

    id: str = Field(default_factory=idg.readout, primary_key=True)
    efo_id: str = Field(default=None, unique=True, index=True)
    name: Optional[str] = None
    molecule: Optional[str] = None
    instrument: Optional[str] = None
    measurement: Optional[str] = None
    created_at: datetime = CreatedAt


class experiment(SQLModel, table=True):  # type: ignore
    """Experiments."""

    id: str = Field(default_factory=idg.experiment, primary_key=True)
    external_id: str = Field(default=None, unique=True)
    name: Optional[str] = Field(default=None, index=True)
    date: datetime = Field(default=None, index=True)
    project_id: str = Field(default=None, foreign_key="project.id", index=True)
    experiment_type_id: str = Field(
        default=None, foreign_key="experiment_type.id", index=True
    )
    created_at: datetime = CreatedAt


class experiment_type(SQLModel, table=True):  # type: ignore
    """Experiment types."""

    id: str = Field(default_factory=idg.experiment, primary_key=True)
    name: Optional[str] = None
    efo_id: str = Field(default=None, unique=True)
    created_at: datetime = CreatedAt


class project(SQLModel, table=True):  # type: ignore
    """Project."""

    id: str = Field(default_factory=idg.project, primary_key=True)
    external_id: str = Field(default=None, unique=True, index=True)
    name: Optional[str] = Field(default=None, index=True)
    created_at: datetime = CreatedAt
    created_by: str = CreatedBy


class treatment(SQLModel, table=True):  # type: ignore
    """Treatment."""

    id: str = Field(default_factory=idg.treatment, primary_key=True)
    external_id: str = Field(default=None, unique=True, index=True)
    name: Optional[str] = Field(default=None, index=True)
    created_at: datetime = CreatedAt


class version_vvhc(SQLModel, table=True):  # type: ignore
    """Wetlab schema module versions deployed in a given instance.

    Migrations of the schema module add rows to this table, storing the schema
    module version to which we migrated along with the user who performed the
    migration.
    """

    v: str = Field(primary_key=True)
    migration: Optional[str] = None
    user_id: str = CreatedBy
    created_at: datetime = CreatedAt


class migration_vvhc(SQLModel, table=True):  # type: ignore
    """Latest migration.

    This stores the reference to the latest migration script deployed.
    """

    version_num: Optional[str] = Field(primary_key=True)
