import numpy as np
import csv

with open('ion_occs/ION_OCC_1') as f:
	reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
	first_row = next(reader)
	second_row = next(reader)
	num_cols = len(second_row)
	print(num_cols)


def plot(col,rep):
	data = np.loadtxt(fname='ion_occs/ION_OCC_%s' % rep, usecols=(col), skiprows=1,unpack=True)
	return np.mean(data)

for col in np.arange(1,num_cols):
		avs = []
		for rep in [1,2,3]:
			av = plot(col,rep)
			avs.append(av)
		print('%s %.2f ± %.2f' % ( col, np.mean(avs), np.std(avs)))
