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
plt.rcParams['xtick.major.size'] = 0
plt.rcParams['xtick.major.width'] = 0
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['axes.unicode_minus']=False
plt.rcParams.update({'font.size': 15})

def plot_function ():
	filename = 'equil_data.txt'
	x1, y1, yerr = np.loadtxt(fname=filename, comments=['@','#'], usecols=(0,1,2), unpack=True)
	plt.errorbar((x1/1000)+200, y1, yerr=yerr, marker='o', mfc='white', mec='darkorange', ms=10, mew=2, ecolor='darkorange',elinewidth=1,capsize=2, color='darkorange')

fig = plt.figure()
ax = fig.add_subplot(111)

plot_function()

plt.xticks(np.arange(200,1050,step=200))
plt.xlabel('time (ns)', fontsize=25 ) 
plt.ylabel('energy (kJ mol$^{-1}$)', fontsize=25 )
plt.savefig('PMF_timecourse.png', bbox_inches='tight', dpi=900)
