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

ylabel = "distance (nm)"
xlabel = "energy (kJ mol$^{-1}$)"

data = []

def loaddata (name):
	global data
#	filename = 'bsres_%s.xvg' % (name)
	x, y, y1 = np.loadtxt(fname=file, comments=['@','#'], usecols=(0,1,2), skiprows=20, unpack=True)
	if data == []:
                print 'empty'
                data = y
        elif data != []:
                print 'not empty'
                data = np.column_stack((data,y))
	return x, data

def plotdata (xdata,ydata,yerr1):
#	bulk_value = ydata[-10:]
#	start = xdata[-1:]
#	minimum = np.amin(ydata)
#	bulk = np.average(bulk_value)
#	diff = int(bulk - minimum)
#	for i in [i for i,x in enumerate(ydata) if x == minimum]:
 #       	pass
#	min_err = yerr1[i]
#	bulk_err = yerr1[-10:]
#	bulk_err_av =  np.average(bulk_err)
#	x_min= xdata[i] 
#	err = int(round(bulk_err_av + min_err))
#	print '%s -%s %s' % (name, diff, err)
	x_min = 0
	bulk = 0
	plt.plot(xdata, ydata, color='blue', linewidth=2)
	plt.fill_between(xdata-x_min, ydata-bulk-yerr1, ydata-bulk+yerr1, alpha=0.3, facecolor='gray')
	plt.plot(xdata, ydata-yerr1,  color='blue', linewidth=0.5)
	plt.plot(xdata, ydata+yerr1,  color='blue', linewidth=0.5)


plt.xlabel('%s' % ylabel , fontsize=20 )
plt.ylabel('%s' % xlabel , fontsize=20 )
plt.legend(frameon=False)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 6)

file='bsResult_1.xvg'
x,y1 = loaddata(file)
file='bsResult_3.xvg'
x, y3 = loaddata(file)
file='bsResult_4.xvg'
x,y4 = loaddata(file)

plotdata(x,np.average(data,axis=1 ),np.std(data,axis=1))
plt.savefig('PMF_WT_av.png', bbox_inches='tight', dpi=600 )

