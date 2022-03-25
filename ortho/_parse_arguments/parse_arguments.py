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

import os
import sys
import getopt


# =============
# Print Version
# =============

def print_version():
    """
    Prints the version of the code given in.
    """

    # Get the parent directory of this script
    file_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.dirname(file_directory)

    # Find the version
    version_dummy = {}
    exec(open(os.path.join(parent_directory, '__version__.py'), 'r').read(),
         version_dummy)
    version = version_dummy['__version__']
    del version_dummy

    # String to print
    version_string = \
        """
Version %s
        """ % (version)

    print(version_string)


# =============
# Print License
# =============

def print_license():
    """
    Prints the license and author info.
    """

    license_string = \
        """
Author:
Siavash Ameli
University of California, Berkeley
April 27, 2020

License: BSD-3-Clause
        """

    print(license_string)


# ===========
# Print Usage
# ===========

def print_usage(exec_name):
    """
    Prints the usage for the stand-alone application.
    """

    usage_string = \
        """
Usage:
$ %s  [options]
        """ % (exec_name)

    options_string = \
        """
Optional arguments:

-h --help                   Prints this help message.
-v --version                Prints version
-l --license                Prints author info, citation and license.
-n --num-func[=int]         Number of orthogonal functions to generate.
                            Positive integer. Default is 9.
-s --start-func[=int]       Starting function index. Non-negative integer.
                            Default is 1.
-e --end-interval[=float]   End of the interval of functions domains. Real
                            number greater than zero. Default is 1.
-c --check                  Checks orthogonality of generated functions.
-p --plot                   Plots generated functions, also saves the plot as
                            pdf and svg file in the current directory.
            """

    example_string = \
        """
Description:

This script generates a set of orthonormal functions, called phi_perp, based on
the set of non-orthonormal functions

    phi_i(t) = t**(1/(i+i)),      i = I, ... , I+N

The orthonormalized functions phi_perp_i are linear combination of the
functions phi_i, as

    phi_perp_i(t) = alpha_i * sum_{j=I}^{I+N} a_{ij} phi_j(t)

The functions phi_perp are orthonormal in the interval [0, L] with respect to
weight w(t) = 1/t. That is

    int_0^L phi_perp_i(t) phi_perp_j(t) 1/t dt = delta_{ij}

where delta_{ij} is the Kronecker delta function.

The script can be configured as follows:

   Variable     Variable in script              Option
   --------    --------------------    -------------------------
      I         "StartFunctionIndex"    "-s", or "--start-func"
      N         "NumFunctions"          "-n", or "--num-func"
      L         "EndInterval"           "-e", or "--end-interval"

Output:

1. Prints the symbolic functions
2. Prints a human readable coefficients, "alpha" and "a" of the functions
3. Prints a matrix of mutual inner product of functions to check orthogonality
   (with option "-c")
4. Plots the set of functions (with option "-p")
5. Saves the plot as pdf and svg in the current directory (with option "-p")

Examples:

1. Generate nine orthogonal functions from function index 1 to 9
    $ %s

2. Generate seven orthogonal functions from function index 1 to 8
    $ %s -n 8

3. Generate nine orthogonal functions from function index 0 to 8
    $ %s -s 0

4. Generate nine set of orthogonal functions starting from function 1, that are
   orthonormal in the interval [0, 10]
    $ %s -e 10

5. Check orthogonality of each two function, and plot the orthonormal functions
   and save the plot to pdf and svg
    $ %s -c -p

6. A complete example:
    $ %s -n 9 -s 1 -e 1 -c -p

        """ % (exec_name, exec_name, exec_name, exec_name, exec_name,
               exec_name)

    print(usage_string)
    print(options_string)
    print(example_string)


# ===============
# Parse Arguments
# ===============

def parse_arguments(argv, test=False):
    """
    Parses the argument of the executable.

    :param argv: list of keys and user inputs.
    :type: list

    :param Test: If ``True``, the program is not exited after options ``-h``,
        ``-v``, and ``-l``.
        If ``False``, the program is exited by the above options.
    :type Test: bool
    """

    # Initialize variables (defaults)
    arguments = {
        'check_orthogonality': False,
        'plot_flag': False,
    }

    try:
        opts, args = getopt.getopt(argv[1:], "hvln:s:e:cp", [
            "help", "version", "license", "num-func=", "start-func=",
            "end-interval=", "check", "plot"])
    except getopt.GetoptError:
        print('Invalid option entered.')
        print_usage(argv[0])
        sys.exit(2)

    # Assign options
    for opt, arg in opts:

        if opt in ('-h', '--help'):
            print_usage(argv[0])
            if not test:
                sys.exit(0)
        elif opt in ('-v', '--version'):
            print_version()
            if not test:
                sys.exit(0)
        elif opt in ("-l", "--license"):
            print_license()
            if not test:
                sys.exit(0)
        elif opt in ("-n", "--num-func"):
            arguments['num_func'] = int(arg)
        elif opt in ("-s", "--start-func"):
            arguments['start_index'] = int(arg)
        elif opt in ("-e", "--end-interval"):
            arguments['end_interval'] = float(arg)
        elif opt in ("-c", '--check'):
            arguments['check_orthogonality'] = True
        elif opt in ("-p", "--plot"):
            arguments['plot_flag'] = True

    return arguments
