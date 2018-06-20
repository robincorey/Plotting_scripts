#!/sansom/s137/bioc1535/anaconda2/bin/python
#
# python script to plot any Gromacsdata file
# 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import curve_fit
from scipy import optimize
from scipy import signal
import os
import re
import sys
import csv
import shutil
import pandas as pd
import subprocess
import os.path
from scipy.interpolate import spline

def loaddata ( str ):
        print "%s" % y
	return
filename = 'HILLS'
file = open('%s' % filename, 'r')
xlabel = "time (ns)"
ylabel = "gaussian height (kj/mol)"
xdata, ydata = np.loadtxt(fname='%s' %filename, comments='#', usecols=(0,5), unpack=True)
params = {'legend.fontsize': 'large',
	'axes.labelsize': 'x-large',
	'xtick.labelsize': 'large',
	'ytick.labelsize': 'large'}
plt.rcParams.update(params)
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['font.sans-serif'] = "cmss10"
plt.plot((xdata / 1000000), ydata, 'b')
plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=15 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=15 )
plt.tight_layout()
plt.savefig('%s.png' % filename )
plt.show ()
