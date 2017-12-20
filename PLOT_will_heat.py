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

def loaddata ( str ):
        print "%s" % y
	return

filename = sys.argv[1]
xlabel = "charge"
ylabel = "lys/arg"
f = open('data','w')
sed = subprocess.call(['sed', '/#/d', filename], stdout=f)
ydata, xdata = np.loadtxt(fname='data', comments='@', usecols=(0,1), unpack=True)	

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
plt.ylim([-0.1,1.1])
plt.xlim([-60,60])
plt.xticks(np.arange(-60, 61, 30))
plt.yticks(np.arange(0, 1.1, 0.2))
xy = np.vstack([xdata,ydata])
z = gaussian_kde(xy)(xy)
idx = z.argsort()
x, y, z = xdata[idx], ydata[idx], z[idx]
plt.scatter(x, y, c=z, s=50, edgecolor='', cmap='jet')
plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
plt.plot([0, 0], [0, 0.99], 'k--', lw=2)
plt.plot([-59, 59], [0.5, 0.5], 'k--', lw=2)
plt.savefig('%s.png' % filename, bbox_inches='tight')
