# Title:   Function to configure plot style
import matplotlib.pyplot as plt
from distutils.spawn import find_executable

DPI = 800
FONTSIZE = 8
LABELSIZE = 10
PAD_INCHES = 0.02
GRID_LINEWIDTH = 0.5
FIGSIZE = (3, 2.5)
TICK_MAJOR_WIDTH = .5
TICK_MAJOR_SIZE = 3
TICK_MINOR_WIDTH = .25
TICK_MINOR_SIZE = 1.5
LEGEND_FONTSIZE = 6


def config_plots() -> None:
    """
    This function configurates the default Matpltlib variables.
    """
    params = {'figure.dpi': DPI,
              'figure.figsize': FIGSIZE,
              'font.size': FONTSIZE,
              'font.family': 'serif',
              'axes.labelsize': LABELSIZE,
              'xtick.top': 'on',
              'xtick.minor.bottom': 'on',
              'xtick.minor.top': 'on',
              'xtick.direction': 'in',
              'ytick.right': 'on',
              'ytick.minor.left': 'on',
              'ytick.minor.right': 'on',
              'ytick.direction': 'in',
              'xtick.major.width': TICK_MAJOR_WIDTH,
              'xtick.major.size': TICK_MAJOR_SIZE,
              'xtick.minor.width': TICK_MINOR_WIDTH,
              'xtick.minor.size': TICK_MINOR_SIZE,
              'ytick.major.width': TICK_MAJOR_WIDTH,
              'ytick.major.size': TICK_MAJOR_SIZE,
              'ytick.minor.width': TICK_MINOR_WIDTH,
              'ytick.minor.size': TICK_MINOR_SIZE,
              'savefig.dpi': DPI,
              'savefig.bbox': 'tight',
              'savefig.pad_inches': PAD_INCHES,
              'axes.axisbelow': True,
              'axes.grid': True,
              'grid.linestyle': '--',
              'grid.linewidth': GRID_LINEWIDTH,
              'legend.fontsize': LEGEND_FONTSIZE,
              'legend.framealpha': 0}
    if find_executable('latex'):  # Use LaTeX
        params['text.usetex'] = True
    plt.rcParams.update(params)
