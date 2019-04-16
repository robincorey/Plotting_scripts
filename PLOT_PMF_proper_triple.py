#!/sansom/s137/bioc1535/programs/anaconda2/bin/python

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
import subprocess
import os.path

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
plt.rcParams['axes.unicode_minus']=False
plt.rcParams.update({'font.size': 15})

def plot_pmf(num):
	x, y, y1 = np.loadtxt(fname=filename, comments=['@','#'], usecols=(0,1,2), skiprows=20, unpack=True)
	xdata = x[:-12]
	ydata = y[:-12]
	yerr1 = y1[:-12]
	bulk_value = ydata[-10:]
	start = xdata[-1:]
	minimum = np.amin(ydata)
	bulk = np.average(bulk_value)
	diff = int(bulk - minimum)
	for i in [i for i,x in enumerate(ydata) if x == minimum]:
		pass
	min_err = yerr1[i]
	bulk_err = yerr1[-10:]
	bulk_err_av =  np.average(bulk_err)
	x_min= xdata[i] 
	err = int(round(bulk_err_av + min_err))
	print 'site %s energy well is %s +/- %s' % (num, diff, err)
	plt.subplots(4,1,num)
	plt.plot(xdata-x_min, ydata-bulk, color='red', linewidth=3)
	plt.fill_between(xdata-x_min, ydata-bulk-yerr1, ydata-bulk+yerr1, alpha=0.3, facecolor='gray')
	plt.plot(xdata-x_min, ydata-bulk-yerr1, color='gray', linewidth=0.5)
	plt.plot(xdata-x_min, ydata-bulk+yerr1, color='gray', linewidth=0.5)

plt.figure(1, figsize=(4,5))

filename = sys.argv[1]
plot_pmf(1)
filename = sys.argv[2]
plot_pmf(2)
filename = sys.argv[3]
plot_pmf(3)

plt.xlabel("distance (nm)", fontsize=25 )
plt.ylabel("energy (kJ mol$^{-1}$", fontsize=25 )
#fig = matplotlib.pyplot.gcf()
#fig.set_size_inches(4, 5)
plt.savefig('PMF_triple.png', bbox_inches='tight')
