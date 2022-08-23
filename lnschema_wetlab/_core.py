from datetime import datetime as datetime
from typing import Optional  # noqa

from lnschema_bionty import featureset, species  # noqa
from sqlmodel import Field, SQLModel


def utcnow():
    return datetime.utcnow().replace(microsecond=0)


class version_vvhc(SQLModel, table=True):  # type: ignore
    """Schema module version."""

    v: Optional[str] = Field(primary_key=True)
    user_id: str = Field(foreign_key="user.id")
    time_created: datetime = Field(default_factory=utcnow, nullable=False)


class dobject_biometa(SQLModel, table=True):  # type: ignore
    """Link between dobject and meta."""

    dobject_id: Optional[str] = Field(
        default=None, foreign_key="dobject.id", primary_key=True
    )
    biometa_id: Optional[int] = Field(
        default=None, foreign_key="biometa.id", primary_key=True
    )


class biometa(SQLModel, table=True):  # type: ignore
    """Metadata is a combination of biosample and experiment."""

    id: Optional[int] = Field(default=None, primary_key=True)
    biosample_id: int = Field(default=None, foreign_key="biosample.id")
    readout_type_id: int = Field(default=None, foreign_key="readout_type.id")
    featureset_id: int = Field(default=None, foreign_key="featureset.id")
    experiment_id: int = Field(default=None, foreign_key="experiment.id")


class biosample(SQLModel, table=True):  # type: ignore
    """Biological samples that are registered in experiments."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    species_id: int = Field(default=None, foreign_key="species.id")


class readout_type(SQLModel, table=True):  # type: ignore
    """Readout type of experiments."""

    id: Optional[int] = Field(default=None, primary_key=True)
    efo_id: str = Field(default=None, index=True)
    name: str = Field(default=None, index=True)
    molecule: str = Field(default=None)
    instrument: str = Field(default=None)
    measurement: str = Field(default=None)


class experiment(SQLModel, table=True):  # type: ignore
    """Experiments."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    project: str = Field(default=None)
    experiment_type_id: int = Field(default=None, foreign_key="experiment_type.id")


class experiment_type(SQLModel, table=True):  # type: ignore
    """Experiment types."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    efo_id: str = Field(default=None)
