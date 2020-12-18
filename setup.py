#!/usr/bin/env python

# =======
# Imports
# =======

from __future__ import print_function
import os
import sys
import codecs

# Import setuptools
try:
    import setuptools
    from setuptools.extension import Extension
except ImportError:
    # Install setuptools
    try:
        import pip
        from pip import main
        pip.main(['install','setuptools'])
        import setuptools
        from setuptools.extension import Extension
    except:
        raise ImportError('Cannot import setuptools.')

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
    except ImportError:
        return ReadFile(Filename)

# ====
# Main
# ====

def main(argv):

    Directory = os.path.dirname(os.path.realpath(__file__))
    PackageName = "OrthogonalFunctions"
    PackageNameForDoc = "Orthogonal Functions"

    # Version
    version_dummy = {}
    exec(open(os.path.join(Directory,PackageName,'__version__.py'),'r').read(),version_dummy)
    Version = version_dummy['__version__']
    del version_dummy

    # Author
    Author = open(os.path.join(Directory,'AUTHORS.txt'),'r').read().rstrip()

    # Requirements
    Requirements = [i.strip() for i in open(os.path.join(Directory,"requirements.txt"),'r').readlines()]

    # ReadMe
    LongDescription = open(os.path.join(Directory,'README.rst'),'r').read()

    # Setup
    setuptools.setup(
        name = PackageName,
        version = Version,
        author = Author,
        author_email = 'sameli@berkeley.edu',
        description = 'Generate orthogonal set of functions',
        long_description = LongDescription,
        long_description_content_type = 'text/x-rst',
        keywords = 'orthogonal-functions regression sympy computer-algebra gram-schmidt',
        url = 'https://github.com/ameli/Orthogonal-Functions',
        download_url = 'https://github.com/ameli/Orthogonal-Functions/archive/main.zip',
        project_urls = {
            "Documentation": "https://github.com/ameli/Orthogonal-Functions/blob/main/README.rst",
            "Source": "https://github.com/ameli/Orthogonal-Functions",
            "Tracker": "https://github.com/ameli/Orthogonal-Functions/issues",
        },
        platforms = ['Linux','OSX','Windows'],
        packages = setuptools.find_packages(exclude=['tests.*','tests']),
        install_requires = Requirements,
        python_requires = '>=2.7',
        setup_requires = [
            'setuptools',
            'pytest-runner'],
        tests_require = [
            'pytest',
            'pytest-cov'],
        include_package_data=True,
        zip_safe=False,
        entry_points = {
            "console_scripts": [
                "gen-ortho = OrthogonalFunctions.__main__:main"
            ]
        },
        extras_require = {
            'dev': [
                'pytest-cov',
                'codecov'
            ],
            'docs': [
                'sphinx',
                'sphinx-math-dollar',
                'sphinx-toggleprompt',
            ]
        },
        classifiers = [
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
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
