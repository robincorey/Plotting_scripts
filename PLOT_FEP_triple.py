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

colors = ['', 'red', 'red', 'red', 'blue' ]

def plot_function (num):
	x = [ num-0.1,num-0.05,num,num+0.05,num+0.1 ]
	ydata = np.genfromtxt(fname=sys.argv[num], usecols=(0), unpack=True)
	std = np.std(ydata)
	yav = np.mean(ydata)
	plt.scatter(x, ydata, facecolors='none', s=75, edgecolors=colors[num], linewidths=1)
	plt.errorbar(num, yav, yerr=std, marker='_', color='k', capsize=10, capthick=2, barsabove='True')
	#plt.errorbar(1.5, ave2, yerr=std2, color='k', elinewidth=2, capsize=10, capthick=2, barsabove='True')
	plt.plot(num,yav, marker='_', color='k', markersize=40, markeredgecolor='k', markeredgewidth=3)
	#plt.ylim([np.min(ydata)-5,np.max(ydata)+5])

for num in np.arange(1,5):
	print num
	plot_function(num)

plt.yticks(np.arange(130,146,step=5))
plt.xticks([2,4],['bound','free'])
plt.xlim([0.25,4.75])
plt.ylabel("energy (kJ mol$^{-1}$)", fontsize=25) #, position=(0,1.5) )
plt.axes().set_aspect(0.35)
plt.figure(1, figsize=(4,3))
plt.savefig('FEP_triple.png', bbox_inches='tight')

