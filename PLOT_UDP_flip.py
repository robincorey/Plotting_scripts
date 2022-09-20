#!/sansom/s137/bioc1535/anaconda2/bin/python

import matplotlib.patches as mpatches
import scipy as sc
import numpy as np
import matplotlib.cm as cm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]

def PlotFlip(filename):
	x, y1, y2, y3, y4, y5, y6 = np.loadtxt(fname=filename, usecols=[0,1,2,3,4,5,6], comments=['#','@'], unpack=True)
	centre = (y1[0]+y2[0]+y3[0]+y4[0]+y5[0]+y6[0])/6
	print centre
	plt.plot(x/1000000,y1-centre,color='red', linewidth=0.5)
	plt.plot(x/1000000,y2-centre,color='orange', linewidth=0.5)
	plt.plot(x/1000000,y3-centre,color='yellow', linewidth=0.5)
	plt.plot(x/1000000,y4-centre,color='green', linewidth=0.5)
	plt.plot(x/1000000,y5-centre,color='blue', linewidth=0.5)
	plt.plot(x/1000000,y6-centre,color='violet', linewidth=0.5)
	plt.plot([0, np.max(x/1000000)], [2, 2], color='gray',linewidth=6, alpha=0.5)
	plt.plot([0, np.max(x/1000000)], [-2, -2], color='gray',linewidth=6, alpha=0.5)

PlotFlip(filename)
	
mu = u'\u03bc'
plt.xlabel('time (%ss)' % mu, fontsize=16)
plt.ylabel('PO4 z position (nm)', fontsize=16)
plt.xticks(np.arange(0,16,step=5))
plt.xlim(0,15)
plt.yticks(np.arange(-4,5,step=2))
plt.ylim(-4,4)
#plt.savefig('%s.pdf' % sys.argv[2], bbox_inches='tight', format='pdf' )
plt.savefig('%s.png' % sys.argv[2], bbox_inches='tight')
