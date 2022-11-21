"""Schema module for a generic wetlab (`vvhc`).

Import the package::

   import lnschema_wetlab

This is the complete API reference:

.. autosummary::
   :toctree: .

   Biometa
   Biosample
   Techsample
   BiosampleTechsample
   Readout
   Treatment
   ProjectExperiment
   Experiment
   ExperimentType

Development tools:

.. autosummary::
   :toctree: .

   dev

"""
# This is lnschema-module vvhc.
_schema_id = "vvhc"
_name = "wetlab"
_migration = "bfda12fc80a8"
__version__ = "0.9.1"

from ._biosample import Biosample, Treatment
from ._core import (  # noqa
    Biometa,
    Experiment,
    ExperimentType,
    ProjectExperiment,
    Readout,
    dobject_biometa,
)
from ._techsample import BiosampleTechsample, Techsample
