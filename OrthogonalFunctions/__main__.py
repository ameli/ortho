#! /usr/bin/env python

# =======
# Imports
# =======

import sys
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
