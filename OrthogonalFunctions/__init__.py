# Depending on python 2 or 3, import relative to the directory or the package
import sys
if sys.version_info[0] == 2:
    # For python 2
    from .ParseArguments import ParseArguments
    from .OrthogonalFunctions import OrthogonalFunctions
else:
    # For python 3
    from OrthogonalFunctions.ParseArguments import ParseArguments
    from OrthogonalFunctions.OrthogonalFunctions import OrthogonalFunctions

from .__version__ import __version__
