#!/home/birac/anaconda2/bin/python
import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import signal
import sys
import subprocess

def loaddata ( str ):
        print "%s" % y
	return

filename = sys.argv[1]
xlabel = "time ($\mu$s)"
ylabel = "RMSD (nm)"
f = open('data','w')
sed = subprocess.call(['sed', '/#/d', filename], stdout=f)
xdata, ydata = np.loadtxt(fname='data', comments='@', usecols=(0,1), unpack=True)	

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

plt.plot(xdata, ydata, color='gray', marker='.', markersize=0)
smooth = sc.signal.savgol_filter(ydata, 11, 1, deriv=0, delta=1, axis=-1, mode='interp', cval=0.0)
plt.plot(xdata, smooth, 'red', linewidth=0.5)

plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
plt.savefig('%s.png' % filename, bbox_inches='tight')
