"""Schema module for a generic wetlab (`vvhc`).

Import the package::

   import lnschema_wetlab

This is the complete API reference:

.. autosummary::
   :toctree: .

   Biosample
   Techsample
   Readout
   Treatment
   Experiment
   ExperimentType

Development tools:

.. autosummary::
   :toctree: .

   dev
   link

"""
# This is lnschema-module vvhc.
_schema_id = "vvhc"
_name = "wetlab"
_migration = "bfda12fc80a8"
__version__ = "0.10.2"

from . import dev, link
from ._core import (  # noqa
    Biosample,
    Experiment,
    ExperimentType,
    Readout,
    Techsample,
    Treatment,
)
