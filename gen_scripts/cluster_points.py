import numpy as np
import sys
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

def cluster_coords(x,y,z, eps, min_samples, res, resid):
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
	#print "Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels)
	#print "Completeness: %0.3f" % metrics.completeness_score(labels_true, labels)
	#print "V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels)
	#print "Adjusted Rand Index: %0.3f"
	#      % metrics.adjusted_rand_score(labels_true, labels)
	#print "Adjusted Mutual Information: %0.3f"
	#      % metrics.adjusted_mutual_info_score(labels_true, labels,
        #                                   average_method='arithmetic')
	#print("Silhouette Coefficient: %0.3f"
      #% metrics.silhouette_score(X, labels))
	plotCluster(coords, labels, core_samples_mask, n_clusters_)
	labelGraph(x, y, res, resid)
	return labels

def plot_coords(x,y,z,s):
	ax.scatter(x,y,z, color='red', s=s*10)
	plt.savefig('test_3d.png', bbox_inches='tight', dpi=300)

def plotCluster(_x, labels, core_samples_mask, n_clusters_):
	unique_labels = set(labels) # unique labels = cluster ID
	colors = plt.cm.RdYlBu(np.linspace(0, 1, len(unique_labels)))
	for k, col in zip(unique_labels, colors):
		if k == -1:
			col = 'dimgray'
		class_member_mask = (labels == k)
		xy = _x[class_member_mask & ~core_samples_mask]
		ax = plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='w', markersize=6)
		xy = _x[class_member_mask & core_samples_mask]
		ax = plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='w', markersize=14)
	plt.savefig('test_cluster.png')

def labelGraph(x, y , res, resid):
	#for i in range(len(a)):
	for num in range(len(res)):
		resnum = int(res[num])
		ax = plt.text(x[num],y[num],'%s %s' % (resid[num], resnum))
	plt.savefig('test_cluster_label.png')

fig = plt.figure()
#ax = Axes3D(fig)

ax = fig.add_subplot(111)

filename=sys.argv[1]
x, y, z, s, res  = np.genfromtxt(fname=filename, usecols=(5, 6, 5, 8, 4), unpack=True, skip_header=2, skip_footer=2)
resid = np.genfromtxt(fname=filename, usecols=(3), unpack=True, skip_header=2, skip_footer=2, dtype=None)
cluster_coords(x,y,z, 10, 3, res, resid)
