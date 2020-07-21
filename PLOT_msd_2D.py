import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import signal
import sys
from scipy.interpolate import griddata

fig = plt.figure()
ax = fig.add_subplot(111)

# define global arrays

all_x = []
all_y = []
all_msd = []

def getdata (num,rep):
	global all_x
	global all_y
	global all_msd
	print 'msd_data/%s.%s.pdb' % (num, rep)
	# load data
	x,y,z,msd = np.loadtxt(fname='msd_data/%s.%s.pdb' % (num, rep), comments=['TER','END','TITLE','REMARK','CRYST1','MODEL'], usecols=(5,6,7,9), unpack=True)
	all_x = np.append(all_x,x)
	all_y = np.append(all_y,y)
	all_msd = np.append(all_msd,msd)	

for num in np.arange(41,49):
        for rep in [1,2,3]:
                getdata(num,rep)

print np.max(all_msd)
print np.min(all_msd)
# define grid
xi = np.linspace(np.min(all_x/10),np.max(all_x/10),40)
yi = np.linspace(np.min(all_y/10),np.max(all_y/10),40)
# grid data
zi = griddata((all_x/10, all_y/10), all_msd, (xi[None,:], yi[:,None]), method='nearest')
# contour the gridded data, plotting dots at the randomly spaced data points.
CS = plt.contour(xi,yi,zi,8,linewidths=0.5,colors='k')
CS = plt.contourf(xi,yi,zi,8,cmap=plt.cm.jet)
plt.colorbar() # draw colorbar
# plot data points.
#plt.scatter(x,y,marker='o',c='b',s=5)

x,y,z,msd = np.loadtxt(fname='clip_prot.pdb', comments=['TER','END','TITLE','REMARK','CRYST1','MODEL'], usecols=(5,6,7,9), unpack=True)
plt.scatter(x/10, y/10, c='white', s=5, edgecolor='k',marker='o')

plt.xlim([0,20])
plt.ylim([0,20])
plt.xticks(np.arange(0,21,step=5))
plt.yticks(np.arange(0,21,step=5))
plt.xlabel('x (nm)')
plt.ylabel('y (nm)')
plt.savefig('msd_test.png', bbox_inches='tight')
