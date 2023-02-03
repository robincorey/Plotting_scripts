#!/bin/bash

## run all of the scripts needed to make lipid density plots 
#takes input $1 number of repeats
## if not working try source /.bashrc before running

GIT=/sansom/s137/bioc1535/Desktop/git-repos/Plotting_scripts/scripts_of_note/

module load ubuntu-18/plumed/2.5.0

mkdir -p DENS

echo -e aBB '\n' q | gmx make_ndx -f md_1.tpr -o BB.ndx

for lipid in POPE BB CARD POPG
do 
	echo $lipid | gmx editconf -f md_1.gro -o md-centre-$lipid.pre.pdb -n  BB.ndx
	echo $lipid | gmx editconf -f md-centre-$lipid.pre.pdb -o md-centre-$lipid.pdb
	for i in $(seq 1 $1)
	do 
		echo "Processing md $i"
		echo -e BB '\n' System | gmx trjconv -f md_$i.xtc -s md_$i.tpr -center -o DENS/centre.$lipid.$i.xtc -n BB.ndx -skip 10 -pbc mol
		echo -e BB '\n' $lipid | gmx trjconv -f DENS/centre.$lipid.$i.xtc -s md_$i.tpr -fit rotxy+transxy -n BB.ndx -o DENS/$lipid.$i.xtc
	done
	gmx trjcat -f DENS/$lipid.*.xtc -o DENS/all.$lipid.xtc -cat
	$GIT/make_plumed_script2.sh $lipid > DENS/${lipid}_plumed_coordinates.sh
	sed -i "s/PRINT ,pos/PRINT ARG=pos/g" DENS/${lipid}_plumed_coordinates.sh
	plumed driver --mf_xtc DENS/all.$lipid.xtc --plumed DENS/${lipid}_plumed_coordinates.sh
done

for lipid in POPE CARD POPG
do
	python $GIT/lipid-density-xy-new.py $lipid
done

rm ./bck*
rm ./*#*
rm -f DENS/*#*
