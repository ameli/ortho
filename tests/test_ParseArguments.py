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
    Argv1 = ['', '-n', '8', '-s', '1', '-e', '1', '-c', '-p']
    Argv2 = ['', '-h']
    Argv3 = ['', '-l']
    Argv4 = ['', '-v']

    # Parse arguments
    Test = True
    Arguments1 = ParseArguments(Argv1,Test)
    Arguments2 = ParseArguments(Argv2,Test)
    Arguments3 = ParseArguments(Argv3,Test)
    Arguments4 = ParseArguments(Argv4,Test)

    print(Arguments1)
    print(Arguments2)
    print(Arguments3)
    print(Arguments4)

# ===========
# System Main
# ===========

if __name__ == "__main__":
    test_ParseArguments()
