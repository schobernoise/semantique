from semantique.blocks import *
from semantique.extent import SpatialExtent, TemporalExtent
from semantique.recipe import QueryRecipe

import semantique.datacube
import semantique.mapping
import semantique.operators
import semantique.reducers
import semantique.dimensions
import semantique.components

from importlib.metadata import version, PackageNotFoundError

try:
  __version__ = version("semantique")
except PackageNotFoundError:
  __version__ = "unknown"