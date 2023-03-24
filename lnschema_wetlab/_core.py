from datetime import datetime as datetime
from typing import Optional

from lndb import settings
from lnschema_core import File, Project  # noqa
from lnschema_core._timestamps import CreatedAt, UpdatedAt
from lnschema_core._users import CreatedBy
from lnschema_core.dev.sqlmodel import schema_sqlmodel
from sqlmodel import Field

from . import _name as schema_name
from .dev import id as idg

SQLModel, prefix, schema_arg = schema_sqlmodel(schema_name)


class ExperimentBase(SQLModel):  # type: ignore
    """Experiments."""

    id: str = Field(default_factory=idg.experiment, primary_key=True)
    name: str = Field(default=None, index=True)
    date: datetime = Field(default=None, index=True)
    """Date on which the experiment is performed."""
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt


class ExperimentTypeBase(SQLModel):  # type: ignore
    """Experiment types.

    Useful for bucketing experiments.
    """

    id: str = Field(default_factory=idg.experiment_type, primary_key=True)
    name: str = Field(default=None, index=True)
    efo_id: str = Field(default=None, unique=True)
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt


class BiosampleBase(SQLModel):  # type: ignore
    """Biosamples: the fundamental observational unit."""

    id: str = Field(default_factory=idg.biosample, primary_key=True)
    name: Optional[str] = Field(default=None, index=True)
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt

    # # relationships
    # @declared_attr
    # def species(self) -> Optional[Species]:
    #     return relationship("Species")


class TechsampleBase(SQLModel):  # type: ignore
    """Tech samples that are generated due to instrument units."""

    id: str = Field(default_factory=idg.techsample, primary_key=True)
    name: Optional[str] = Field(default=None, index=True)
    batch: Optional[str] = None
    filepath_r1: Optional[str] = None
    filepath_r2: Optional[str] = None
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt


class ReadoutBase(SQLModel):  # type: ignore
    """Readouts."""

    id: str = Field(default_factory=idg.readout, primary_key=True)
    efo_id: Optional[str] = Field(default=None, unique=True, index=True)
    name: Optional[str] = None
    molecule: Optional[str] = None
    instrument: Optional[str] = None
    measurement: Optional[str] = None
    created_by: str = CreatedBy
    created_at: datetime = CreatedAt
    updated_at: Optional[datetime] = UpdatedAt


# the following is just for testing purposes
if "wetlab" in settings.instance.schema:
    from ._actual import Biosample, Experiment, ExperimentType, Readout, Techsample

else:
    Experiment = None  # type: ignore
    ExperimentType = None  # type: ignore
    Biosample = None  # type: ignore
    Techsample = None  # type: ignore
    Readout = None  # type: ignore
