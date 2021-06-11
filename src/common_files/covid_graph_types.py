from typing import TYPE_CHECKING, TypeVar, Optional, List, Sequence, Tuple
assert TYPE_CHECKING, "Can't import this module at runtime!"
from src.common_files.graph_plotting import GraphPlotter
from pandas import DataFrame

GraphPlotterTypeVar = TypeVar('GraphPlotterTypeVar', bound=GraphPlotter)
OPTIONAL_STR = Optional[str]
STRING_LIST = List[str]
STRING_SEQUENCE = Sequence[str]
DATA_FRAME_LIST = List[DataFrame]
IMAGE_AND_TITLE = Tuple[str, str]
