#! /usr/bin/env python

# =======
# Imports
# =======

import sys

# Depending on python 2 or 3, import relative to the directory or the package
if sys.version_info[0] == 2:
    # For python 2
    from ParseArguments import ParseArguments
    from OrthogonalFunctions import OrthogonalFunctions
else:
    # Python 3
    from OrthogonalFunctions import ParseArguments
    from OrthogonalFunctions import OrthogonalFunctions

# ====
# Main
# ====

def main(args=None):

    # User arguments
    if args is None:
        args = sys.argv

    # Parse arguments 
    Arguments = ParseArguments(args)

    # Create an object
    OF = OrthogonalFunctions(**Arguments)

    # Compute the orthogonal functions
    OF.Process()

    # Print the results
    OF.Print()

    # Check the orthogonality of the functions
    if Arguments['CheckOrthogonality']:
        OF.Check()

    # Plot results
    if Arguments['PlotFlag']:
        OF.Plot()

# ===========
# System Main
# ===========

if __name__ == "__main__":
    sys.exit(main())
