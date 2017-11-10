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
plt.rcParams['axes.facecolor'] = plt.cm.jet(0)
plt.rcParams['axes.unicode_minus']=False
plt.xticks(np.arange(-180, 181, 90))
plt.yticks(np.arange(-180, 181, 90))
plt.hist2d(xdata, ydata, (360, 360), cmap=plt.cm.jet)
plt.plot([59, 59], [99, 179], 'w--', lw=2)
plt.plot([109, 109], [99, 179], 'w--', lw=2)
plt.plot([59, 109], [99, 99], 'w--', lw=2)
plt.plot([59, 109], [179, 179], 'w--', lw=2)
plt.xlim([-180,180])
plt.ylim([-180,180])
strip1 = filename.rstrip('.xvg')
sysname = strip1.replace('_',' ')
plt.text(60, -160, '%s' % sysname, color='white', fontsize=15)
plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
plt.savefig('%s_lines.png' % strip1, bbox_inches='tight')
print datetime.now() - startTime
