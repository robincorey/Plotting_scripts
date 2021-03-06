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

filename = sys.argv[1]
xlabel = "distance (nm)"
ylabel = "energy (kJ mol$^{-1}$)"
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

print 'energy well is %s +/- %s' % (diff, err)

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
#plt.rcParams['font.sans-serif'] = "cmss10"
plt.rcParams['axes.unicode_minus']=False
plt.rcParams.update({'font.size': 15})

plt.plot(xdata-x_min, ydata-bulk, color='red', linewidth=3) 
plt.fill_between(xdata-x_min, ydata-bulk-yerr1, ydata-bulk+yerr1, alpha=0.3, facecolor='gray')
plt.plot(xdata-x_min, ydata-bulk-yerr1, color='gray', linewidth=0.5)
plt.plot(xdata-x_min, ydata-bulk+yerr1, color='gray', linewidth=0.5)

strip1 = filename.rstrip('.xvg')
sysname = strip1.replace('_',' ')
plt.xlabel('%s' % xlabel, fontsize=25 )
plt.ylabel('%s' % ylabel, fontsize=25 )
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(4, 5)
plt.savefig('%s.png' % strip1, bbox_inches='tight')


#pmf_current=np.genfromtxt('pmf.xvg', autostrip=True, comments='@',skip_header=13)

#plt.figure(1, figsize=(30,30))
#plt.plot(pmf_current[:,0],pmf_current[:,1], linewidth=3, color='red')
#plt.xticks(xt, fontproperties=font1,  fontsize=15)
#plt.yticks(np.arange(0, 1.3,0.2), fontproperties=font1,  fontsize=15)
#plt.tick_params(axis='both', which='major', width=3, length=5, labelsize=15, direction='out', pad=10)
#plt.ylim(0,1.2)
#plt.xlim(0,10)
#plt.show() # or         plt.savefig('pmf.png', dpi=600
