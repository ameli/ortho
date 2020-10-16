#! /usr/bin/env python

# =======
# Imports
# =======

import sys
from OrthogonalFunctions import OrthogonalFunctions

# matplotlib without display
import matplotlib
matplotlib.use('Agg')

# =========================
# Test Orthogonal Functions
# =========================

def test_OrthogonalFunctions():

    Arguments = \
    {
        'NumFunctions': 8,
        'StartFunctionIndex': 1,
        'EndInterval': 1
    }

    # Create an object
    OF = OrthogonalFunctions(**Arguments)

    # Compute the orthogonal functions
    OF.Process()

    # Print the results
    OF.Print()

    # Check the orthogonality of the functions
    OF.Check()

    # Plot the results
    OF.Plot()

# ===========
# System Main
# ===========

if __name__ == "__main__":
    test_OrthogonalFunctions()
