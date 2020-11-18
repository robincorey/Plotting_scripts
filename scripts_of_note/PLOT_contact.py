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
		array2d = [[float(digit) for digit in line.split(',')] for line in file]
	x = array2d[0]
	y = [row[0] for row in array2d]
	array2d = np.delete(array2d, (0), axis=1)
	array2d = np.delete(array2d, (0), axis=0)
	return x[1:],y[1:],array2d

x,y,data = getdata('%s' % sys.argv[1])
from scipy.interpolate import griddata
yi = np.linspace(np.min(y),np.min(y),len(y))
xi = np.linspace(np.min(x),np.min(x)+len(x))
#zi = griddata((x, y), all_msd, (xi[None,:], yi[:,None]), method='nearest')

plt.imshow(data,cmap=plt.cm.Blues) #,extent=[np.min(x),np.min(x)+len(x),np.min(y),np.max(y)]) #,aspect='equal')
plt.colorbar() 

yint = []
for val in (y):
    yint.append(int(val))

xint = []
for val in x:
    xint.append(int(val))

plt.yticks(np.arange(0,len(y)),(yint),fontsize=10)
plt.xticks(np.arange(0,len(x)),(xint), rotation=90,fontsize=10) #:np.arange(np.min(x),np.min(x)+len(x),step=1),(x))

ax1.set_xlabel('A domain')
ax1.set_ylabel('N domain')

plt.savefig('test_contact4.png', bbox_inches='tight')
