"""Schema module for a generic wetlab (`vvhc`).

Import the package::

   import lnschema_wetlab

This is the complete API reference:

.. autosummary::
   :toctree: .

   biometa
   biosample
   techsample
   project
   experiment
   experiment_type
   dobject_biometa
   readout

Tracking versions & migrations:

.. autosummary::
   :toctree: .

   version_vvhc
   migration_vvhc

"""
# This is lnschema-module vvhc.
_schema = "vvhc"
_migration = None
__version__ = "0.4.0"
_tables = ["biosample", "techsample"]

from ._core import (  # noqa
    biometa,
    dobject_biometa,
    experiment,
    experiment_type,
    migration_vvhc,
    project,
    readout,
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

# if "readout" in _tables:
#    from ._readout import readout
