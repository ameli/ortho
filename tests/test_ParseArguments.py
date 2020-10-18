#! /usr/bin/env python

# =======
# Imports
# =======

from OrthogonalFunctions import ParseArguments

# ====================
# Test Parse Arguments
# ====================

def test_ParseArguments():

    # Mock user argument
    Argv1 = ['./GenerateOrthogonalFunctions.py', '-n', '8', '-s', '1', '-e', '1', '-c', '-p']
    Argv2 = ['./GenerateOrthogonalFunctions.py', '-h']
    Argv3 = ['./GenerateOrthogonalFunctions.py', '-l']
    Argv4 = ['./GenerateOrthogonalFunctions.py', '-v']

    # Parse arguments
    Arguments1 = ParseArguments(Argv1)
    Arguments2 = ParseArguments(Argv2)
    Arguments3 = ParseArguments(Argv3)
    Arguments4 = ParseArguments(Argv4)

    print(Arguments1)
    print(Arguments2)
    print(Arguments3)
    print(Arguments4)

# ===========
# System Main
# ===========

if __name__ == "__main__":
    test_ParseArguments()
