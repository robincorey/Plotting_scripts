# Simple script for plotting a gmx xvg with an unknown number of columns
# Comments should be removed from xvg ahead of time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

# pandas only allows one comment, so # need to be removed manually
df = pd.read_csv(sys.argv[1], sep="\t", on_bad_lines='skip', comment='@', header=None)

# define cmap
cmap = cm.get_cmap('rainbow_r', len(df. columns))

# get centre
centre = (df.mean(axis=1)[0])

#loop through columns and plot
for col in np.arange(1,len(df. columns)):
    plt.plot(df.iloc[:,0]/1e6, df.iloc[:,col]-centre, c=cmap(col), linewidth=1)

mu = u'\u03bc'
plt.xlabel('time (%ss)' % mu, fontsize=16)
plt.ylabel('PO4 z position (nm)', fontsize=16)
plt.xticks(np.arange(0,16,step=5))
plt.xlim(0,15)
plt.yticks(np.arange(-4,5,step=2))
plt.ylim(-4,4)
plt.savefig('Figs/%s.png' % sys.argv[2] , bbox_inches='tight')
