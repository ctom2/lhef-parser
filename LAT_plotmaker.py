from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter,AutoMinorLocator
import numpy as np

def set_plt():
    plt.rcParams['xtick.labelsize'] = 20
    plt.rcParams['ytick.labelsize'] = 20

    plt.rcParams['font.size'] = 20
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.figsize'] = 12, 5
    plt.rcParams['axes.titlesize'] = 20
    plt.rcParams['axes.labelsize'] = 20
    plt.rcParams['axes.labelpad'] = 1
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markersize'] = 6
    plt.rcParams['legend.fontsize'] = 13
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'

    plt.rcParams['xtick.major.size'] = 10
    plt.rcParams['xtick.minor.size'] = 5

    plt.rcParams['ytick.major.size'] = 10
    plt.rcParams['ytick.minor.size'] = 5

    fig, ax = plt.subplots()

    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.major.formatter._useMathText = True
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))

def PlotData(data, xlabel, bins, save, path, log=False):
    set_plt()  
    plt.hist(data, color='black', linewidth=1.8, histtype='step', align='mid', bins=np.arange(*bins))
    
    if log: plt.yscale('log')
    
    plt.xlabel(xlabel, horizontalalignment='right', x=1.0)
    plt.xticks(np.arange(bins[0], bins[1] + 1, bins[2]*10))
    plt.ylabel('Events')
    plt.title('p + p $\sqrt{s}$ = 13 GeV', horizontalalignment='right', x=1.0)

    if save: 
        plt.savefig(path, dpi=200, bbox_inches='tight')
    else: 
        plt.show()

def PlotDataDouble(data1, data2, particle, xlabel, bins, save, path, log=False, loc=False, legend=True):
    set_plt()
    plt.hist(
        data1, color='blue', linewidth=1.8, histtype='step', align='mid', 
        bins=np.arange(*bins), label = particle + ' 1'
    )
    plt.hist(
        data2, color='red', linewidth=1.8, histtype='step', align='mid', 
        bins=np.arange(*bins), label = particle + ' 2'
    )

    if log: plt.yscale('log')
        
    if legend: plt.legend()

    if loc: plt.legend(loc=8)

    plt.xlabel(xlabel, horizontalalignment='right', x=1.0)

    plt.xticks(np.arange(bins[0], bins[1] + bins[2], bins[2]*10))
    plt.ylabel('Events')
    plt.title('p + p $\sqrt{s}$ = 13 GeV', horizontalalignment='right', x=1.0)

    if save: 
        plt.savefig(path, dpi=200, bbox_inches='tight')
    else: 
        plt.show()