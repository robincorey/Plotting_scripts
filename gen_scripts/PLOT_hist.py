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
xlabel = "bins"
ylabel = "pop"
f = open('data','w')
sed = subprocess.call(['sed', '/#/d', filename], stdout=f)
ydata = np.loadtxt(fname='data', comments='@', usecols=(1), unpack=True)

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
plt.rcParams['axes.unicode_minus']=False

#plt.xlim([0,50])
plt.hist(ydata, color='gray') # marker='.', markersize=0)
strip1 = filename.rstrip('.xvg')
sysname = strip1.replace('_',' ')
plt.title('%s' % sysname )
plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
plt.savefig('%s.png' % strip1, bbox_inches='tight')

