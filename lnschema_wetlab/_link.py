from lndb import settings
from lnschema_core.dev.sqlmodel import schema_sqlmodel
from sqlmodel import Field

from . import _name as schema_name

SQLModel, prefix, schema_arg = schema_sqlmodel(schema_name)


if "wetlab" in settings.instance.schema:

    class ProjectExperiment(SQLModel, table=True):  # type: ignore
        """Links `Project` and `Experiment`."""

        __tablename__ = f"{prefix}project_experiment"

        project_id: str = Field(foreign_key="core.project.id", primary_key=True)
        experiment_id: str = Field(foreign_key="wetlab.experiment.id", primary_key=True)

    class FileExperiment(SQLModel, table=True):  # type: ignore
        """Links for `File` and `Experiment`."""

        __tablename__ = f"{prefix}file_experiment"

        file_id: str = Field(foreign_key="core.file.id", primary_key=True)
        experiment_id: str = Field(foreign_key="wetlab.experiment.id", primary_key=True)

    class FileReadout(SQLModel, table=True):  # type: ignore
        """Links for `File` and `Readout`."""

        __tablename__ = f"{prefix}file_readout"

        file_id: str = Field(foreign_key="core.file.id", primary_key=True)
        readout_id: str = Field(foreign_key="wetlab.readout.id", primary_key=True)

    class BiosampleTechsample(SQLModel, table=True):  # type: ignore
        """Links for `Biosample` and `Techsample`."""

        __tablename__ = f"{prefix}biosample_techsample"

        biosample_id: str = Field(foreign_key="wetlab.biosample.id", primary_key=True)
        techsample_id: str = Field(foreign_key="wetlab.techsample.id", primary_key=True)

    class FileBiosample(SQLModel, table=True):  # type: ignore
        """Links for `File` and `Biosample`."""

        __tablename__ = f"{prefix}file_biosample"

        file_id: str = Field(foreign_key="core.file.id", primary_key=True)
        biosample_id: str = Field(foreign_key="wetlab.biosample.id", primary_key=True)

else:
    ProjectExperiment = None  # type: ignore
    FileExperiment = None  # type: ignore
    BiosampleTechsample = None  # type: ignore
    FileBiosample = None  # type: ignore
    FileReadout = None  # type: ignore
