"""Schema module for a generic wetlab (`vvhc`).

Import the package::

   import lnschema_wetlab

This is the complete API reference:

.. autosummary::
   :toctree: .

   Biometa
   DObjectBiometa
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
__version__ = "0.8.1"

from ._biosample import Biosample
from ._core import (  # noqa
    Biometa,
    DObjectBiometa,
    Experiment,
    ExperimentType,
    ProjectExperiment,
    Readout,
    Treatment,
)
from ._techsample import BiosampleTechsample, Techsample
