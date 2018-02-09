#!/sansom/s137/bioc1535/anaconda2/bin/python
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
from scipy.interpolate import griddata

def loaddata ( str ):
        print "%s" % y
	return


##########
# Plotting data
##########

filename = sys.argv[1]
xlabel = "X (nm)"
ylabel = "Y (nm)"
f = open('data_%s' % filename,'w')
sed = subprocess.call(['sed', '/#/d', filename], stdout=f)
dat = np.genfromtxt('data_%s' % filename,skip_header=0)
X_dat = dat[:,0]
Y_dat = dat[:,1]
Z_dat = dat[:,2]

params = {'legend.fontsize': 'medium',
	'axes.labelsize': 'medium',
	'xtick.labelsize': 'large',
	'ytick.labelsize': 'large'}

plt.rcParams.update(params)
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['font.sans-serif'] = "cmss10"

X, Y, Z, = np.array([]), np.array([]), np.array([])
for i in range(len(X_dat)):
        X = np.append(X,X_dat[i])
        Y = np.append(Y,Y_dat[i])
        Z = np.append(Z,Z_dat[i])
xi = np.linspace(X.min(),X.max(),1000)
yi = np.linspace(Y.min(),Y.max(),1000)
zi = griddata((X, Y), Z, (xi[None,:], yi[:,None]), method='cubic')
zmin = 2
zmax = 6
zi[(zi<zmin) | (zi>zmax)] = None
CS = plt.contourf(xi, yi, zi, 15, cmap=cm.winter, 
		vmax=zmax, vmin=zmin)
plt.colorbar()  
plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
plt.savefig('%s.png' % filename )
plt.show ()
