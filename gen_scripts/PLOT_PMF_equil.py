#!/sansom/s137/bioc1535/programs/anaconda2/bin/python

import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import re
import sys
import os.path

params = {'legend.fontsize': 'large',
        'axes.labelsize': 'xx-large',
        'xtick.labelsize': 'large',
        'ytick.labelsize': 'large'}
plt.rcParams.update(params)
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['xtick.major.size'] = 0
plt.rcParams['xtick.major.width'] = 0
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['axes.unicode_minus']=False
plt.rcParams.update({'font.size': 15})

xlabel = "distance (nm)"
ylabel = "energy (kJ mol$^{-1}$)"

def plotdata (name,num):
	filename = 'convergence/%s_pmf.xvg' % (name)
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
	print '%s -%s %s' % (name, diff, err)
	plt.plot(xdata-x_min, ydata-bulk, color=colors[num], linewidth=2, label=name) 

colors = cm.rainbow(np.linspace(0, 1, 15 )) 
for num,pmf in enumerate(np.arange(100000,850000,50000)):
	plotdata(pmf,num)
	
plt.xlabel('%s' % xlabel, fontsize=25 )
plt.ylabel('%s' % ylabel, fontsize=25 )
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(4, 5)
plt.savefig('equil_time.png', bbox_inches='tight')

