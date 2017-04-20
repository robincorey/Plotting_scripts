#!/home/birac/anaconda2/bin/python
#
# python script to plot any Gromacsdata file
# 

### Version control

# original made Aug-2016
# Updated for \t Sept-210
# Updated Legends Sept-2016
# Improved legends Jan-2017. Now added prompt
# Improved CSV Feb-2017.
# Prettier graphs May-2017
# HOLE

import scipy as sc
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
import matplotlib.patches as mpatches

def loaddata ( str ):
        print "%s" % y
	return

filename = sys.argv[1]
leg = sys.argv[2]
xlabel = "time (ns)"
ylabel = "structure"
xdata, ydata = np.loadtxt(fname='%s' % filename, delimiter=',', usecols=(0,1), unpack=True)	

params = {'legend.fontsize': 'large',
	'axes.labelsize': 'x-large',
	'xtick.labelsize': 'x-large',
	'ytick.labelsize': 'x-large'}
plt.rcParams.update(params)
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['font.sans-serif'] = "cmss10"

#plt.plot(xdata, ydata, color='blue', marker='.', markersize=0)
smooth = sc.signal.savgol_filter(ydata, 11, 1, deriv=0, delta=1, axis=-1, mode='interp', cval=0.0)
plt.plot(xdata, smooth, color='red', marker='.', markersize=0)
plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
legend = mpatches.Patch(color='red', label='%s' % leg)
plt.legend(handles=[legend])
plt.savefig('%s.png' % filename, bbox_inches='tight')

