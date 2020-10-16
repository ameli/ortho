#! /usr/bin/env python

# =======
# Imports
# =======

from OrthogonalFunctions import ParseArguments

# ====================
# Test Parse Arguments
# ====================

def test_ParseArguments():

    # Fake user argument
    Argv = ['./GenerateOrthogonalFunctions.py', '-n', '8', '-s', '1', '-e', '1', '-c', '-p']

    # Parse arguments
    Arguments = ParseArguments(Argv)

    print(Arguments)

# ===========
# System Main
# ===========

if __name__ == "__main__":
    test_ParseArguments()
