import sys
import MDAnalysis as mda
import numpy as np

u = mda.Universe(sys.argv[1], sys.argv[2])

f = open("%s" % sys.argv[4], "w")
for i in np.arange(60):
	CLA = u.select_atoms("%s and cylayer %d %d 45 -45 protein" % (sys.argv[3], i , (i+1)))
	print('%s' % (len(CLA)))
