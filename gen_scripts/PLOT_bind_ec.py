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
#plt.rcParams['font.sans-serif'] = "cmss10"
plt.rcParams['axes.unicode_minus']=False
plt.rcParams.update({'font.size': 15})


ylabel = "bound lipid count"

xposition = [] 
pdb = sys.argv[1]
lipids = [ 'POPE' , 'POPG', 'CARD' ]
rm_cmd = 'rm -f %s.binding.txt' % pdb
os.system(rm_cmd)

def plot_function (pdb, lipid, counter):
	leaflets = [  'lower', 'upper' ]
	for shift, leaflet in enumerate(leaflets):
		shift_value = float((shift - 0.5)*0.35)
		x = [ counter+shift_value, counter+shift_value, counter+shift_value ]
		xposition.append(counter+shift_value-0.1)
		filename = 'binding_data/%s_binding_%s_%s.txt' % ( leaflet, pdb, lipid )
		print filename
		ydata = np.genfromtxt(fname=filename, usecols=(3), unpack=True)
		std = np.std(ydata)
	        yav = np.mean(ydata)
		yav_int = round(yav, 1)
		std_int = round(std, 1)
		ax.bar(x, yav, width=0.3, facecolor='none', align='center', edgecolor=colors[counter], linewidth=3,yerr=std, capsize=4, ecolor=colors[counter], alpha=0.1, joinstyle='round')
                ax.scatter(x, ydata, facecolors='none', s=75, edgecolors=colors[counter], linewidths=1)
		#ax.text(counter+shift_value,yav+1.5,'%s' % yav_int,  color='k', fontsize=10, horizontalalignment='center')
		f = open('%s.binding.txt' % pdb, 'a')
		f.write('%s %s %s %s +/- %s\n' % (pdb, lipid, leaflet, yav_int, std_int))

fig = plt.figure()
ax = fig.add_subplot(111)
colors = [ 'red', 'blue', 'green' ]
		
for counter, lipid in enumerate(lipids):
	plot_function(pdb, lipid, counter)

#plt.yticks(np.arange(0, 21, step=5 ))
#plt.xticks(np.arange(-0.5, 2.5, step=0.5), ('inner', 'outer', 'inner', 'outer', 'inner', 'outer'), rotation=45)
plt.xticks(xposition, ('inner', 'outer', 'inner', 'outer', 'inner', 'outer'), rotation=45)
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
plt.title('%s' % pdb)
plt.savefig('%s.png' % pdb, bbox_inches='tight', dpi=900)
