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

def loaddata ( str ):
        print "%s" % y
	return

def plotfunction ( str ):
	#filename = sys.argv[1]
	nuc = sys.argv[1]
	filename = '%s/%s/plot.data' % ( nuc, i[j] )
	#print '%s' % filename
	xlabel = "z coordinate ($\AA$)"
	ylabel = "radius ($\AA$)"
	xdata, ydata = np.loadtxt(fname='%s' % filename, delimiter=',', usecols=(0,1), unpack=True)	
	av = '%s_av.data' % nuc
	xav, yav = np.loadtxt(fname='%s' % av, delimiter=',', usecols=(0,1), unpack=True)
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
	plt.ylim([1.5,5.5])
	plt.xlim([-7,7])
	colors = cm.rainbow(np.linspace(0, 1, 31 )) 
	plt.plot(xdata, ydata, color='gray', marker='.', markersize=0)
	plt.plot(xav, yav, color='red', marker='.', markersize=1)
	plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
	plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
	plt.savefig('%s%s_gray.png' % (filename, nuc), bbox_inches='tight')

i=[500, 502, 504, 506, 508, 510, 600, 602, 604, 606, 608, 610, 700, 702, 704, 706, 708, 710, 800, 802, 804, 806, 808, 810, 900, 902, 904, 906, 908, 910, 1000]

for j in xrange(0, 31):
        plotfunction(j)
