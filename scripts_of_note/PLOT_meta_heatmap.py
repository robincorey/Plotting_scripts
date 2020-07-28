import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

filename = 'fes.dat'
file = open('%s' % filename, 'r')
xdata, ydata, zdata = np.loadtxt(fname='%s' %filename, comments='#', usecols=(0,1,2), unpack=True)
xlabel = "d1 (nm)"
ylabel = "d2 (nm)"

# Sort the points by density, so that the densest points are plotted last
plt.xlabel('%s' % xlabel, fontname="cmss10", fontsize=15 )
plt.ylabel('%s' % ylabel, fontname="cmss10", fontsize=15 )
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xdata, ydata, zdata) ##, s=30, edgecolor='')
plt.colorbar()
plt.savefig('%s.png' % filename )
plt.show ()
