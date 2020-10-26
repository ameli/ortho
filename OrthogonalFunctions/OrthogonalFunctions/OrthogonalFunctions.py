# =======
# Imports
# =======

from .OrthogonalizationUtilities import GramSchmidtProcess
from .OrthogonalizationUtilities import PrintCoefficientsOfFunctions
from .OrthogonalizationUtilities import CheckMutualOrthonormality
from .PlotUtilities import PlotFunctions

# ====================
# Orthogonal Functions
# ====================

class OrthogonalFunctions():
    """
    The main class of the package, which wraps the functions.
    """

    # ----
    # Init
    # ----

    def __init__(self,**kwargs):
        """
        Parses the user inputs and sets the member data of the object.

        Keyword arguments
            * ``NumFunctions``
            * ``StartFunctionIndex``
            * ``EndInterval``

        :param **kwargs: Variable keyword arguments.
        :type: ``**kwargs``
        """

        # Default settings
        Defaults = \
        {
            'NumFunctions': 9,
            'StartFunctionIndex': 1,
            'EndInterval': 1
        }

        # Number of functions
        if 'NumFunctions' in kwargs:
            self.NumFunctions = kwargs['NumFunctions']
        else:
            self.NumFunctions = Defaults['NumFunctions']

        # Start function index
        if 'StartFunctionIndex' in kwargs:
            self.StartFunctionIndex = kwargs['StartFunctionIndex']
        else:
            self.StartFunctionIndex = Defaults['StartFunctionIndex']

        # End interval
        if 'EndIntrval' in kwargs:
            EndInterval = kwargs['EndInterval']
        else:
            EndInterval = Defaults['EndInterval']

        # Check arguments
        if self.NumFunctions < 1:
            print('The option "NumFunctions" should be at least 1.')
            exit(1)
        if self.StartFunctionIndex < 0:
            print('"StartFunctionIndex" should be at least 1.')
            exit(1)
        if EndInterval <= 0.0:
            print('"EndInterval" should be greater than zero.')
            exit(1)

        # Intrval
        self.Interval = [0,EndInterval]

        # Initialize output variable
        self.phi_orthonormalized_list = None

    # -------
    # Process
    # -------

    def Process(self):
        """
        Computes the set of orthonormalized functions.
        """

        # Generate alist of symbolic orthonormal functions
        self.phi_orthonormalized_list = GramSchmidtProcess(
                self.NumFunctions,
                self.StartFunctionIndex,
                self.Interval)

    # -----
    # Check
    # -----

    def Check(self):
        """
        Check the mutual orthogonality of the functions.
        """

        if self.phi_orthonormalized_list is None:
            raise RuntimeError('Call Process() first.')

        # Check orthonormality of functions
        CheckMutualOrthonormality(
                self.phi_orthonormalized_list,
                self.Interval)

    # -----
    # Print
    # -----

    def Print(self):
        """
        Print Coefficients of Functions.
        """

        if self.phi_orthonormalized_list is None:
            raise RuntimeError('Call Process() first.')

        PrintCoefficientsOfFunctions(
                self.phi_orthonormalized_list,
                self.StartFunctionIndex)

    # ----
    # Plot
    # ----

    def Plot(self):
        """
        Plot the generated functions.
        """

        if self.phi_orthonormalized_list is None:
            raise RuntimeError('Call Process() first.')

        # Plot Functions
        PlotFunctions(
                self.phi_orthonormalized_list,
                self.StartFunctionIndex,
                self.Interval)
