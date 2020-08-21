import MDAnalysis as mda
from MDAnalysis.analysis.density import DensityAnalysis

def get_dens(tpr, xtc1, xtc2, xtc3):
	u = mda.Universe(tpr, xtc1, xtc2, xtc3, continuous=False) # fitted trajectory
	ions = u.select_atoms("name KC") 
	#D = DensityAnalysis(ions, delta=1.0, gridcenter=(7.5,8,9),xdim=2,ydim=2,zdim=4)
	D = DensityAnalysis(ions, delta=1.0, padding=10)
	D.run()
	D.density.export("ions.dx", type="double")

get_dens('md_Kdp_1.fit.0.gro','md_Kdp_1.fit.xtc','md_Kdp_2.fit.xtc','md_Kdp_3.fit.xtc')
