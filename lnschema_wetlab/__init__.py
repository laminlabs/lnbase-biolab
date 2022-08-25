"""Schema module for a generic wetlab (`vvhc`).

Import the package::

   import lnschema_wetlab

This is the complete API reference:

.. autosummary::
   :toctree: .

   biometa
   biosample
   techsample
   experiment
   experiment_type
   dobject_biometa
   readout_type
   version_vvhc
"""
# This is lnschema-module vvhc.
_schema_module_id = "vvhc"
__version__ = "0.3.0"
_tables = ["biosample", "techsample"]

from ._core import (  # noqa
    biometa,
    dobject_biometa,
    experiment,
    experiment_type,
    readout_type,
    version_vvhc,
)

if "biosample" in _tables:
    from ._biosample import biosample

if "techsample" in _tables:
    from ._techsample import techsample

# if "experiment" in _tables:
#    from ._experiment import experiment

# if "experiment_type" in _tables:
#    from ._experiment_type import experiment_type

# if "readout_type" in _tables:
#    from ._readout_type import readout_type
