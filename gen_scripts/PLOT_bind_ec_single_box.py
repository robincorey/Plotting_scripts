#!/sansom/s137/bioc1535/programs/anaconda2/bin/python

import scipy as sc
import numpy as np
from scipy import stats
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


ylabel = "bound lipid count"
ylims = [0]
xposition = [] 
pdb = sys.argv[1]
lipids = [ 'POPE' , 'POPG', 'CARD' ]
rm_cmd = 'rm -f %s.binding.txt' % pdb
os.system(rm_cmd)

def plot_function (pdb, lipid, counter):
	leaflets = [  'lower', 'upper' ]
	low = []
	up = []
	for shift, leaflet in enumerate(leaflets):
		shift_value = float((shift - 0.5)*0.35)
		x = [ counter+shift_value ] * 9
		xposition.append(counter+shift_value-0.1)
		filename = 'binding_data/%s_binding_%s_%s.txt' % ( leaflet, pdb, lipid )
		print filename # upper_binding_5AJI_CARD.txt
		ydata = np.genfromtxt(fname=filename, usecols=(4), unpack=True)
		if leaflet is 'lower':
			low = ydata
		elif leaflet is 'upper':
			up = ydata
		std = np.std(ydata)
	        yav = np.mean(ydata)
		ymax = np.max(ydata)
		yav_int = round(yav, 1)
		std_int = round(std, 1)
		ylims.append(ymax)
		#ax.bar(x, yav, width=0.3, facecolor='none', align='center', edgecolor=colors[counter], linewidth=3,yerr=std, capsize=4, ecolor=colors[counter], alpha=0.1, joinstyle='round')
		bp = ax.boxplot(ydata, positions=[counter+shift_value])
		plt.setp(bp['boxes'], color=colors[counter])
		ax.scatter(x, ydata, facecolors='none', s=50, edgecolors=colors[counter], linewidths=0.2)
		#ax.text(counter+shift_value,yav+1.5,'%s' % yav_int,  color='k', fontsize=10, horizontalalignment='center')
		f = open('%s.binding.txt' % pdb, 'a')
		f.write('%s %s %s %s +/- %s\n' % (pdb, lipid, leaflet, yav_int, std_int))
	#print low
	#print up
	p2 = 1
	t2, p2 = stats.ttest_ind(up,low)
	#print t2
	print 'p = %s' % p2
	if p2 < 100:
		sig = 'ns'
	if p2 < 0.05:
		sig = '*'
	if p2 < 0.01:
		sig = '**'
	if p2 < 0.001:
		sig = '***'
	alldata = np.concatenate((up, low))
	print alldata
	print up
	print low
	plt.text(counter+shift_value-0.175,np.max(alldata)+1,sig, horizontalalignment='center')
	f2 = open('pvalues.txt', 'a')
	f2.write('%s %s = %s\n' % (pdb, lipid, p2))

fig = plt.figure()
ax = fig.add_subplot(111)
colors = [ 'red', 'blue', 'green' ]
		
for counter, lipid in enumerate(lipids):
	plot_function(pdb, lipid, counter)

#print np.max(ylims)
plt.ylim(0,np.max(ylims)+4)
plt.yticks(np.arange(0, np.max(ylims)+5, step=5 ))
#plt.xticks(np.arange(-0.5, 2.5, step=0.5), ('inner', 'outer', 'inner', 'outer', 'inner', 'outer'), rotation=45)
plt.xticks(xposition, ('inner', 'outer', 'inner', 'outer', 'inner', 'outer'), rotation=45)
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=25 )
plt.title('%s' % pdb)
plt.savefig('%s_box.png' % pdb, bbox_inches='tight', dpi=900)
