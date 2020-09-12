#! /usr/bin/env python

"""
# Package Prerequisits:
    Install the followings python packages: numpy, sympy, matplotlib. If using anaconda or miniconda python
    distirbutor in linux, you may install them via
    $ sudo conda install -c conda-forge numpy sympy matplotlib -y
"""

# =======
# Imports
# =======

import sys
import getopt
import sympy
import numpy
import matplotlib
import matplotlib.pyplot as plt

# ==========================
# Declare symbolic variables
# ==========================

n = sympy.symbols('n',integer=True,positive=True)
t = sympy.symbols('t',real=True,positive=True)

# ===============
# Parse Arguments
# ===============

def ParseArguments(argv):
    """
    Parses the argument of the executable and obtains the filename.
    """

    # -------------
    # Print Version
    # -------------

    def PrintVersion():

        VersionString = \
                """
Version 0.0.1
                """

        print(VersionString)

    # -------------
    # Print License
    # -------------

    def PrintLicense():

        LicenseString = \
                """
Author: 
    Siavash Ameli
    University of California, Berkeley
    April 27, 2020

Citation:
    Ameli, S. and Shadden. S. C., "Maximum Likelihood Estimation of Variance and Nugget in General Linear Model"

License:
    GNU General Public License v3.0
                """

        print(LicenseString)

    # -----------
    # Print Usage
    # -----------

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

    # -----------------

    # Initialize variables (defaults)
    NumFunctions = 9
    StartFunctionIndex = 1
    EndInterval = 1
    CheckOrthogonality = False
    PlotFlag = False

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
            NumFunctions = int(arg)
        elif opt in ("-s","--start-func"):
            StartFunctionIndex = int(arg)
        elif opt in ("-ae","--end-interval"):
            EndInterval = float(arg)
        elif opt in ("-c",'--check'):
            CheckOrthogonality = True
        elif opt in ("-p","--plot"):
            PlotFlag = True

    # Check arguments
    if NumFunctions < 1:
        print('The option "NumFunctions" should be at least 1. Set with "-n" or "--num-func" option.')
        exit(1)
    if StartFunctionIndex < 0:
        print('"StartFunctionIndex" should be at least 1. Set with "-s" or "--start-funct" option.')
        exit(1)
    if EndInterval <= 0.0:
        print('"EndInterval" should be greater than zero. Set with "-e" or "--end-interval" option.')
        exit(1)

    return NumFunctions,StartFunctionIndex,EndInterval,CheckOrthogonality,PlotFlag

# ===
# phi
# ===

def phi(i):
    """
    Generates a list of non-orthogonal functions defined by t**{1/n}
    """
    return t**(sympy.Rational(sympy.S(1),sympy.S(i+1)))

# =============
# Inner Product
# =============

def InnerProduct(f,g):
    """
    Inner product of two functions with weight 1/t
    """
    # The two stage sympy.expand below is needed so sympy.integrate can perform properly
    h = sympy.expand(sympy.expand(f*g)/t)

    # Integrate function f between 0 and 1
    return sympy.integrate(h,(t,sympy.S(0),sympy.S(EndInterval)))

# =========
# Normalize
# =========

def Normalize(f):
    """
    Normalize a function with respect to inner product
    """
    return f/sympy.sqrt(InnerProduct(f,f))

# ====================
# Gram-Schmidt Process
# ====================

def GramSchmidtProcess(NumFunctions,StartFunctionIndex):
    """
    Generates a list of orthonormalized symbolic functions
    """

    print('---------------------')
    print('Orthogonal Functions:')
    print('---------------------')
    print('')

    # Create an empty list of orthnormalized functions
    phi_orthonormalized_list = []

    # Gram-Schmidt orthogonalization process
    for i in range(NumFunctions):

        # Initialize Gram-Schmidt process
        phi_non_orthogonal = phi(i+sympy.S(StartFunctionIndex))
        phi_orthogonalized = phi_non_orthogonal
        if i > 0:

            # Subtract a new function from each of previous orthonormalized functions
            for j in range(i):

                # Subtract new non-orthogomal function from the projection of the previous orthonormalized function
                phi_orthogonalized -= InnerProduct(phi_non_orthogonal,phi_orthonormalized_list[j])*phi_orthonormalized_list[j]

        # Normalize an orthogonalized funcction
        phi_orthogonalized = sympy.simplify(phi_orthogonalized)
        phi_orthonormalized = Normalize(phi_orthogonalized)
        phi_orthonormalized = sympy.simplify(phi_orthonormalized)

        # Store result to the list
        phi_orthonormalized_list.append(phi_orthonormalized)

        # Print progress
        print('phi_%d(t) = '%(i+StartFunctionIndex))
        print(phi_orthonormalized_list[i])
        print('')

    return phi_orthonormalized_list

# ===========================
# Check Mutual Orthonormality
# ===========================

def CheckMutualOrthonormality(phi_orthonormalized_list):
    """
    Checks the inner orthonormality of each of two fuctions froma list of symbolic functions.
    It returns an array with elements -1,0,1.
        -1: two functions are not orthogonal
         0: two functions are orthogonal
        +1: function is orthonormal
    """

    # Initialize output
    NumFunctions = len(phi_orthonormalized_list)
    MutualInnerProducts = -1 * numpy.ones((NumFunctions,NumFunctions),dtype=int)

    # Mutual inner products
    for i in range(NumFunctions):
        for j in range(i+1):

            # Inner product as symbolic number
            InnerProd = InnerProduct(phi_orthonormalized_list[i],phi_orthonormalized_list[j])

            # Convert symbolic number to -1,0,1 numpy integer
            if InnerProd == sympy.S(1):
                MutualInnerProducts[i,j] = 1
            elif InnerProd == sympy.S(0):
                MutualInnerProducts[i,j] = 0

            # Symmetric matrix
            if i != j:
                MutualInnerProducts[j,i] = MutualInnerProducts[i,j]

    # Print results
    print('----------------------------------')
    print('Mutual inner product of functions:')
    print('----------------------------------')
    print('')
    print(MutualInnerProducts)
    print('')

# ===============================
# Print Coefficients of Functions
# ===============================

def PrintCoefficientsOfFunctions(phi_orthonormalized_list,StartFunctionIndex):
    """
    Prints the coefficients of orthonormalized functions as

        phi_j = alpha_j * \sum_{i=1}^n a_{ij} t^{1/i}

    where alpha_j = sqrt{2/j}, and a_{ij} are integers
    """

    print('-------------------------')
    print('Coefficient of functions:')
    print('-------------------------')
    print('')
    print('i       alpha_[i]   a_[ij]')
    print('------  ----------  ---------')

    NumFunctions = len(phi_orthonormalized_list)
    for j in range(NumFunctions):

        # Multiply each function with sqrt(2/i+1) to have integer coefficients
        Alpha = (sympy.S(-1)**(sympy.S(j))) * sympy.sqrt(sympy.Rational(2,j+StartFunctionIndex+1))
        Function = phi_orthonormalized_list[j] / Alpha
        Function = sympy.simplify(Function)

        # Convert the function to a polynomial
        Polynomial = sympy.Poly(Function)

        # Get the coefficient of each monomial
        Coefficients = []
        for i in range(j+1):
            Coefficient = Polynomial.coeff_monomial(t**(sympy.Rational(1,i+1+StartFunctionIndex)))
            Coefficients.append(Coefficient)

        # Print human friendly
        Sign = (-1)**(j)
        SignAsString = '-'
        if Sign > 0: SignAsString = '+'
        AlphaAsString = SignAsString + 'sqrt(2/%d)'%(j+StartFunctionIndex+1)
        print('i = %d:  %s  %s'%(j+StartFunctionIndex,AlphaAsString,Coefficients))

    print('')

# ==============
# Plot Functions
# ==============

def PlotFunctions(phi_orthonormalized_list,StartFunctionIndex):

    # Color palette
    import seaborn as sns
    # sns.set()

    # Axes font size
    sns.set(font_scale=1.2)

    # LaTeX
    plt.rc('text',usetex=True)
    matplotlib.font_manager._rebuild()

    # Style sheet
    sns.set_style("white")
    sns.set_style("ticks")

    # Font (Note: this should be AFTER the plt.style.use)
    plt.rc('font', family='serif')
    plt.rcParams['svg.fonttype'] = 'none'  # text in svg file will be text not path.

    # Axis
    t_array = numpy.logspace(-7,numpy.log10(EndInterval),1000)

    # Evaluate functions
    NumFunctions = len(phi_orthonormalized_list)

    f = numpy.zeros((NumFunctions,t_array.size),dtype=float)
    for j in range(NumFunctions):
        f_lambdify = sympy.lambdify(t,phi_orthonormalized_list[j],'numpy')
        f[j,:] = f_lambdify(t_array)

    # Plot
    fig,ax = plt.subplots(figsize=(7,4.8))
    for j in range(NumFunctions):
        ax.semilogx(t_array,f[j,:],label=r'$i = %d$'%(j+StartFunctionIndex))

    ax.legend(ncol=3,loc='lower left',borderpad=0.5,frameon=False)
    ax.set_xlim([t_array[0],t_array[-1]])
    ax.set_ylim([-1,1])
    ax.set_yticks([-1,0,1])
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$\phi_i^{\perp}(t)$')
    ax.set_title('Orthogonal functions')
    ax.grid(axis='y')

    SaveDir = './doc/images/'
    SaveFullname_SVG = SaveDir + 'OrthogonalFunctions.svg'
    SaveFullname_PDF = SaveDir + 'OrthogonalFunctions.pdf'
    plt.savefig(SaveFullname_SVG,transparent=True,bbox_inches='tight')
    plt.savefig(SaveFullname_PDF,transparent=True,bbox_inches='tight')
    print('')
    print('Plot saved to "%s".'%(SaveFullname_SVG))
    print('Plot saved to "%s".'%(SaveFullname_PDF))
    plt.show()

# ====
# Main
# ====

def main(argv):

    # Interval of defining functions [0,EndInterval]
    global EndInterval

    # Parse arguments
    NumFunctions,StartFunctionIndex,EndInterval,CheckOrthogonality,PlotFlag = ParseArguments(argv)

    # Generate alist of symbolic orthonormal functions
    phi_orthonormalized_list = GramSchmidtProcess(NumFunctions,StartFunctionIndex)

    # Print Coefficients of Functions
    PrintCoefficientsOfFunctions(phi_orthonormalized_list,StartFunctionIndex)

    # Check orthonormality of functions
    if CheckOrthogonality:
        CheckMutualOrthonormality(phi_orthonormalized_list)

    # Plot Functions
    if PlotFlag:
        PlotFunctions(phi_orthonormalized_list,StartFunctionIndex)

# ===========
# System Main
# ===========

if __name__ == "__main__":
    main(sys.argv)
