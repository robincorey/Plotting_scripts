import scipy as sc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import signal
import sys
from scipy.interpolate import griddata

fig, ax1 = plt.subplots()

# define global arrays

def getdata (file):
	with open(file) as file:  
		array2d = [[float(digit) for digit in line.split()] for line in file]
	x = array2d[0]
	y = [row[0] for row in array2d]
	array2d = np.delete(array2d, (0), axis=1)
	array2d = np.delete(array2d, (0), axis=0)
	return x[1:],y[1:],array2d

x,y,data = getdata('%s' % sys.argv[1])
#CS = plt.contour(x,y,data,np.arange(0.04,0.21,step=0.02),linewidths=0.5,colors='k')
#CS = plt.contourf(x,y,data,np.arange(0.04,0.21,step=0.02),cmap=plt.cm.jet)
plt.imshow(data,interpolation='spline16',cmap=plt.cm.jet,extent=[np.min(x),np.max(x),np.min(y),np.max(y)])
plt.colorbar() 

#xp,yp,zp,msd = np.loadtxt(fname='clip.pdb', comments=['TER','END','TITLE','REMARK','CRYST1','MODEL'], usecols=(5,6,7,9), unpack=True)
#plt.scatter(xp/10, yp/10, c='k', s=5,marker='o')

plt.xticks(np.arange(np.min(x),np.max(x)+1,step=5))
plt.yticks(np.arange(np.min(y),np.max(y)+1,step=5))
ax1.set_xlabel('x (nm)')
ax1.set_ylabel('y (nm)')
plt.savefig('dens_%s.png' % sys.argv[2], bbox_inches='tight')
