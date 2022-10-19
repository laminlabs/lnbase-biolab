"""Schema module for a generic wetlab (`vvhc`).

Import the package::

   import lnschema_wetlab

This is the complete API reference:

.. autosummary::
   :toctree: .

   biometa
   dobject_biometa
   biosample
   techsample
   biosample_techsample
   project
   readout
   treatment
   experiment
   experiment_type
   migration_vvhc
   version_vvhc

Tracking versions & migrations:

.. autosummary::
   :toctree: .

   version_vvhc
   migration_vvhc

"""
# This is lnschema-module vvhc.
_schema_id = "vvhc"
_migration = "01360b6492cc"
__version__ = "0.7.0"

from ._biosample import biosample
from ._core import (  # noqa
    biometa,
    dobject_biometa,
    experiment,
    experiment_type,
    migration_vvhc,
    project,
    readout,
    treatment,
    version_vvhc,
)
from ._techsample import biosample_techsample, techsample
