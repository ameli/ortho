#!/usr/bin/env python

# SPDX-FileCopyrightText: Copyright 2021, Siavash Ameli <sameli@berkeley.edu>
# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileType: SOURCE
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the license found in the LICENSE.txt file in the root
# directory of this source tree.

# =======
# Imports
# =======

from __future__ import print_function
import os
from os.path import join
import sys
import codecs
import subprocess


# ===============
# install package
# ===============

def install_package(package):
    """
    Installs packages using pip.

    Example:

    .. code-block:: python

        >>> install_package('numpy>1.11')

    :param package: Name of package with or without its version pin.
    :type package: string
    """

    subprocess.check_call([sys.executable, "-m", "pip", "install",
                           "--prefer-binary", package])


# =====================
# Import Setup Packages
# =====================

# Import setuptools
try:
    import setuptools
except ImportError:
    # Install setuptools
    install_package('setuptools')
    import setuptools


# =========
# read file
# =========

def read_file(Filename):
    with codecs.open(Filename, 'r', 'latin') as File:
        return File.read()


# ================
# read file to rst
# ================

def read_file_to_rst(Filename):
    try:
        import pypandoc
        rstname = "{}.{}".format(os.path.splitext(Filename)[0], 'rst')
        pypandoc.convert(read_file(Filename), 'rst', format='md',
                         outputfile=rstname)
        with open(rstname, 'r') as f:
            rststr = f.read()
        return rststr
    except ImportError:
        return read_file(Filename)


# ================
# get requirements
# ================

def get_requirements(directory, subdirectory=""):
    """
    Returns a list containing the package requirements given in a file named
    "requirements.txt" in a subdirectory.
    """

    requirements_filename = join(directory, subdirectory, "requirements.txt")
    requirements_file = open(requirements_filename, 'r')
    requirements = [i.strip() for i in requirements_file.readlines()]

    return requirements


# ====
# main
# ====

def main(argv):

    directory = os.path.dirname(os.path.realpath(__file__))
    package_name = "ortho"

    # Version
    version_dummy = {}
    version_file = join(directory, package_name, '__version__.py')
    exec(open(version_file, 'r').read(), version_dummy)
    version = version_dummy['__version__']
    del version_dummy

    # author
    author = open(os.path.join(directory, 'AUTHORS.txt'), 'r').read().rstrip()

    # Requirements
    requirements = get_requirements(directory)
    test_requirements = get_requirements(directory, subdirectory="tests")
    docs_requirements = get_requirements(directory, subdirectory="docs")

    # ReadMe
    long_description = open(os.path.join(directory, 'README.rst'), 'r').read()

    url = 'https://github.com/ameli/ortho'
    download_url = url + '/archive/main.zip'
    documentation_url = url + '/blob/main/README.rst'
    tracker_url = url + '/issues'

    # Setup
    setuptools.setup(
        name=package_name,
        version=version,
        author=author,
        author_email='sameli@berkeley.edu',
        description='Generate orthogonal set of functions',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        keywords='orthogonal-functions regression sympy computer-algebra' +
                 'gram-schmidt',
        url=url,
        download_url=download_url,
        project_urls={
            "Documentation": documentation_url,
            "Source": url,
            "Tracker": tracker_url,
        },
        platforms=['Linux', 'OSX', 'Windows'],
        packages=setuptools.find_packages(exclude=[
            'tests.*',
            'tests',
            'examples.*',
            'examples']
        ),
        install_requires=requirements,
        python_requires='>=3.9',
        setup_requires=[
            'setuptools',
            'pytest-runner'],
        tests_require=[
            'pytest',
            'pytest-cov'],
        include_package_data=True,
        zip_safe=False,
        entry_points={
            "console_scripts": [
                "ortho=ortho.__main__:main"
            ]
        },
        extras_require={
            'test': test_requirements,
            'docs': docs_requirements,
        },
        classifiers=[
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Natural Language :: English',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )


# ===========
# script main
# ===========

if __name__ == "__main__":
    main(sys.argv)
