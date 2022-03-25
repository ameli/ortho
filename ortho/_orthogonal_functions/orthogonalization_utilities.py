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

import sympy
import numpy
from .declarations import t


# ===
# phi
# ===

def phi(i):
    """
    Generates a list of non-orthogonal functions defined by
    :math:`t^{\\frac{1}{n}}`.

    :param i: The index of a basis function.
    :type i: int

    :return: A ``sympy`` object of the ``i``-th basis function.
    :rtype: sympy object
    """

    return t**(sympy.Rational(sympy.S(1), sympy.S(i+1)))


# =============
# Inner Product
# =============

def inner_product(f, g, interval):
    """
    Inner product of two functions with weight :math:`t^{-1}`.

    :param f: A ``sympy`` function.
    :type f: sympy object

    :param g: A ``sympy`` function.
    :type g: sympy object

    :param interval: The interval of the domain of the functions in the form
    ``[Start, end]``.
    :type interval: list

    :return: The inner product of the functions.
    :rtype: float
    """

    # The two stage sympy.expand below is needed so sympy.integrate can perform
    # properly
    h = sympy.expand(sympy.expand(f*g)/t)

    # Integrate function f between 0 and 1
    return sympy.integrate(h, (t, sympy.S(interval[0]), sympy.S(interval[1])))


# =========
# Normalize
# =========

def normalize(f, interval):
    """
    Normalize a function with respect to inner product.

    :param f: A sympy function.
    :type f: sympy object

    :param interval: The interval of the domain of the functions in the form
    ``[Start, end]``.
    :type interval: list

    :return: The normalized sympy function
    :rtype: sympy object
    """

    return f/sympy.sqrt(inner_product(f, f, interval))


# ====================
# Gram-Schmidt Process
# ====================

def gram_schmidt_process(
        num_func,
        start_index,
        interval,
        verbose=False):
    """
    Generates a list of orthonormalized symbolic functions.

    :param num_func: Number of functions to generate.
    :type num_func: int

    :param start_index: The start index of the functions.
    :type start_index: int

    :param interval: The interval of the domain of the functions in the form
        ``[Start, End]``.
    :type interval: list

    :return: list of sympy functions.
    :rtype: list
    """

    if verbose:
        print('---------------------')
        print('Orthogonal functions:')
        print('---------------------')
        print('')

    # Create an empty list of orthnormalized functions
    phi_orthonormalized_list = []

    # Gram-Schmidt orthogonalization process
    for i in range(num_func):

        # Initialize Gram-Schmidt process
        phi_non_orthogonal = phi(i+sympy.S(start_index))
        phi_orthogonalized = phi_non_orthogonal
        if i > 0:

            # Subtract a new function from each of previous orthonormalized
            # functions
            for j in range(i):

                # Subtract new non-orthogomal function from the projection of
                # the previous orthonormalized function
                phi_orthogonalized -= inner_product(
                        phi_non_orthogonal, phi_orthonormalized_list[j],
                        interval) * phi_orthonormalized_list[j]

        # Normalize an orthogonalized function
        phi_orthogonalized = sympy.simplify(phi_orthogonalized)
        phi_orthonormalized = normalize(phi_orthogonalized, interval)
        phi_orthonormalized = sympy.simplify(phi_orthonormalized)

        # Store result to the list
        phi_orthonormalized_list.append(phi_orthonormalized)

        # Print progress
        if verbose:
            print('phi_%d(t) = ' % (i+start_index))
            print(phi_orthonormalized_list[i])
            print('')

    return phi_orthonormalized_list


# ===========================
# Check Mutual Orthonormality
# ===========================

def check_mutual_orthonormality(
        phi_orthonormalized_list,
        interval,
        verbose=False):
    """
    Checks the inner orthonormality of each of two functions from a list of
    symbolic functions.

    It returns an array with elements ``-1``, ``0``, or ``1``.

        * ``-1``: two functions are not orthogonal.
        *  ``0``: two functions are orthogonal.
        * ``+1``: function is orthonormal.

    :param phi_orthonormalized_list: The list of sympy functions that are
        orthonormalized.
    :type phi_orthonormalized_list: list

    :param interval: The interval of the domain of the functions in the form
        ``[Start, End]``.
    :type interval: list

    :return: The mutual orthogonality matrix.
    :rtype: ndarray
    """

    # Initialize output
    num_func = len(phi_orthonormalized_list)
    mutual_inner_products = -1 * numpy.ones((num_func, num_func),
                                            dtype=int)

    # Mutual inner products
    for i in range(num_func):
        for j in range(i+1):

            # Inner product as symbolic number
            inner_prod = inner_product(phi_orthonormalized_list[i],
                                       phi_orthonormalized_list[j], interval)

            # Convert symbolic number to -1, 0, 1 numpy integer
            if inner_prod == sympy.S(1):
                mutual_inner_products[i, j] = 1
            elif inner_prod == sympy.S(0):
                mutual_inner_products[i, j] = 0

            # Symmetric matrix
            if i != j:
                mutual_inner_products[j, i] = mutual_inner_products[i, j]

    # Print results
    if verbose:
        print('----------------------------------')
        print('Mutual inner product of functions:')
        print('----------------------------------')
        print('')
        print(mutual_inner_products)
        print('')

    status = numpy.allclose(numpy.eye(num_func), mutual_inner_products)
    return status


# ===================
# get symbolic coeffs
# ===================

def get_symbolic_coeffs(
        phi_orthonormalized_list,
        start_index):
    """
    Gets symbolic coefficients of alpha[i] and a[ij].
    """

    num_func = len(phi_orthonormalized_list)
    sym_alpha = [None] * num_func
    sym_coeffs = [None] * num_func

    for j in range(num_func):

        # Multiply each function with sqrt(2/i+1) to have integer coeffs
        sym_alpha[j] = (sympy.S(-1)**(sympy.S(j))) * \
                 sympy.sqrt(sympy.Rational(2, j+start_index+1))
        function = phi_orthonormalized_list[j] / sym_alpha[j]
        function = sympy.simplify(function)

        # Convert the function to a polynomial
        polynomial = sympy.Poly(function)

        sym_coeffs[j] = []
        # Get the coeff of each monomial
        for i in range(j+1):
            coeff = polynomial.coeff_monomial(
                    t**(sympy.Rational(1, i+1+start_index)))
            sym_coeffs[j].append(coeff)

    return sym_alpha, sym_coeffs


# ==================
# Get numeric coeffs
# ==================

def get_numeric_coeffs(
        sym_alpha,
        sym_coeffs):
    """
    Evaluate symbolic coefficients to numerics.
    """

    num_func = len(sym_coeffs)
    alpha = []
    coeffs = [None] * num_func

    for j in range(num_func):
        alpha.append(float(sym_alpha[j]))

        coeffs[j] = []
        for i in range(len(sym_coeffs[j])):
            coeffs[j].append(int(sym_coeffs[j][i]))

    return alpha, coeffs


# =========================
# Print coeffs of functions
# =========================

def print_coeffs_of_functions(
        coeffs,
        start_index):
    """
    Prints the coeffs of orthonormalized functions as

    .. math::

        \\phi_j(t) = \\alpha_j * \\sum_{i=1}^n a_{ij} t^{\\frac{1}{i}}

    where :math:`\\alpha_j = \\sqrt{\\frac{2}{j}}`, and :math:`a_{ij}` are
    integers.

    :param phi_orthonormalized_list: The list of sympy functions that are
        orthonormalized.
    :type phi_orthonormalized_list: list

    :param start_index: The start index of the functions.
    :type start_index: int
    """

    print('-------------------------')
    print('coeff of functions:')
    print('-------------------------')
    print('')
    print('i       alpha_[i]     a_[ij]')
    print('------  -----------   ---------')

    num_func = len(coeffs)
    for j in range(num_func):

        # Print human friendly
        sign = (-1)**(j)
        sign_as_string = '-'
        if sign > 0:
            sign_as_string = '+'
        alpha_as_string = sign_as_string + \
            'sqrt(2/%d)' % (j+start_index+1)
        print('i = %d:  %11s  %s'
              % (j+start_index, alpha_as_string, coeffs[j]))

    print('')
