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
_migration = "a171e861e473"
__version__ = "0.7.1"

from ._biosample import biosample
from ._core import (  # noqa
    biometa,
    dobject_biometa,
    experiment,
    experiment_type,
    migration_vvhc,
    readout,
    treatment,
    version_vvhc,
)
from ._techsample import biosample_techsample, techsample
