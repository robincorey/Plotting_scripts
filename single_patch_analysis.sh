#!/bin/bash

lipid_binding () {
echo 'group "'${1}'_'${3}'" and same residue as within 0.8 of group Protein' > select_${1}_${2}.dat
gmx "select" -f ../md_${2}_${4}.xtc -s ../md_${2}_${4}.tpr -os bind_${1}_${2}_${4} -sf select_${1}_${2}.dat -n ../${2}_leaflets.ndx -tu ns -b 500 -seltype res_cog 
}

lipid_quant () {
av=`awk '{sum+=$2} END {print sum/NR}' bind_${1}_${2}_${3}.xvg`
echo ${1} ${2} ${3} $av  
}


for leaflet in lower upper
do
	mkdir -p binding_data
	rm -f binding_data/${leaflet}_binding*.txt
	mkdir -p ${leaflet}_leaflet
	cd ${leaflet}_leaflet
	for pdb in 6B21 1NEK 5AJI 4DJI 5SV0 1FFT 
	do
	echo $pdb 
		for lipid in POPE POPG CARD
		do	
		#	lipid_binding $lipid $pdb $leaflet $num
			for num in 1 2 3
			do
				lipid_binding $lipid $pdb $leaflet $num
				lipid_quant  $lipid $pdb $num >> ../binding_data/${leaflet}_binding_${pdb}_$lipid.txt
			done
		done
	done
	cd ..
done
