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

os.system('bash /sansom/s137/bioc1535/Desktop/CG_KIT/combine_all_f.sh > all_dF_f.txt')
#os.system('bash /sansom/s137/bioc1535/Desktop/CG_KIT/combine_all_r.sh > all_dF_r.txt')

def plot_function ():
	x_f, yf1, yf2, yf3, yf4, yf5 = np.loadtxt(fname='all_dF_f.txt', delimiter=',', comments='Time', usecols=(0,1,2,3,4,5), unpack=True)
	y_f = np.stack((yf1,yf2,yf3,yf4,yf5), axis=1)
	print y_f
	plt.errorbar((x_f/1000), y_f.mean(1), yerr=y_f.std(1), marker='o',mfc='white', mec='green', ms=10, mew=2, ecolor='green',elinewidth=1,capsize=2, color='green')
#        x_r, yr1, yr2, yr3, yr4, yr5 = np.loadtxt(fname='all_dF_r.txt', delimiter=',', comments='Time', usecols=(0,1,2,3,4,5), unpack=True)	
#	y_r = np.stack((yr1,yr2,yr3,yr4,yr5), axis=1)
#        plt.errorbar(-(x_r/1000-275), y_r.mean(1), yerr=y_r.std(1), marker='o',mfc='white', mec='blue', ms=10, mew=2, ecolor='blue',elinewidth=1,capsize=2, color='blue')

def add_average ():
	y = np.loadtxt(fname='average_final_eq.txt', usecols=(0))
	yav = np.mean(y)
	x = np.arange(50,250,1)
	plt.fill_between(x, yav+2.6809, yav-2.6809, alpha=0.3, facecolor='gray')
	plt.plot([50, 250], [yav, yav], color='k', linestyle='--',linewidth=2)
	#plt.ylim([yav-5.3618, yav+5.3618])
	y_min = round(yav-8.04)
	y_max = round(yav+8.04)
	plt.yticks(np.arange(y_min, y_max, step=5))
	plt.ylim([y_min-1, y_max+1])

fig = plt.figure()
ax = fig.add_subplot(111)

add_average()
plot_function()


#leg = plt.legend(bbox_to_anchor=(1.05, 1), loc=2) # , borderaxespad=0.) #frameon=True)
#leg.get_frame().set_edgecolor('k')
#leg.get_frame().set_linewidth(0.0)
plt.xlim=([0,250])
plt.xlabel('time (ns)', fontsize=25 ) 
plt.ylabel('energy (kJ mol$^{-1}$)', fontsize=25 )
plt.savefig('FEP_timecourse.png', bbox_inches='tight', dpi=900)
