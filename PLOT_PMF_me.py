#!/sansom/s137/bioc1535/anaconda2/bin/python

import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
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
#xlabel = "distance ($\AA$)"
xlabel = "distance (nm)"
ylabel = "energy (kJ mol$^{-1}$)"
f = open('data','w')
sed = subprocess.call(['sed', '/#/d', filename], stdout=f)
xdata, ydata, yerr1 = np.loadtxt(fname='data', comments='@', usecols=(0,1,2), unpack=True)

params = {'legend.fontsize': 'large',
	'axes.labelsize': 'xx-large',
	'xtick.labelsize': 'large',
	'ytick.labelsize': 'large'}
plt.rcParams.update(params)
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['font.sans-serif'] = "cmss10"
plt.rcParams['axes.unicode_minus']=False
plt.rcParams.update({'font.size': 15})

#plt.ylim([0,0.65])
plt.errorbar(xdata, ydata-41.6, color='#ff8000', markersize=0, yerr=yerr1, ecolor='#ffbf80', capthick=0 )
plt.plot(xdata, ydata-41.6, color='#ff8000') 
strip1 = filename.rstrip('.xvg')
sysname = strip1.replace('_',' ')
plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
plt.savefig('%s.png' % strip1, bbox_inches='tight')

