import numpy as np
import sys
from sklearn.cluster import DBSCAN

import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

def cluster_coords(x,y,z, eps, min_samples):
	coords = np.vstack((x,y,z)).T
	db = DBSCAN(eps=eps, min_samples=min_samples).fit(coords)
	labels = db.labels_
	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	n_clusters_ = len(set(labels)) - (1 if -1 else 0)
	n_noise_ = list(labels).count(-1)
	print 'eps is %s' % eps
	print 'Estimated number of clusters: %d' % n_clusters_
	print 'Estimated number of noise points: %d' % n_noise_
	plotCluster(coords, labels, core_samples_mask, n_clusters_)
	return labels

def plot_coords(x,y,z,s):
	ax.scatter(x,y,z, color='red', s=s*10)
	plt.savefig('test_3d.png', bbox_inches='tight', dpi=300)

def plotCluster(_x, labels, core_samples_mask, n_clusters_):
	unique_labels = set(labels)
	colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
	for k, col in zip(unique_labels, colors):
		if k == -1:
			col = 'k'
		class_member_mask = (labels == k)
		xy = _x[class_member_mask & ~core_samples_mask]
		ax = plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
		markeredgecolor='k', markersize=6)
		xy = _x[class_member_mask & core_samples_mask]
		ax = plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
		markeredgecolor='k', markersize=14)
	plt.savefig('test_cluster.png')

fig = plt.figure()
ax = Axes3D(fig)

filename=sys.argv[1]
#coords = np.genfromtxt(fname=filename, usecols=(5,6,7), unpack=True, skip_header=2, skip_footer=2)
x = np.genfromtxt(fname=filename, usecols=(5), unpack=True, skip_header=2, skip_footer=2)
y = np.genfromtxt(fname=filename, usecols=(6), unpack=True, skip_header=2, skip_footer=2)
z = np.genfromtxt(fname=filename, usecols=(7), unpack=True, skip_header=2, skip_footer=2)
s = np.genfromtxt(fname=filename, usecols=(9), unpack=True, skip_header=2, skip_footer=2)
plot_coords(x,y,z,s)
cluster_coords(x,y,z, 25, 3)
#plot_cluster(x,y,z,s)
#labels = db.labels_
#from collections import Counter
#Counter(labels)
