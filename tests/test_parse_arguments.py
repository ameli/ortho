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

from ortho._parse_arguments import parse_arguments


# ====================
# Test Parse arguments
# ====================

def test_parse_arguments():

    # Mock user argument
    argv1 = ['', '-n', '8', '-s', '1', '-e', '1', '-c', '-p']
    argv2 = ['', '-h']
    argv3 = ['', '-l']
    argv4 = ['', '-v']

    # Parse arguments
    Test = True
    arguments1 = parse_arguments(argv1, Test)
    arguments2 = parse_arguments(argv2, Test)
    arguments3 = parse_arguments(argv3, Test)
    arguments4 = parse_arguments(argv4, Test)

    print('User arguments:')
    print(arguments1)
    print(arguments2)
    print(arguments3)
    print(arguments4)


# ===========
# Script Main
# ===========

if __name__ == "__main__":
    test_parse_arguments()
