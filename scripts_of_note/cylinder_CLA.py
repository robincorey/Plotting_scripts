import sys
import MDAnalysis as mda
import numpy as np

u = mda.Universe(sys.argv[1], sys.argv[2])

f = open("CLA_%s.txt" % sys.argv[3], "w")
for ts in u.trajectory[1000:len(u.trajectory):100]:
	for i in np.arange(60):
		CLA = u.select_atoms("resname CLA and cylayer %d %d 45 -45 protein" % ( i , (i+1)))
		f.write('%s,' % (len(CLA)))
	f.write('\n')
