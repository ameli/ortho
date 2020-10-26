# =======
# Imports
# =======

import sympy
import numpy
from .Declarations import n,t

# ===
# phi
# ===

def phi(i):
    """
    Generates a list of non-orthogonal functions defined by :math:`t^{\\frac{1}{n}}`.

    :param i: The index of a basis function.
    :type i: int

    :return: A ``sympy`` object of the ``i``-th basis function.
    :rtype: sympy object
    """

    return t**(sympy.Rational(sympy.S(1),sympy.S(i+1)))

# =============
# Inner Product
# =============

def InnerProduct(f,g,Interval):
    """
    Inner product of two functions with weight :math:`t^{-1}`.

    :param f: A ``sympy`` function.
    :type f: sympy object

    :param g: A ``sympy`` function.
    :type g: sympy object

    :param Interval: The interval of the domain of the functions in the form ``[Start,end]``.
    :type Interval: list

    :return: The inner product of the functions.
    :rtype: float
    """

    # The two stage sympy.expand below is needed so sympy.integrate can perform properly
    h = sympy.expand(sympy.expand(f*g)/t)

    # Integrate function f between 0 and 1
    return sympy.integrate(h,(t,sympy.S(Interval[0]),sympy.S(Interval[1])))

# =========
# Normalize
# =========

def Normalize(f,Interval):
    """
    Normalize a function with respect to inner product.

    :param f: A sympy function.
    :type f: sympy object

    :param Interval: The interval of the domain of the functions in the form ``[Start,end]``.
    :type Interval: list

    :return: The normalized sympy function
    :rtype: sympy object
    """

    return f/sympy.sqrt(InnerProduct(f,f,Interval))

# ====================
# Gram-Schmidt Process
# ====================

def GramSchmidtProcess(NumFunctions,StartFunctionIndex,Interval):
    """
    Generates a list of orthonormalized symbolic functions.

    :param NumFunctions: Number of functions to generate.
    :type NumFunctions: int

    :param StartFunctionIndex: The start index of the functions.
    :type StartFunctionIndex: int

    :param Interval: The interval of the domain of the functions in the form ``[Start,End]``.
    :type Interval: list

    :return: list of sympy functions.
    :rtype: list
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
                phi_orthogonalized -= InnerProduct(phi_non_orthogonal,phi_orthonormalized_list[j],Interval)*phi_orthonormalized_list[j]

        # Normalize an orthogonalized funcction
        phi_orthogonalized = sympy.simplify(phi_orthogonalized)
        phi_orthonormalized = Normalize(phi_orthogonalized,Interval)
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

def CheckMutualOrthonormality(phi_orthonormalized_list,Interval):
    """
    Checks the inner orthonormality of each of two fuctions froma list of symbolic functions.

    It returns an array with elements ``-1``, ``0``, or ``1``.

        * ``-1``: two functions are not orthogonal.
        *  ``0``: two functions are orthogonal.
        * ``+1``: function is orthonormal.

    :param phi_orthonormalized_list: The list of sympy functions that are orthonormalized.
    :type phi_orthonormalized_list: list

    :param Interval: The interval of the domain of the functions in the form ``[Start,End]``.
    :type Interval: list

    :return: The mutual orthogonality matrix.
    :rtype: ndarray
    """

    # Initialize output
    NumFunctions = len(phi_orthonormalized_list)
    MutualInnerProducts = -1 * numpy.ones((NumFunctions,NumFunctions),dtype=int)

    # Mutual inner products
    for i in range(NumFunctions):
        for j in range(i+1):

            # Inner product as symbolic number
            InnerProd = InnerProduct(phi_orthonormalized_list[i],phi_orthonormalized_list[j],Interval)

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

    .. math::

        \phi_j(t) = \\alpha_j * \sum_{i=1}^n a_{ij} t^{\\frac{1}{i}}

    where :math:`\\alpha_j = \sqrt{\\frac{2}{j}}`, and :math:`a_{ij}` are integers.

    :param phi_orthonormalized_list: The list of sympy functions that are orthonormalized.
    :type phi_orthonormalized_list: list

    :param StartFunctionIndex: The start index of the functions.
    :type StartFunctionIndex: int
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
