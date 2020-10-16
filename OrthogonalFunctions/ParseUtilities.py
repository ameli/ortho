# =======
# Imports
# =======

import sys
import getopt

# =============
# Print Version
# =============

def PrintVersion():

    VersionString = \
            """
Version 0.0.1
            """

    print(VersionString)

# =============
# Print License
# =============

def PrintLicense():

    LicenseString = \
            """
Author: 
Siavash Ameli
University of California, Berkeley
April 27, 2020

Citation:
Ameli, S. and Shadden. S. C., "Maximum Likelihood Estimation of Variance and Nugget in General Linear Model"

License: MIT
            """

    print(LicenseString)

# ===========
# Print Usage
# ===========

def PrintUsage(ExecName):
    UsageString = \
    """
Usage:
$ %s  [options]
    """%(ExecName)

    OptionsString = \
    """
Optional arguments:

-h --help                   Prints this help message.
-v --version                Prints version
-l --license                Prints author info, citation and license.
-n --num-func[=int]         Number of orthogonal functions to generate. Positive integer. Default is 9.
-s --start-func[=int]       Starting function index. Non-negative integer. Default is 1.
-e --end-interval[=float]   End of the interval of functions domains. Real number greater than zero. Default is 1.
-c --check                  Checks orthogonality of generated functions.
-p --plot                   Plots generated functions, also saves the plot as pdf and svg file in the current directory.
            """

    ExampleString = \
            """
Description:

This script generates a set of orthonormal functions, called phi_perp, based on the set of non-orthonormal functions

    phi_i(t) = t**(1/(i+i)),      i = I, ... , I+N

The orthonormalized functions phi_perp_i are linear combination of the functions phi_i, as

    phi_perp_i(t) = alpha_i * sum_{j=I}^{I+N} a_{ij} phi_j(t)

The functions phi_perp are orthonormal in the interval [0,L] with respect to weight w(t) = 1/t. That is

    int_0^L phi_perp_i(t) phi_perp_j(t) 1/t dt = delta_{ij}

where delta_{ij} is the Kronecker delta function.

The script can be configured as follows:

   Variable     Variable in script              Option
   --------    --------------------    -------------------------
      I         "StartFunctionIndex"    "-s", or "--start-func"
      N         "NumFunctions"          "-n", or "--num-func"
      L         "EndInterval"           "-e", or "--end-interval" 

Outpt:

1. Prints the symbolic functions
2. Prints a human readable coefficients, "alpha" and "a" of the functions
3. Prints a matrix of mutual inner product of functions to check orthogonality (with option "-c")
4. Plots the set of functions (with option "-p")
5. Saves the plot as pdf and svg in the current directory (with option "-p")

Examples:

1. Generate nine orthogonal functions from function index 1 to 9
    $ %s

2. Generate seven orthogonal functions from function index 1 to 8
    $ %s -n 8

3. Generate nine orthogonal functions from function index 0 to 8
    $ %s -s 0

4. Generate nine set of orthogonal functions starting from function 1, that are orthonormal in the interval [0,10]
    $ %s -e 10

5. Check orthogonality of each two function, and plot the orthonormal functions and save the plot to pdf and svg
    $ %s -c -p

6. A complete example:
    $ %s -n 9 -s 1 -e 1 -c -p

            """%(ExecName,ExecName,ExecName,ExecName,ExecName,ExecName)

    print(UsageString)
    print(OptionsString)
    print(ExampleString)

# ===============
# Parse Arguments
# ===============

def ParseArguments(argv):
    """
    Parses the argument of the executable and obtains the filename.
    """

    # Initialize variables (defaults)
    Arguments = \
    {
        'CheckOrthogonality': False,
        'PlotFlag': False,
    }

    try:
        opts,args = getopt.getopt(argv[1:],"hvln:s:e:cp",["help","version","license","num-func=","start-func=","end-interval=","check","plot"])
    except getopt.GetoptError:
        print('Invalid option entered.')
        PrintUsage(argv[0])
        sys.exit(2)

    # Assign options
    for opt,arg in opts:
        
        if opt in ('-h','--help'):
            PrintUsage(argv[0])
            sys.exit()
        elif opt in ('-v','--version'):
            PrintVersion()
            sys.exit()
        elif opt in ("-l","--license"):
            PrintLicense()
            sys.exit()
        elif opt in ("-n","--num-func"):
            Arguments['NumFunctions'] = int(arg)
        elif opt in ("-s","--start-func"):
            Arguments['StartFunctionIndex'] = int(arg)
        elif opt in ("-e","--end-interval"):
            Arguments['EndInterval'] = float(arg)
        elif opt in ("-c",'--check'):
            Arguments['CheckOrthogonality'] = True
        elif opt in ("-p","--plot"):
            Arguments['PlotFlag'] = True

    return Arguments
