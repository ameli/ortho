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

import sys

from OrthogonalFunctions._parse_arguments import parse_arguments
from OrthogonalFunctions import OrthogonalFunctions


# ====
# Main
# ====

def main(args=None):

    # User arguments
    if args is None:
        args = sys.argv

    # Parse arguments
    arguments = parse_arguments(args)

    # Create an object
    OF = OrthogonalFunctions(**arguments)

    # Compute the orthogonal functions
    OF.process()

    # Print the results
    OF.print()

    # Check the orthogonality of the functions
    if arguments['check_orthogonality']:
        OF.check()

    # Plot results
    if arguments['plot_flag']:
        OF.plot()


# ===========
# System Main
# ===========

if __name__ == "__main__":
    sys.exit(main())
