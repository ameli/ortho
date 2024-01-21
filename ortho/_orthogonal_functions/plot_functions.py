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

import numpy
import sympy
import os
from .plot_utilities import plt, matplotlib, get_custom_theme, save_plot
from .declarations import t

__all__ = ['plot_functions']


# ==============
# Plot Functions
# ==============

@matplotlib.rc_context(get_custom_theme(font_scale=1.2))
def plot_functions(phi_orthonormalized_list, start_index, interval):
    """
    Plots the generated functions, also saves the plots as both ``svg`` and
    ``pdf`` format.

    :param phi_orthonormalized_list: The list of generated functions. Each
        entry is a ``sympy`` object.
    :param: list

    :param start_index: The indet of the first function.
    :type start_index: int

    :param Interval: The right side of the interval of the domain of the
        functions.
    :param Interval: float
    """

    # Axis
    t_array = numpy.logspace(-7, numpy.log10(interval[1]), 1000)

    # Evaluate functions
    num_functions = len(phi_orthonormalized_list)

    f = numpy.zeros((num_functions, t_array.size), dtype=float)
    for j in range(num_functions):
        f_lambdify = sympy.lambdify(t, phi_orthonormalized_list[j], 'numpy')
        f[j, :] = f_lambdify(t_array)

    # Plot
    fig, ax = plt.subplots(figsize=(7, 4.8))
    for j in range(num_functions):
        ax.semilogx(t_array, f[j, :],
                    label=r'$i = %d$' % (j+start_index))

    ax.legend(ncol=3, loc='lower left', borderpad=0.5, frameon=False)
    ax.set_xlim([t_array[0], t_array[-1]])
    ax.set_ylim([-1, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$\phi_i^{\perp}(t)$')
    ax.set_title('Orthogonalized inverse-monomial functions')
    ax.grid(axis='y')

    # Get the root directory of the package (parent directory of this script)
    file_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(file_dir)
    second_parent_dir = os.path.dirname(parent_dir)

    # Try to save in the docs/images directory. Check if exists and writable
    save_dir = os.path.join(second_parent_dir, 'docs', 'images')
    if (not os.path.isdir(save_dir)) or (not os.access(save_dir, os.W_OK)):

        # Write in the current working directory
        save_dir = os.getcwd()

    # Save plot in both svg and pdf format
    if os.access(save_dir, os.W_OK):
        save_filename = 'orthogonal_functions'
        save_plot(plt, save_filename, save_dir=save_dir,
                  transparent_background=True)
    else:
        print('Cannot save plot to %s. Directory is not writable.' % save_dir)

    # If no display backend is enabled, do not plot in the interactive mode
    if matplotlib.get_backend() != 'agg':
        plt.show()
