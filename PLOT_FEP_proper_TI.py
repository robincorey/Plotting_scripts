#!/sansom/s137/bioc1535/programs/anaconda2/bin/python

import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import sys

def loaddata ( str ):
        print "%s" % y
	return

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
#plt.rcParams['font.sans-serif'] = "sans-serif" #cmss10"
plt.rcParams['axes.unicode_minus']=False
plt.rcParams.update({'font.size': 15})

plt.xticks([1,1.5],['bound','free'])
ylabel = "energy (kJ mol$^{-1}$)"

x = [ 1, 1.05, 0.95, 1.025, 0.975 ]

filename = sys.argv[1]
ydata = np.loadtxt(fname=filename, usecols=(0), unpack=True)
for i in range(len(x)):
	plt.scatter(x[i], ydata[i], facecolors='none', s=100, edgecolors='red', linewidths=2)
ave1=np.mean(ydata)
std1=np.std(ydata)
plt.errorbar(1, ave1, yerr=std1, color='k', elinewidth=2, capsize=10, capthick=2, barsabove='True')
plt.plot(1,np.mean(ydata), marker='_', color='k', markersize=60, markeredgecolor='k', markeredgewidth=3)

x = [1.5,1.55,1.45,1.525,1.475] 
filename2 = sys.argv[2]
ydata = np.loadtxt(fname=filename2, usecols=(0), unpack=True)
#xdata = ([2,2,2,2,2])
for i in range(len(x)):
	plt.scatter(x[i], ydata[i], facecolors='none', s=100, edgecolors='blue', linewidths=2)
ave2=np.mean(ydata)
std2=np.std(ydata)
plt.errorbar(1.5, ave2, yerr=std2, color='k', elinewidth=2, capsize=10, capthick=2, barsabove='True')
plt.plot(1.5,np.mean(ydata), marker='_', color='k', markersize=60, markeredgecolor='k', markeredgewidth=3)

print '%s +/- %s' % ( ave1, std1 )
print '%s +/- %s' % ( ave2, std2 )

diff = ave1 - ave2
diffsd = std1 + std2
pos = ave2 + (diff/2)
print 'difference is %d +/- %d'  % ( diff, diffsd )

print pos

plt.xlim([0.75,1.75])
plt.ylabel('%s' % ylabel, fontsize=25 )
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(3, 5)
plt.savefig('FEP_TI.png', bbox_inches='tight', dpi=900)

