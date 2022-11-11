#!/sansom/s137/bioc1535/programs/anaconda2/bin/python

import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import sys

params = {'legend.fontsize': 'large',
        'axes.labelsize': 'xx-large',
        'xtick.labelsize': 'large',
        'ytick.labelsize': 'large'}
plt.rcParams.update(params)
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.major.width'] = 0
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['axes.unicode_minus']=False
plt.rcParams.update({'font.size': 15})

os.system('bash /sansom/s137/bioc1535/Desktop/CG_KIT/get_comp_data.sh > comp.txt')

ylabel = "energy (kJ mol$^{-1}$)"

fig = plt.figure()
ax = fig.add_subplot(111)
colors = [ 'red', 'blue', 'green', 'orange', 'purple', 'cyan']

def set_axis ():
	ydata = np.genfromtxt(fname='comp.txt', usecols=(1,4,7,10,13,16), unpack=True)
	plt.yticks(np.arange(np.round(np.min(ydata)-5, 0), np.round(np.max(ydata)+5,0), step=5))

def plot_function (tech, col, num):
	x = [ num,num,num,num,num ]
	ydata = np.genfromtxt(fname='comp.txt', usecols=(col), unpack=True)
	std = np.std(ydata)
	yav = np.mean(ydata)
	#ax.bar(x, yav, width=0.3, facecolor='none', align='center', edgecolor=colors[num], linewidth=3,yerr=std, capsize=4, ecolor=colors[counter], alpha=0.1, joinstyle='round')
	ax.scatter(x, ydata, facecolors='none', s=75, edgecolors=colors[num], linewidths=1)
	ax.errorbar(num, yav, yerr=std, marker='_', color='k', capsize=2)
	#plt.ylim([np.min(ydata)-5,np.max(ydata)+5])

techniques = {'TI':1, 'TI-C':4, 'DEXP':7, 'IEXP':10, 'BAR':13, 'MBAR':16}

for num, (tech, col) in enumerate(techniques.items()):
	print tech
	print col
	print num
	plot_function( tech, col, num)

set_axis()

#plt.xlim([0.75,1.75])
plt.xticks(np.arange(0.3,6.3), ('TI', 'TI-CUBIC', 'DEXP', 'IEXP', 'BAR', 'MBAR'),  rotation=45, horizontalalignment='right')
plt.ylabel('%s' % ylabel, fontsize=25 )
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(3, 5)
plt.savefig('FEP_comp.png', bbox_inches='tight', dpi=900)
