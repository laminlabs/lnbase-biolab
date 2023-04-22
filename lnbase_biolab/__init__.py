"""Base classes for a lab schema in biology (`vvhc`).

Import the package::

   import lnbase_biolab

Base classes:

.. autosummary::
   :toctree: .

   ExperimentBase
   ExperimentTypeBase
   BiosampleBase
   TechsampleBase

Development tools:

.. autosummary::
   :toctree: .

   dev
   link

"""
_codeproject_id = "vvhc"
_name = "biolab"
__version__ = "0.15.0"

from . import dev
from ._core import (  # noqa
    BiosampleBase,
    ExperimentBase,
    ExperimentTypeBase,
    TechsampleBase,
)
