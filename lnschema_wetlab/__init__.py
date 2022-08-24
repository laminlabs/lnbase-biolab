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
__version__ = "0.2.4"

from ._core import (  # noqa
    biometa,
    biosample,
    dobject_biometa,
    experiment,
    experiment_type,
    readout_type,
    techsample,
    version_vvhc,
)
