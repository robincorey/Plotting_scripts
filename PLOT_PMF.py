#!/sansom/s137/bioc1535/anaconda2/bin/python

import os
import sys
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties

# Fonts

alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
styles = ['normal', 'italic', 'oblique']
font = FontProperties()

#  tick fonts
font1 = font.copy()
font1.set_family('sans-serif')
font1.set_style('normal')

# label fonts
font2 = font.copy()
font2.set_family('sans-serif')
font2.set_style('normal')
font2.set_weight('normal')
rcParams['mathtext.default'] = 'regular'

def energysurface(loc, files, start, end):
	count=False
	d=[]
	os.chdir(loc)
	os.system('pwd')
	print(files)
	inp=open(files)
	for line in inp:
		word = line.strip()
		number = word.split()
		if number[0][0] != '#':
			if number[0][0] != '@':
				if count==False:
				   	d = [[] for x in range(len(number))]
				   	count=True
				if start <= float(number[0]) <= end:
					for i in range(len(number)):
						d[i].append(float(number[i]))

	d[0] = np.array(d[0])
	d[1] = np.array(d[1])
	d[2] = np.array(d[2])
	return d	
	
	
#plot between values
start, end=0, 40 # not sure why we'd want this

rcParams['axes.linewidth']=5
colourline= ['red','K', 'blue']
colourshade= ['red','K', 'blue']
minenergy, maxenergy = 0,0
figure(1, figsize=(10,10))

# Location of output files
base='/sansom/s137/bioc1535/Desktop/Projects/'
location=[base+'Specific_applications/VRG4/PMF/Site_1_A/DATA',base+'Specific_applications/VRG4/PMF/Site_1_A/DATA']

files='bootstrap.xvg'

for i in range(len(location)):
	d = energysurface(location[i], files, start, end)
	d[1]=d[1]+(d[1][-1]*-1)

	if max(d[1]) > maxenergy:
			maxenergy=round(max(d[1]),-1)
	if min(d[1]) < minenergy:
		minenergy = round(min(d[1])-5, -1)
	maxenergy=10
	fill_between(d[0]*10, d[1]-d[2], d[1]+d[2], alpha=0.3, facecolor=colourshade[i])
	plot(d[0]*10, d[1], linewidth=3, color=colourline[i])
	ylim(minenergy, maxenergy);xticks(np.arange(0,40,5), fontproperties=font1, fontsize=25);yticks(np.arange(minenergy, maxenergy,2), fontproperties=font1, fontsize=25)
	tick_params(axis='both', which='major', width=2, length=5, labelsize=25, direction='in', pad=10, right='off', top='off');xlim(start*1, end*1)
	xlim(0,40)
	xlabel('distance($\AA$)', fontproperties=font2,fontsize=20);ylabel('energy (kJ mol$^{-1}$)', fontproperties=font2,fontsize=20) 
	subplots_adjust(left=0.15, wspace=0.15, hspace=0.5, top=0.95, bottom=0.1)
os.chdir(location[0])
savefig('pmf.png', dpi=900)
#show()
