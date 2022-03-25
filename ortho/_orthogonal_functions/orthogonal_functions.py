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
from .plot_utilities import plot_functions


# ====================
# Orthogonal Functions
# ====================

class OrthogonalFunctions(object):
    """
    The main class of the package, which wraps the functions.
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

        Keyword arguments
            * ``num_func``
            * ``start_index``
            * ``end_interval``

        :param **kwargs: Variable keyword arguments.
        :type: ``**kwargs``
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
        """

        if self._phi_orthonormalized_list is None:
            raise RuntimeError('Call Process() first.')

        print_coeffs_of_functions(
                self.sym_coeffs,
                self.start_index)

    # ----
    # Plot
    # ----

    def plot(self):
        """
        Plot the generated functions.
        """

        if self._phi_orthonormalized_list is None:
            raise RuntimeError('Call Process() first.')

        # Plot Functions
        plot_functions(
                self._phi_orthonormalized_list,
                self.start_index,
                self._interval)
