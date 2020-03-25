import glob
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

file_list = glob.glob('*.rmsf.xvg')

data = []
for f in file_list:
	data.append(np.loadtxt(f, usecols=1))
	res = np.loadtxt(f, usecols=0)

arr = np.vstack(data)

#plt.plot(res, np.mean(arr, axis=0), color='red', linewidth=3)
#plt.fill_between(res, np.mean(arr, axis=0)-np.std(arr, axis=0), np.mean(arr, axis=0)+np.std(arr, axis=0), alpha=0.3, facecolor='gray')
plt.errorbar(res, np.mean(arr, axis=0), color='#0033cc', marker='.', markersize=1, yerr=np.std(arr, axis=0), ecolor='#99b3ff', fmt='o', capthick=0 )
plt.xlabel('residue', fontsize=15 )
plt.ylabel('RMSF (nm)', fontsize=15 )
plt.savefig('test.png')
#plt.plot(xdata-x_min, ydata-bulk-yerr1, color='gray', linewidth=0.5)
#plt.plot(xdata-x_min, ydata-bulk+yerr1, color='gray', linewidth=0.5)

#plt.plot(np.mean(arr, axis=0),np.std(arr, axis=0)
#print np.mean(arr, axis=0) #np.std(arr, axis=0)


