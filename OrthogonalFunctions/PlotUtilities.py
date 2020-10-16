# =======
# Imports
# =======

import sympy
import numpy
import matplotlib
import matplotlib.pyplot as plt
from .Declarations import n,t

# =============
# Plot Settings
# =============

def PlotSettings():
    """
    General settings for the plot.
    """

    # Color palette
    import seaborn as sns
    # sns.set()

    # Axes font size
    sns.set(font_scale=1.2)

    # LaTeX
    plt.rc('text',usetex=True)
    matplotlib.font_manager._rebuild()

    # Style sheet
    sns.set_style("white")
    sns.set_style("ticks")

    # Font (Note: this should be AFTER the plt.style.use)
    plt.rc('font', family='serif')
    plt.rcParams['svg.fonttype'] = 'none'  # text in svg file will be text not path.

# ==============
# Plot Functions
# ==============

def PlotFunctions(phi_orthonormalized_list,StartFunctionIndex,Interval):

    # Run plot settings
    PlotSettings()

    # Axis
    t_array = numpy.logspace(-7,numpy.log10(Interval[1]),1000)

    # Evaluate functions
    NumFunctions = len(phi_orthonormalized_list)

    f = numpy.zeros((NumFunctions,t_array.size),dtype=float)
    for j in range(NumFunctions):
        f_lambdify = sympy.lambdify(t,phi_orthonormalized_list[j],'numpy')
        f[j,:] = f_lambdify(t_array)

    # Plot
    fig,ax = plt.subplots(figsize=(7,4.8))
    for j in range(NumFunctions):
        ax.semilogx(t_array,f[j,:],label=r'$i = %d$'%(j+StartFunctionIndex))

    ax.legend(ncol=3,loc='lower left',borderpad=0.5,frameon=False)
    ax.set_xlim([t_array[0],t_array[-1]])
    ax.set_ylim([-1,1])
    ax.set_yticks([-1,0,1])
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$\phi_i^{\perp}(t)$')
    ax.set_title('Orthogonal functions')
    ax.grid(axis='y')

    SaveDir = './doc/images/'
    SaveFullname_SVG = SaveDir + 'OrthogonalFunctions.svg'
    SaveFullname_PDF = SaveDir + 'OrthogonalFunctions.pdf'
    plt.savefig(SaveFullname_SVG,transparent=True,bbox_inches='tight')
    plt.savefig(SaveFullname_PDF,transparent=True,bbox_inches='tight')
    print('')
    print('Plot saved to "%s".'%(SaveFullname_SVG))
    print('Plot saved to "%s".'%(SaveFullname_PDF))

    if matplotlib.get_backend() != 'agg':
        plt.show()
