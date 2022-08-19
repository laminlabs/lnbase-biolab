"""Schema module for a generic wetlab (`vvhc`).

Import the package::

   import lnschema_wetlab

This is the complete API reference:

.. autosummary::
   :toctree: .

   biometa
   biosample
   dobject_biometa
   readout_type
   version_vvhc
"""
# This is lnschema-module vvhc.
_schema_module_id = "vvhc"
__version__ = "0.1.2"  # denote a pre-release for 0.1.0 with 0.1a1

from ._core import (  # noqa
    biometa,
    biosample,
    dobject_biometa,
    readout_type,
    version_vvhc,
)
