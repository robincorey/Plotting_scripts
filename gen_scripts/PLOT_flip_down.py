#!/sansom/s137/bioc1535/anaconda2/bin/python

import matplotlib.patches as mpatches
import scipy as sc
import numpy as np
import matplotlib.cm as cm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path
from scipy import signal
from matplotlib.font_manager import FontProperties

def PlotLipidContact(j): 
	xlabel = "time ($\mu$s)"
	ylabel = "z-position (nm)"
	val = int(j)
	val2 = int(k)
	ydata = np.loadtxt(fname=filename, usecols=val, unpack=True) #% val
	#xdata = np.loadtxt(fname=filename, usecols=0, unpack=True)
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
	plt.tick_params(labelsize=18)
	smooth = sc.signal.savgol_filter(ydata-7.50412, 25, 1, deriv=0, delta=1, axis=-1, mode='interp', cval=0.0)
	plt.plot(xdata, smooth, color=next(colors), linewidth=1) 
        plt.axes().set_aspect(0.2)
	strip1 = filename.rstrip('.xvg')
	sysname = strip1.replace('_',' ')
	plt.xlabel('%s' % xlabel, fontproperties=font2, fontname="cmss10", fontsize=25 )
	plt.ylabel('%s' % ylabel, fontproperties=font2, fontname="cmss10", fontsize=25 )
	plt.savefig('flip%s.png' % j)
	return

# Fonts
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
styles = ['normal', 'italic', 'oblique']
font = FontProperties()

#  tick fonts
font1 = font.copy()
font1.set_family('sans-serif')
font1.set_style('normal')
font2 = font.copy()
font2.set_family('sans-serif')
font2.set_style('normal')
font2.set_weight('normal')
plt.rcParams['mathtext.default'] = 'regular'

filename = 'PO4.xvg'
xdata = np.loadtxt(fname=filename, usecols=0, unpack=True)
plt.plot([0.1, 1.3292], [-2.56991, -2.56991], '0.8', lw=40)
plt.plot([0.1, 1.3292], [2.56988, 2.56988], '0.8', lw=40)
text_file = open("down.xvg", "r")
lines = text_file.read().split('\n')
x = np.arange(5)
ys = [i+x+(i*x)**2 for i in range(5)]
colors = iter(cm.rainbow(np.linspace(0, 1, len(ys))))

for k, j in enumerate(lines):
	if not j == "":
		print j
		PlotLipidContact(j)
plt.tight_layout()
plt.savefig('flip_downsca.png') 
