#!/sansom/s137/bioc1535/anaconda2/bin/python

import matplotlib.patches as mpatches
import scipy as sc
import numpy as np
import matplotlib.cm as cm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import csv

def Count(filename):
	file = open(filename,'r')
	count = 0
	keyword = ' s'
	for line in file:
    		if keyword in line:
        		count = count + 1
	centre = 0
	data = []
	for i in np.arange(0,count):
		x, y = np.loadtxt(fname=filename, usecols=[0,i+1], comments=['#','@'], unpack=True)
		centre = centre + y[0]
		if data == []:
			data = y
		elif data != []:
			data = np.column_stack((data,y))
	centre = centre/count
	cmap = cm.get_cmap('rainbow_r', count)
	for i in np.arange(0,count):
#		print(data[:, i])
		plt.plot(x/1000000,data[:, i]-centre,c=cmap(i), linewidth=0.5)


Count(sys.argv[1])

mu = u'\u03bc'
plt.xlabel('time (%ss)' % mu, fontsize=16)
plt.ylabel('PO4 z position (nm)', fontsize=16)
plt.xticks(np.arange(0,16,step=5))
plt.xlim(0,3)
plt.yticks(np.arange(-4,5,step=2))
plt.ylim(-4,4)
#plt.savefig('%s.pdf' % sys.argv[2], bbox_inches='tight', format='pdf' )
plt.savefig('Figs/%s.png' % sys.argv[2] , bbox_inches='tight')
	
