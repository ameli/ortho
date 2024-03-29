#! /usr/bin/env python

# SPDX-FileCopyrightText: Copyright 2021, Siavash Ameli <sameli@berkeley.edu>
# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileType: SOURCE
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the license found in the LICENSE.txt file in the root directory
# of this source tree.


# =======
# Imports
# =======

# matplotlib without display
import os
import matplotlib
matplotlib.use('Agg')

from ortho import OrthogonalFunctions                              # noqa: E402

import warnings                                                    # noqa: E402
warnings.resetwarnings()
warnings.filterwarnings("error")


# ===========
# remove file
# ===========

def remove_file(filename):
    """
    Remove file.
    """

    if os.path.exists(filename):
        os.remove(filename)


# =========================
# Test Orthogonal Functions
# =========================

def test_orthogonal_functions():

    arguments = {
        'num_func': 9,
        'start_index': 1,
        'end_interval': 1
    }

    # Create an object
    OF = OrthogonalFunctions(**arguments)

    # Print the results
    OF.print()

    # Check the orthogonality of the functions
    OF.check(verbose=True)

    # Plot the results
    OF.plot(filename='orthogonal_functions')

    # Remove saved plots
    remove_file('orthogonal_functions.svg')
    remove_file('orthogonal_functions.pdf')


# ===========
# Script Main
# ===========

if __name__ == "__main__":
    test_orthogonal_functions()
