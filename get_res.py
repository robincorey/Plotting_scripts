import sys
import numpy as np
import os
import re
import pandas as pd

res = sys.argv[1]

print(res)

for lig in ['ligand','noligand']:
	values = []
	for i in np.arange(1,4):
		file = open('%s.%s.xvg' % (lig, i), 'r')
		for line in file:
			if re.search(' %s ' % res, line):
				newline = line.strip().replace(res,' ').strip()
				#newline = print(line.strip().replace(res,' '))
				values.append(float(newline.strip()))	
	print('%s %5.2f %5.2f' % (lig, np.mean(values), np.std(values)))
