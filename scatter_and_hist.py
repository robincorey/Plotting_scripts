import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import os
import sys

left, width = 0.1, 0.9
bottom, height = 0.1, 1.0
spacing = 0

rect_scatter = [left, bottom, width, height]
rect_histy = [left + width + spacing, bottom, 0.2, height]
fig = plt.figure(figsize=(6, 4))

ax = fig.add_axes(rect_scatter)
ax_histy = fig.add_axes(rect_histy) #, sharey=ax)

all_data = []

def plot_function (num,rep):
        global all_data
        x,y = np.loadtxt(fname='MD_%s_%s.xvg' % (num,rep),usecols=(0,1),comments=['#','@'],unpack=True)
        ax.plot(x/1000, y, color='gray', linewidth=1,alpha=0.1)
        all_data = np.append(all_data,y)

for num in np.arange(0,30,step=2):
        for rep in np.arange(1,25):
                plot_function(num,rep)

n,bins,patches = ax_histy.hist(all_data,density=True,bins=50, orientation='horizontal',color='red',histtype='stepfilled')
unbound = len([i for i in all_data if i > 0.7])
bound = len([i for i in all_data if i < 0.7])
print '%.3f %% of frames are bound' % ((float(bound)/(float(bound)+float(unbound))*100))
#ax_histy.set_xticks(np.arange(0,np.max(n)+1,step=np.max(n)))
ax.set_ylim(0,np.max(all_data))
ax.set_yticks(np.arange(0,np.max(all_data),step=0.2))
ax_histy.set_xticks([],[])
ax_histy.set_yticks([],[])
ax.set_ylabel("CDL-prot mindist (nm)", fontsize=20) #, position=(0,1.5) )
ax.set_xlabel("time (ns)", fontsize=20)
fig.savefig('mindist.png', bbox_inches='tight')
