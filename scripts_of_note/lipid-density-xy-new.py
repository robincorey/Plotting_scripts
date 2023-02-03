import matplotlib as mpl
mpl.use('Agg')
import sys
import MDAnalysis as mda
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import *
import pylab
import plumed
import os
import seaborn as sb
import glob
import copy
from scipy.stats import gaussian_kde
mpl.rcParams['agg.path.chunksize'] = 10000


##Need to have plumed files saved as LIPID_POS_X, LIPID_POS_Y etc in the folder you run this in
##As well as BB_POS_X etc for the backbond trace

def plot_lipid_density(lipid,label,cmap,xmin,xmax,ymin,ymax):
	coords = []
	##load in plumed files
	LIP_POS_X=plumed.read_as_pandas("{}_POS_X".format(lipid))
	LIP_POS_Y=plumed.read_as_pandas("{}_POS_Y".format(lipid))
	xcoords_BB = plumed.read_as_pandas("BB_POS_X")
	ycoords_BB = plumed.read_as_pandas("BB_POS_Y")
	##This is for LIP and stack data
	xcoords_LIP = LIP_POS_X.drop(columns="time")
	xcoords_LIP = xcoords_LIP.stack().reset_index(drop=True)
	print(xcoords_LIP)
	ycoords_LIP = LIP_POS_Y.drop(columns="time")
	ycoords_LIP = ycoords_LIP.stack().reset_index(drop=True)
	##This is for BB and stack data
	xcoords_BB = xcoords_BB.drop(columns="time")
	xcoords_BB = xcoords_BB.stack().reset_index(drop=True)
	ycoords_BB = ycoords_BB.drop(columns="time")
	ycoords_BB = ycoords_BB.stack().reset_index(drop=True)
	# #coordinates 
	x_min=xmin
	y_min=ymin
	x_max=xmax
	y_max=ymax
	# rescale coordinates to angstroms
	xcoords_LIP = xcoords_LIP * 10
	ycoords_LIP = ycoords_LIP * 10
	xcoords_BB = xcoords_BB * 10
	ycoords_BB = ycoords_BB * 10
	# Inverse for figure plotting
	# xcoords_LIP = -xcoords_LIP
	# ycoords_LIP = -ycoords_LIP
	# xcoords_BB = -xcoords_BB
	# ycoords_BB = -ycoords_BB
	#print(xcoords_LIP)
	#General plotting settings
	matplotlib.rcParams.update({'font.size': 40})
	bins=30
	fig = plt.figure(figsize=(15,15))
	ax = fig.add_subplot(111)
	plt.ylabel("y ($\AA$)")#, fontsize=50)
	plt.xlabel("x ($\AA$)")#, fontsize=50)
	#The ticks will need to be modified to look nice with the xmax/ymax
	ticks_x = int((x_max-x_min)/6)
	ticks_y = int((y_max-y_min)/6)
	# definition of axes for the graph
	ax.set_xlim([x_min,x_max])
	ax.set_ylim([y_min,y_max])
	ax.set_aspect('equal')
	##Plotting
	array_op,xedges,yedges = np.histogram2d(xcoords_LIP,ycoords_LIP, bins=bins,range=[[x_min,x_max],[y_min,y_max]])
	max_array=max(array_op.flatten())
	array_avg = array_op/max_array
	extent = [xedges[0], xedges[-1], yedges[0], yedges[-1] ]
	# interesting interpolation: bicubic, lanczos see http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
	cax= ax.imshow(array_avg.T,extent=extent,interpolation='bicubic',origin='lower',cmap=cmap)
	plt.colorbar(cax)
	ax.set_xticks(np.arange(x_min,x_max,ticks_x))
	ax.set_yticks(np.arange(y_min,y_max,ticks_y))
	# ax.set_xticklabels([-45,-30,-15,0,15,30])
	# ax.set_yticklabels([-45,-30,-15,0,15,30])
	##The below line for just a normal BB plot 
	#change values depending on size of filament, miss last unit to not get lines across plot
	plt.plot(xcoords_BB,ycoords_BB, lw=2, c="white", alpha=0.8)
	#plt.plot(xcoords_BB[100:2800],ycoords_BB[100:2800], lw=2, c="white", alpha=0.8)
	##Saving figure
	ax.set_title('{}'.format(label),fontsize=60)
	plt.savefig('{}-xy.png'.format(lipid), format='png', dpi=300)

def plot_lipid_density_yz(lipid,label,cmap,ymin,ymax,zmin,zmax):
	coords = []
	##load in plumed files
	LIP_POS_Y=plumed.read_as_pandas("{}_POS_Y".format(lipid))
	LIP_POS_Z=plumed.read_as_pandas("{}_POS_Z".format(lipid))
	ycoords_BB = plumed.read_as_pandas("BB_POS_Y")
	zcoords_BB = plumed.read_as_pandas("BB_POS_Z")
	##This is for LIP and stack data
	ycoords_LIP = LIP_POS_Y.drop(columns="time")
	ycoords_LIP = ycoords_LIP.stack().reset_index(drop=True)
	zcoords_LIP = LIP_POS_Z.drop(columns="time")
	zcoords_LIP = zcoords_LIP.stack().reset_index(drop=True)
	##This is for BB and stack data
	ycoords_BB = ycoords_BB.drop(columns="time")
	ycoords_BB = ycoords_BB.stack().reset_index(drop=True)
	zcoords_BB = zcoords_BB.drop(columns="time")
	zcoords_BB = zcoords_BB.stack().reset_index(drop=True)
	# #coordinates 
	y_min=ymin
	z_min=zmin
	y_max=ymax
	z_max=zmax
	# rescale coordinates to angstroms
	ycoords_LIP = ycoords_LIP * 10
	zcoords_LIP = zcoords_LIP * 10
	ycoords_BB = ycoords_BB * 10
	zcoords_BB = zcoords_BB * 10
	# Inverse for figure plotting
	# xcoords_LIP = -xcoords_LIP
	# ycoords_LIP = -ycoords_LIP
	# xcoords_BB = -xcoords_BB
	# ycoords_BB = -ycoords_BB
	print(ycoords_LIP)
	#General plotting settings
	matplotlib.rcParams.update({'font.size': 40})
	bins=30
	fig = plt.figure(figsize=(15,15))
	ax = fig.add_subplot(111)
	plt.ylabel("z ($\AA$)")#, fontsize=50)
	plt.xlabel("y ($\AA$)")#, fontsize=50)
	#The ticks will need to be modified to look nice with the xmax/ymax
	ticks_x = int((y_max-y_min)/6)
	ticks_y = int((z_max-z_min)/4)
	# definition of axes for the graph
	ax.set_xlim([y_min,y_max])
	ax.set_ylim([z_min,z_max])
	ax.set_aspect('equal')
	##Plotting
	array_op,xedges,yedges = np.histogram2d(ycoords_LIP,zcoords_LIP, bins=bins,range=[[y_min,y_max],[z_min,z_max]])
	max_array=max(array_op.flatten())
	array_avg = array_op/max_array
	extent = [xedges[0], xedges[-1], yedges[0], yedges[-1] ]
	# interesting interpolation: bicubic, lanczos see http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
	cax= ax.imshow(array_avg.T,extent=extent,interpolation='bicubic',origin='lower',cmap=cmap)
	plt.colorbar(cax)
	ax.set_xticks(np.arange(y_min,y_max,ticks_x))
	ax.set_yticks(np.arange(z_min,z_max,ticks_y))
	# ax.set_xticklabels([-45,-30,-15,0,15,30])
	# ax.set_yticklabels([-45,-30,-15,0,15,30])
	##The below line for just a normal BB plot
	#plt.plot(ycoords_BB[100:6200],zcoords_BB[100:6200], lw=2, c="white", alpha=0.8)
	##Saving figure
	ax.set_title('{}'.format(label),fontsize=60)
	plt.savefig('{}-yz.png'.format(lipid), format='png', dpi=300)

def plot_lipid_density_xz(lipid,label,cmap,xmin,xmax,zmin,zmax):
	coords = []
	##load in plumed files
	LIP_POS_X=plumed.read_as_pandas("{}_POS_X".format(lipid))
	LIP_POS_Z=plumed.read_as_pandas("{}_POS_Z".format(lipid))
	xcoords_BB = plumed.read_as_pandas("BB_POS_X")
	zcoords_BB = plumed.read_as_pandas("BB_POS_Z")
	##This is for LIP and stack data
	xcoords_LIP = LIP_POS_X.drop(columns="time")
	xcoords_LIP = xcoords_LIP.stack().reset_index(drop=True)
	zcoords_LIP = LIP_POS_Z.drop(columns="time")
	zcoords_LIP = zcoords_LIP.stack().reset_index(drop=True)
	##This is for BB and stack data
	xcoords_BB = xcoords_BB.drop(columns="time")
	xcoords_BB = xcoords_BB.stack().reset_index(drop=True)
	zcoords_BB = zcoords_BB.drop(columns="time")
	zcoords_BB = zcoords_BB.stack().reset_index(drop=True)
	# #coordinates 
	x_min=xmin
	z_min=zmin
	x_max=xmax
	z_max=zmax
	# rescale coordinates to angstroms
	xcoords_LIP = xcoords_LIP * 10
	zcoords_LIP = zcoords_LIP * 10
	xcoords_BB = xcoords_BB * 10
	zcoords_BB = zcoords_BB * 10
	# Inverse for figure plotting
	# xcoords_LIP = -xcoords_LIP
	# ycoords_LIP = -ycoords_LIP
	# xcoords_BB = -xcoords_BB
	# ycoords_BB = -ycoords_BB
	#print(xcoords_LIP)
	#General plotting settings
	matplotlib.rcParams.update({'font.size': 40})
	bins=30
	fig = plt.figure(figsize=(15,15))
	ax = fig.add_subplot(111)
	plt.ylabel("z ($\AA$)")#, fontsize=50)
	plt.xlabel("x ($\AA$)")#, fontsize=50)
	#The ticks will need to be modified to look nice with the xmax/ymax
	ticks_x = int((x_max-x_min)/6)
	ticks_y = int((z_max-z_min)/4)
	# definition of axes for the graph
	ax.set_xlim([x_min,x_max])
	ax.set_ylim([z_min,z_max])
	ax.set_aspect('equal')
	##Plotting
	array_op,xedges,yedges = np.histogram2d(xcoords_LIP,zcoords_LIP, bins=bins,range=[[x_min,x_max],[z_min,z_max]])
	max_array=max(array_op.flatten())
	array_avg = array_op/max_array
	extent = [xedges[0], xedges[-1], yedges[0], yedges[-1] ]
	# interesting interpolation: bicubic, lanczos see http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
	cax= ax.imshow(array_avg.T,extent=extent,interpolation='bicubic',origin='lower',cmap=cmap)
	plt.colorbar(cax)
	ax.set_xticks(np.arange(x_min,x_max,ticks_x))
	ax.set_yticks(np.arange(z_min,z_max,ticks_y))
	# ax.set_xticklabels([-45,-30,-15,0,15,30])
	# ax.set_yticklabels([-45,-30,-15,0,15,30])
	##The below line for just a normal BB plot
	#plt.plot(xcoords_BB[100:6200],zcoords_BB[100:6200], lw=2, c="white", alpha=0.8)
	##Saving figure
	ax.set_title('{}'.format(label),fontsize=60)
	plt.savefig('{}-xz.png'.format(lipid), format='png', dpi=300)

plot_lipid_density(sys.argv[1],sys.argv[1],'RdPu',0,200,0,380)
plot_lipid_density_yz(sys.argv[1],sys.argv[1],'RdPu',0,380,0,170)
plot_lipid_density_xz(sys.argv[1],sys.argv[1],'RdPu',0,200,0,170)
