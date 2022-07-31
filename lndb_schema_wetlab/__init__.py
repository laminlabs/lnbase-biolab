"""Wetlab schema module.

Import the package::

   import lndb_schema_wetlab

This is the complete API reference:

.. autosummary::
   :toctree: .

   biometa
   biosample
   dobject_biometa
   readout_type
"""

__version__ = "0.1.0"  # denote a pre-release for 0.1.0 with 0.1a1

from ._core import biometa, biosample, dobject_biometa, readout_type  # noqa
