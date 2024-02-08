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

from .orthogonalization_utilities import gram_schmidt_process
from .orthogonalization_utilities import print_coeffs_of_functions
from .orthogonalization_utilities import check_mutual_orthonormality
from .orthogonalization_utilities import get_symbolic_coeffs
from .orthogonalization_utilities import get_numeric_coeffs
from .plot_functions import plot_functions


# ====================
# Orthogonal Functions
# ====================

class OrthogonalFunctions(object):
    """
    Generates a set of orthonormal functions.

    Parameters
    ----------

        start_index : int, default=1
            The index of the starting function, :math:`i_0`.

        num_func : int, default=9
            Number of orthogonal functions to generate

        end_interval : float, default=1
            The right interval of orthogonality, :math:`L`.

        vebose : boolean, default=False
            Prints the generated functions. An example of output is

            ::

                phi_1(t) =  sqrt(x)
                phi_2(t) =  sqrt(6)*(5*x**(1/3) - 6*sqrt(x))/3
                phi_3(t) =  sqrt(2)*(21*x**(1/4) - 40*x**(1/3) + 20*sqrt(x))/2

    Attributes
    ----------

        sym_phi : sympy obj
            Orthogonal functions :math:`\\phi_i^{\\perp}`

        sym_alpha : sympy obj
            Coefficients :math:`\\alpha_i`

        sym_coeffs : sympy obj
            Coefficients :math:`a_{i,j}`

        alpha : list
            Coefficients :math:`\\alpha_i`

        coeffs : list of lists
            Coefficients :math:`a_{i,j}`

    Notes
    -----

    The orthogonal functions, :math:`\\phi_i^{\\perp}`, are generated based on
    the set of non-orthonormal functions :math:`\\phi_i` defined by the
    inverse-monomials

    .. math::

        \\phi_i(t) = t^{\\frac{1}{i+1}}, \\qquad i = i_0,\\dots,i_0+n.

    The orthonormalized functions :math:`\\phi_i^{\\perp}` are the linear
    combination of the functions :math:`\\phi_i` by

    .. math::

        \\phi_i^{\\perp}(t) = \\alpha_i \\sum_{j = i_0}^{i_0+n} a_{ij}
        \\phi_j(t), \\qquad i = i_0,\\dots,i_0+n.

    The functions :math:`\\phi_i^{\\perp}` are orthonormal in the interval
    :math:`t \\in [0,L]` with respect to the weight function
    :math:`w(t) = t^{-1}`. That is,

    .. math::

        \\langle \\phi_i^{\\perp},\\phi_j^{\\perp} \\rangle_{L^2([0,L],
        \\mathrm{d}t/t)} = \\int_0^L \\phi_i^{\\perp}(t) \\phi_j^{\\perp}(t)
        \\frac{\\mathrm{d}t}{t} = \\delta_{ij},

    where :math:`\\delta_{ij}` is the Kronecker delta function. The orthogonal
    functions are generated by `Gram-Schmidt orthogonalization process
    <https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process>`__.

    Methods
    -------
    check
    print
    plot
    """

    # ----
    # Init
    # ----

    def __init__(
            self,
            start_index=1,
            num_func=9,
            end_interval=1,
            verbose=False):
        """
        Parses the user inputs and sets the member data of the object.
        """

        # Number of functions
        self.num_func = num_func
        self.start_index = start_index
        self.end_interval = end_interval
        self.verbose = verbose

        # Check arguments
        if self.num_func < 1:
            print('The option "num_func" should be at least 1.')
            exit(1)
        if self.start_index < 0:
            print('"start_index" should be at least 1.')
            exit(1)
        if end_interval <= 0.0:
            print('"end_interval" should be greater than zero.')
            exit(1)

        # interval
        self._interval = [0, end_interval]

        # Generate list of functions
        self._phi_orthonormalized_list = self._process()
        self.sym_phi = self._phi_orthonormalized_list

        # Get coeffs of symbolic functions
        self.sym_alpha, self.sym_coeffs = get_symbolic_coeffs(
                self._phi_orthonormalized_list, self.start_index)

        # Get numeric values of coefficients
        self.alpha, self.coeffs = get_numeric_coeffs(
                self.sym_alpha, self.sym_coeffs)

    # -------
    # Process
    # -------

    def _process(self, verbose=False):
        """
        Computes the set of orthonormalized functions.
        """

        # Generate a list of symbolic orthonormal functions
        phi_orthonormalized_list = gram_schmidt_process(
                self.num_func,
                self.start_index,
                self._interval,
                verbose=verbose)

        return phi_orthonormalized_list

    # -----
    # Check
    # -----

    def check(self, verbose=False):
        """
        Check the mutual orthogonality of the functions.

        Parameters
        ----------

            verbose : boolean, default=False
                If `True`, prints the matrix of mutual inner product of
                functions. An example of the output is

                ::

                    [[1 0 0 0 0 0 0 0 0]
                     [0 1 0 0 0 0 0 0 0]
                     [0 0 1 0 0 0 0 0 0]
                     [0 0 0 1 0 0 0 0 0]
                     [0 0 0 0 1 0 0 0 0]
                     [0 0 0 0 0 1 0 0 0]
                     [0 0 0 0 0 0 1 0 0]
                     [0 0 0 0 0 0 0 1 0]
                     [0 0 0 0 0 0 0 0 1]]

        Returns
        -------

            status : boolean
                If `True`, the generated functions are all mutually
                orthonormal. Otherwise returns `False`.
        """

        if self._phi_orthonormalized_list is None:
            raise RuntimeError('Call Process() first.')

        # Check orthonormality of functions
        status = check_mutual_orthonormality(
                self._phi_orthonormalized_list,
                self._interval,
                verbose=verbose)

        return status

    # -----
    # Print
    # -----

    def print(self):
        """
        Print coeffs of Functions.

        An Example of output is

        ::

              i      alpha_i                                    a_[ij]
            ------  ----------   ---------------------------------------------
            i = 1:  +sqrt(2/2)   [1                                          ]
            i = 2:  -sqrt(2/3)   [6,   -5                                    ]
            i = 3:  +sqrt(2/4)   [20,  -40,    21                            ]
            i = 4:  -sqrt(2/5)   [50,  -175,   210,   -84                    ]
            i = 5:  +sqrt(2/6)   [105, -560,   1134,  -1008,   330           ]
            i = 6:  -sqrt(2/7)   [196, -1470,  4410,  -6468,   4620,   -1287 ]
        """

        if self._phi_orthonormalized_list is None:
            raise RuntimeError('Call Process() first.')

        print_coeffs_of_functions(
                self.sym_coeffs,
                self.start_index)

    # ----
    # Plot
    # ----

    def plot(self, filename=None):
        """
        Plot the generated functions.
        """

        if self._phi_orthonormalized_list is None:
            raise RuntimeError('Call Process() first.')

        # Plot Functions
        plot_functions(
                self._phi_orthonormalized_list,
                self.start_index,
                self._interval,
                filename=filename)