#!/sansom/s137/bioc1535/anaconda2/bin/python

import matplotlib.patches as mpatches
import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path
'''
import matplotlib.cm as cm
from scipy.optimize import curve_fit
from scipy import optimize
from scipy import signal
import os
import re
import sys
import csv
import shutil
#import pandas as pd
mport subprocess
import os.path
from scipy.interpolate import spline
'''

def PlotLipidContact(j): 
	xlabel = "time ($\mu$s)"
	ylabel = "lipid (#)"
	ydata = np.loadtxt(fname=filename, skiprows=2, unpack=True)
	xdata = np.loadtxt(fname='time.xvg', unpack=True)
	params = {'legend.fontsize': 'large',
		'axes.labelsize': 'x-large',
		'xtick.labelsize': 'x-large',
		'ytick.labelsize': 'x-large'}
	plt.rcParams.update(params)
	plt.rcParams['axes.linewidth'] = 2
	plt.rcParams['xtick.major.size'] = 5
	plt.rcParams['xtick.major.width'] = 2
	#plt.rcParams['ytick.minor.size'] = 1
	plt.rcParams['ytick.major.size'] = 5
	plt.rcParams['ytick.major.width'] = 2
	plt.rcParams['font.sans-serif'] = "cmss10"
	plt.rcParams['axes.unicode_minus']=False
	#minor_yticks = np.arange(min(ydata), max(ydata)+1, 1)
	#plt.grid(b=True, which='minor', axis='y', color='gray', linestyle='--')
	#plt.minorticks_on()
	scale = 3/(k+0.1)
	plt.axes().set_aspect(scale) #scale, adjustable='box', anchor='SW')
	plt.scatter(xdata, ydata, color=lipid_color[lipid], marker='s', s=1)
	strip1 = filename.rstrip('.xvg')
	sysname = strip1.replace('_',' ')
	plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=25 )
	plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
	return

#plt.savefig('%s.png' % strip1, bbox_inches='tight')


text_file = open("lipid_array.txt", "r")
lines = text_file.read().split('\n')

lipid_color = {}
for k, j in enumerate(lines):
        if os.path.isfile('%s_occ.xvg' % j):
		filename = '%s_occ.xvg' % j
		line_number = 2
		with open(filename) as f:
                	lipid = f.read().splitlines()[1] 
		colors = [ 'blue', 'red', 'green', 'orange', 'teal', 'purple' ]
        	if lipid not in lipid_color:
			position = len(lipid_color)
                	lipid_color[lipid] = colors[position]
        	PlotLipidContact(j)

patchList = []

for key in lipid_color:
	data_key = mpatches.Patch(color=lipid_color[key], label=key) #, loc='center left', bbox_to_anchor=(1, 0.5)) 
	patchList.append(data_key)

print patchList

leg = plt.legend(handles=patchList,  bbox_to_anchor=(1, 0.5), loc='center left') ##)#, bbox_to_anchor=(1.04,0.5), loc='center left')
leg.get_frame().set_edgecolor('k')
leg.get_frame().set_linewidth(2)
#plt.tight_layout()
plt.savefig('test_legend.png', bbox_extra_artists=(leg,), bbox_inches='tight') 
