#!/home/birac/anaconda2/bin/python
#
# python script to plot any Gromacsdata file
# 

##########################
##
#####  Version control ####
##
# original made Aug-2016
# Updated for \t Sept-210
# Updated Legends Sept-2016
# Improved legends for no legen containing grarhs \t Sept-2016
#
##########################

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


def loaddata ( str ):
        print "%s" % y
	return

filename = sys.argv[1]
file = open('%s' % filename, 'r')
for line in file:
        if re.search(" xaxis ", line):
                xlabelpre =  line.split()[3]
                xlabel = xlabelpre.replace('"','')
                print 'x-axis = %s' % xlabel
	if re.search(" yaxis ", line):
                ylabelpre =  line.split()[3]
                ylabel = ylabelpre.replace('"','')
                print 'y-axis = %s' % ylabel

if 'xlabel' not in locals():			## test for existence of variable
                print "X axis name?"
                prompt = '> '
                xlabel = raw_input(prompt)
if 'ylabel' not in locals():
                print "Y axis name?"
                prompt = '> '
                ylabel = raw_input(prompt)

## Get legends 

## Find number of columns
if "legend" in open(filename).read():
	legend = "yes"
	leg_num = subprocess.check_output("grep -c s[0-9] '%s'" % filename, shell=True)
	leg_num2 = int(leg_num)
	## Define array for legends
	leg = ["X-axis"]
	for x in range(0, leg_num2):
		test = subprocess.check_output("grep s'%s' '%s'" % (x, filename), shell=True)
		f = open('test.txt', 'w')
		f.write( test )
		f.close()	
		test2 = subprocess.check_output("cat %s | awk '{print $4 $5}'" % 'test.txt', shell=True)
		test3 = test2.rstrip()
		leg.append('%s' % test3)
		print "legends will be %s" % leg
else:
	legend = "no"
	print "no legend information available"

os.system("rm tempdata")
os.system("egrep -v '\#|\@' %s > tempdata" % filename)  # copy data into temp file

## Ropey homemade csv creator, suitable for only certain files.
os.system("sed 's/^\(                \|               \|              \|             \|            \|            \|           \|           \|        \|         \|        \|        \|       \|      \|     \|    \|   \|  \| \)//g' tempdata -i")
os.system("sed 's/\(                \|               \|              \|             \|            \|            \|           \|           \|        \|         \|        \|        \|       \|      \|     \|    \|   \|  \| \)$//g' tempdata -i")
os.system("sed 's/\(                \|               \|              \|             \|            \|            \|           \|           \|        \|         \|        \|        \|       \|      \|     \|    \|   \|  \)/,/g' tempdata -i")
os.system("sed 's/,,,,/,/g' tempdata -i")
os.system("sed 's/,,,/,/g' tempdata -i")
os.system("sed 's/,,/,/g' tempdata -i")
##
# For other files
os.system("sed 's/\t/,/g' tempdata -i")

with open('tempdata', 'rb') as csvfile:			# get col number
	reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
	first_row = next(reader)
	num_cols = len(first_row)
	print 'Total number of columns = %s' % num_cols
	if num_cols == 0:
		print "No data!"
		sys.exit(0)
	if num_cols == 1:
		xdata = np.loadtxt(fname='tempdata', usecols=(0,), unpack=True)	
	if num_cols == 2:
		xdata, ydata = np.loadtxt(fname='tempdata', delimiter=',', usecols=(0, 1), unpack=True)
	if num_cols > 2:
		print "All columns? y/n "
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
			if num_cols == 3:
				xdata, ydata, ydata2 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)			
			if num_cols == 4:
                                xdata, ydata, ydata2, ydata3 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
			if num_cols == 5:
                                xdata, ydata, ydata2, ydata3, ydata4 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols == 6:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols == 7:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols == 8:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6, ydata7 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols == 9:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6, ydata7, ydata8 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols == 10:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6, ydata7, ydata8, ydata9 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
                        if num_cols == 11:
                                xdata, ydata, ydata2, ydata3, ydata4, ydata5, ydata6, ydata7, ydata8, ydata9, ydata10 = np.loadtxt(fname='tempdata', delimiter=',', unpack=True)
						
##########
# Plotting data
##########

plt.title('%s' % filename )
colors = cm.rainbow(np.linspace(0, 1, num_cols))
if num_cols == 1:
	plt.plot(xdata, color='blue', marker='.', markersize=2)
# Think this section isn't needed anymore
'''
if num_cols == 2:
        plt.plot(xdata, ydata, color='blue', marker='.', markersize=2)
if num_cols == 3:
        plt.plot(xdata, ydata, ydata2, color='blue', marker='.', markersize=2)
if num_cols == 4:
	plt.plot(xdata, ydata, ydata2, ydata3, color='blue', marker='.', markersize=2)
if num_cols == 5:
	plt.plot(xdata, ydata, ydata2, ydata3, ydata4, color='blue', marker='.', markersize=2)
'''
if num_cols > 1 and colprompt1 is not 'n':
	for x in range(1, num_cols):	
		x2 = int(x)
		xdata, ydata = np.loadtxt(fname='tempdata', delimiter=',', usecols=(0, x2), unpack=True)
		if legend == "yes":
			plt.plot(xdata, ydata, color=colors[x2], marker='.', markersize=2, label=leg[x])
			plt.legend()
		else:
			plt.plot(xdata, ydata, color=colors[x2], marker='.', markersize=2)
elif num_cols > 1 and colprompt1 is 'n':
	xdata, ydata = np.loadtxt(fname='tempdata', delimiter=',', usecols=(colxint, colyint), unpack=True)	
        if legend == "yes":	
		plt.plot(xdata, ydata, color=colors[colyint], marker='.', markersize=2, label=leg[colyint])
		plt.legend()
	else: 
		plt.plot(xdata, ydata, color=colors[colyint], marker='.', markersize=2)
plt.xlabel('%s' % xlabel )
plt.ylabel('%s' % ylabel )
#plt.xlim(0, 50)
plt.savefig('%s.png' % filename )
plt.show ()
