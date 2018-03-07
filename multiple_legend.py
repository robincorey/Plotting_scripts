#!/sansom/s137/bioc1535/anaconda2/bin/python

import matplotlib.patches as mpatches
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

legend_dict = { 'data1' : 'green', 'data2' : 'red', 'data3' : 'blue' }
patchList = []
for key in legend_dict:
	data_key = mpatches.Patch(color=legend_dict[key], label=key)
	patchList.append(data_key)

plt.legend(handles=sorted(patchList))
plt.savefig('legend.png', bbox_inches='tight')
