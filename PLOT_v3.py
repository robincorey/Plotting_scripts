#!/home/birac/anaconda2/bin/python
#
# python script to plot any Gromacsdata file
# 

### Version control

# original made Aug-2016
# Updated for \t Sept-210
# Updated Legends Sept-2016
# Improved legends Jan-2017. Now added prompt
# Improved CSV Feb-2017.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import curve_fit
from scipy import optimize
import os
import re
import sys
import csv
import shutil
import pandas as pd
import subprocess
import os.path

def loaddata ( str ):
        print "%s" % y
	return

filename = sys.argv[1]
file = open('%s' % filename, 'r')

## Check for X and Y axis names (Gromacs format)
## If none, prompt for manual import

for line in file:
        if re.search("xaxis", line):
                xlabelpre =  line.split()[3]
                xlabel = xlabelpre.replace('"','')
                print 'x-axis = %s' % xlabel
	if re.search("yaxis", line):
                ylabelpre =  line.split()[3]
                ylabel = ylabelpre.replace('"','')
                print 'y-axis = %s' % ylabel

if 'xlabel' not in locals():	## test for existence of variable
                print "X axis name?"
                prompt = '> '
                xlabel = raw_input(prompt)
if 'ylabel' not in locals():
                print "Y axis name?"
                prompt = '> '
                ylabel = raw_input(prompt)

if os.path.exists("tempdata"):
	os.remove("tempdata")

if os.path.exists("tempdata.all"):
        os.remove("tempdata.all")

os.system("egrep -v '\#|\@' %s > tempdata" % filename)  # copy data into temp file

with open('tempdata', 'rb') as csvfile:			# get col number
	#reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
	#first_row = next(reader)
	#num_cols2= len(first_row)
	num_cols = subprocess.check_output("cat '%s' | awk -F ',' '{print NF}' | head -n 1" % 'tempdata', shell=True)
	num_cols2 = int(num_cols)
	nc2 = num_cols2 - 1
	nc3 = num_cols2 + 1
	print 'Number of data columns = %s' % nc2
	#improved CV converter here!
	for x in range(1, nc3 ):
		#print '%s' % x
		os.system("awk -F ',' '{print $'%s'}' '%s' > '%s'.'%s'" % ( x , 'tempdata' , x , 'tempdata'))
	os.system("paste -d ',' *.tempdata > tempdata.all")
	## Get legends 
	## Define array for legends
	leg = ["X-axis"]
	for x in range(0, nc2):
		# first, check for Gromacs-style legends
        	if 's0' in open('%s' % filename).read():
			test = subprocess.check_output("grep s'%s' '%s'" % (x, filename), shell=True)
        		f = open('test.txt', 'w')
        		f.write( test )
        		f.close()
        		test2 = subprocess.check_output("cat %s | awk '{print $4 $5}'" % 'test.txt', shell=True)
        		test3 = test2.rstrip()
        		leg.append('%s' % test3)
		# if none, prompt for manual
		else:
			print "Legend for column %s" % x
			prompt = '> '
			legend = raw_input(prompt)
			leg.append('%s' % legend)
		print "legends will be %s" % leg
	# read data
	if num_cols2 == 0:
		print "No data!"
		sys.exit(0)
	if num_cols2 == 1:
		xdata = np.loadtxt(fname='tempdata', usecols=(0,), unpack=True)	
	if num_cols2 == 2:
		xdata, ydata = np.loadtxt(fname='tempdata', delimiter=',', usecols=(0, 1), unpack=True)
	if num_cols2 > 2:
		print "Print all columns? y/n "
		prompt = '> '
		colprompt1 = raw_input(prompt)
		if colprompt1 is 'n':
			print "which column for X? (only one; first column=0)"
			prompt = '> '
			colx = raw_input(prompt)
			colxint = int(colx)
                        print "which column for Y?"
			prompt = '> '
                        coly = raw_input(prompt)
                        colyint = int(coly)
			#xdata, ydata = np.loadtxt(fname='tempdata', delimiter=',', usecols=(colxint, colyint), unpack=True)
		else:
			if num_cols2 == 3:
				xdata, ydata, ydata2 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)			
			if num_cols2 == 4:
                                xdata, ydata, ydata2, ydata3 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
			if num_cols2 == 5:
                                xdata, ydata, ydata2, ydata3, ydata4 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols2 == 6:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols2 == 7:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols2 == 8:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6, ydata7 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols2 == 9:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6, ydata7, ydata8 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols2 == 10:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6, ydata7, ydata8, ydata9 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols2 == 11:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6, ydata7, ydata8, ydata9, ydata10 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
						
##########
# Plotting data
##########

plt.title('%s' % filename )
colors = cm.rainbow(np.linspace(0, 1, num_cols ))
if num_cols2== 1:
	plt.plot(xdata, color='blue', marker='.', markersize=2)
if num_cols2> 1 and colprompt1 is not 'n':
	for x in range( 1, num_cols2 ):	
		x2 = int(x)
		xdata, ydata = np.loadtxt(fname='tempdata', delimiter=',', usecols=(0, x2), unpack=True)
		plt.plot(xdata, ydata, color=colors[x2], marker='.', markersize=2, label=leg[x])
elif num_cols2 > 1 and colprompt1 is 'n':
	xdata, ydata = np.loadtxt(fname='tempdata', delimiter=',', usecols=(colxint, colyint), unpack=True)	
	plt.plot(xdata, ydata, color=colors[colyint], marker='.', markersize=2, label=leg[colyint])
plt.xlabel('%s' % xlabel )
plt.ylabel('%s' % ylabel )
plt.legend()
#plt.xlim(0, 50)
plt.savefig('%s.png' % filename )
plt.show ()
