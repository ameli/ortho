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
import sympy
import numpy
import shutil
import matplotlib
import matplotlib.pyplot as plt
from .declarations import t


# =============
# Plot Settings
# =============

def plot_settings():
    """
    General settings for the plot.
    """

    # Color palette
    import seaborn as sns
    # sns.set()

    # Axes font size
    sns.set(font_scale=1.2)

    # LaTeX
    if shutil.which('latex'):
        plt.rc('text', usetex=True)

    # Style sheet
    sns.set_style("white")
    sns.set_style("ticks")

    # Font (Note: this should be AFTER the plt.style.use)
    plt.rc('font', family='serif')
    plt.rcParams['svg.fonttype'] = 'none'  # text in svg file is text not path.


# ==============
# Plot Functions
# ==============

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

    # Run plot settings
    plot_settings()

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
        save_fullename_svg = os.path.join(save_dir, 'orthogonal_functions.svg')
        save_fullename_pdf = os.path.join(save_dir, 'orthogonal_functions.pdf')
        plt.savefig(save_fullename_svg, transparent=True, bbox_inches='tight')
        plt.savefig(save_fullename_pdf, transparent=True, bbox_inches='tight')
        print('')
        print('Plot saved to "%s".' % (save_fullename_svg))
        print('Plot saved to "%s".' % (save_fullename_pdf))
    else:
        print('Cannot save plot to %s. Directory is not writable.' % save_dir)

    # If no display backend is enabled, do not plot in the interactive mode
    if matplotlib.get_backend() != 'agg':
        plt.show()
