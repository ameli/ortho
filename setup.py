#!/usr/bin/env python

# =======
# Imports
# =======

from __future__ import print_function
import os
import sys
import setuptools
import codecs

# =========
# Read File
# =========

def ReadFile(Filename):
    with codecs.open(Filename,'r','latin') as File:
        return File.read()

# ================
# Read File to RST
# ================

def ReadFileToRST(Filename):
    try:
        import pypandoc
        rstname = "{}.{}".format(os.path.splitext(Filename)[0],'rst')
        pypandoc.convert(read(Filename),'rst', format='md', outputfile=rstname)
        with open(rstname, 'r') as f:
            rststr = f.read()
        return rststr
        #return read(rstname)
    except ImportError:
        return ReadFile(Filename)

# ====
# Main
# ====

def main(argv):

    Directory = os.path.dirname(__file__)
    PackageName = "OrthogonalFunctions"

    # Version
    version_dummy = {}
    exec(open(os.path.join(Directory,PackageName,'__version__.py')).read(),version_dummy)
    Version = version_dummy['__version__']
    del version_dummy

    # Author
    Author = open(os.path.join(Directory,'AUTHORS.txt')).read().rstrip()

    # Requirements
    Requirements = [i.strip() for i in open(os.path.join(Directory,"requirements.txt")).readlines()]

    # ReadMe
    LongDescription = ReadFileToRST('README.rst')

    # Setup
    setuptools.setup(
        name = PackageName,
        version = Version,
        author = Author,
        author_email = 'sameli@berkeley.edu',
        description = 'Generate orthogonal set of functions',
        long_description = LongDescription,
        long_description_content_type = 'text/markdown',
        keywords = 'orthogonal-functions regression sympy computer-algebra gram-schmidt',
        url = 'https://github.com/ameli/Orthogonal-Functions/archive/v0.0.1.tar.gz',
        download_url = 'https://github.com/ameli/Orthogonal-Functions',
        project_urls = {
            "Documentation": "https://github.com/ameli/Orthogonal-Functions/blob/master/README.rst",
            "Source": "https://github.com/ameli/Orthogonal-Functions",
            "Tracker": "https://github.com/ameli/Orthogonal-Functions/issues",
        },
        platforms = ['Linux','OSX','Windows'],
        packages = setuptools.find_packages(exclude=("tests",)),
        install_requires = Requirements,
        python_requires = '>=2.7',
        setup_requires = ['pytest-runner'],
        tests_require = ['pytest'],
        include_package_data=True,
        entry_points = {
            "console_scripts": [
                "genorth = GenerateOrthogonalFunctions.__main__:main"
            ]
        },
        classifiers = [
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Natural Language :: English',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )

# ===========
# System Main
# ===========

if __name__ == "__main__":
    main(sys.argv)
