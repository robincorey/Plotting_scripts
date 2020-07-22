import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import signal
import sys
from scipy.interpolate import griddata

#fig = plt.figure()
#ax = fig.add_subplot(111)

fig, ax1 = plt.subplots()

# define global arrays

dens = []

def getdata (rep, end):
	global dens
	with open('%s.%s' % (rep, end)) as file:  
		array2d = [[float(digit) for digit in line.split()] for line in file]
	array2d = np.delete(array2d, (0), axis=1)
	coord = array2d[0]
	array2d = np.delete(array2d, (0), axis=0)
	flatten = np.mean(array2d,axis=0)
        if dens == []:
                print 'empty'
                dens = flatten
	elif dens != []:
		print 'not empty'
		dens = np.column_stack((dens,flatten))
	return coord

for rep in np.arange(1,4):
	coord = getdata(rep, 'dat')

ax1.plot(coord, np.mean(dens,axis=1), color='red', linewidth=3)
ax1.fill_between(coord, np.mean(dens,axis=1)+np.std(dens,axis=1), np.mean(dens,axis=1)-np.std(dens,axis=1), alpha=0.3, facecolor='gray')
ax1.plot(coord, np.mean(dens,axis=1)+np.std(dens,axis=1), color='gray', linewidth=0.5)
ax1.plot(coord, np.mean(dens,axis=1)+np.std(dens,axis=1), color='gray', linewidth=0.5)

dens = []

for rep in np.arange(1,4):
        coord = getdata(rep, 'prot.dat')

ax2 = ax1.twinx()

ax2.plot(coord, np.mean(dens,axis=1), color='blue', linewidth=3)
ax2.fill_between(coord, np.mean(dens,axis=1)+np.std(dens,axis=1), np.mean(dens,axis=1)-np.std(dens,axis=1), alpha=0.3, facecolor='gray')
ax2.plot(coord, np.mean(dens,axis=1)+np.std(dens,axis=1), color='gray', linewidth=0.5)
ax2.plot(coord, np.mean(dens,axis=1)+np.std(dens,axis=1), color='gray', linewidth=0.5)

#plt.xticks(np.arange(0,21,step=5))
#plt.yticks(np.arange(0,21,step=5))
ax1.set_xlabel('x (nm)')
ax1.set_ylabel('TAG density')
ax2.set_ylabel('protein density')
plt.savefig('test.png', bbox_inches='tight')
