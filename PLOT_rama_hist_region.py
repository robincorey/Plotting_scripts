#!/home/birac/anaconda2/bin/python
#
# python script to plot any Gromacsdata file
# 

import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import signal
import sys
import subprocess
from scipy.stats import gaussian_kde
from datetime import datetime

startTime = datetime.now()

def loaddata ( str ):
        print "%s" % y
	return

filename = sys.argv[1]
xlabel = "$\phi$"
ylabel = "$\psi$"
f = open('data_%s' % filename,'w')
sed = subprocess.call(['sed', '/#/d', filename], stdout=f)
xdata, ydata = np.loadtxt(fname='data_%s' % filename, comments='@', usecols=(0,1), unpack=True)	

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
plt.xlim([45,135])
plt.ylim([90,180])
plt.xticks(np.arange(45, 136, 30))
plt.yticks(np.arange(90, 181, 30))
plt.hist2d(xdata, ydata, (720, 720), cmap=plt.cm.jet, range=([40,135],[90,180]))
plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
plt.savefig('%s.png' % filename, bbox_inches='tight')
print datetime.now() - startTime
