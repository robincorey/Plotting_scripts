import sys 
import MDAnalysis as mda
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from MDAnalysis.analysis import diffusionmap, align

# load in trajectorty data
U = mda.Universe(sys.argv[1],sys.argv[2])

# align trajectory based on CA
align_rms = align.AlignTraj(U,U,select='name CA',in_memory=True).run()

# create RMSD matrix for pairwise frames
matrix = diffusionmap.DistanceMatrix(U,select='name CA').run()
matrix.dist_matrix.shape

# plot
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111)
im = plt.imshow(matrix.dist_matrix, origin='lower', cmap='rainbow')
#plt.colorbar(im, cmap='rainbow', ax=ax, label='RMSD ($\AA$)', pad=0.2, size=)
plt.xticks(np.arange(0, len(U.trajectory)+1, step=(len(U.trajectory)/5)))
plt.yticks(np.arange(0, len(U.trajectory)+1, step=(len(U.trajectory)/5)))
plt.xlabel('frame')
plt.ylabel('frame')
divider = make_axes_locatable(ax)
cb_ax = divider.append_axes("right", size="5%", pad=0.2)
plt.colorbar(im, cmap='rainbow', ax=ax, label='RMSD ($\AA$)', cax=cb_ax)
plt.savefig('2D-rmsd.png',bbox_inches='tight', dpi=900)
