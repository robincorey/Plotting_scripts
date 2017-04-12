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

def loaddata ( str ):
        print "%s" % y
	return

filename = sys.argv[1]
file = open('%s' % filename, 'r')

ydata, xdata, zdata = np.loadtxt(fname='%s' %filename, delimiter=' ', skiprows=1, unpack=True)
#x, y, z = np.loadtxt(fname='%s' %filename, delimiter=' ', skiprows=1, unpack=True)

##########
# Plotting data
##########

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

plt.title('%s' % filename )
#N = int(len(z)**.5)
#z = z.reshape(N, N)
#plt.pcolormesh(x,y,z)
plt.xlim([0,56])
plt.ylim([-1,37])
s=120
plt.scatter(xdata, ydata, color='r', s=1, alpha=0.2)
#plt.imshow(z, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)))
#	cmap=cm.hot)   # norm=LogNorm())

#plt.plot(x,z)
#legendq = raw_input(prompt)
#if legendq is 'y':
#	plt.legend()
#plt.xlim(0, 50)
plt.savefig('%s.png' % filename )
plt.show ()
