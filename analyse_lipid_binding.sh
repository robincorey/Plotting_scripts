#!/bin/bash

declare -A residue_numbers=( ["1FFT"]="1-1174" ["1NEK"]="1175-3530" ["4DJI"]="3531-4580" ["5AJI"]="4581-8352" ["5SV0"]="8353-10652" ["6B21"]="10653-11423" )

count_lipid_binding () {
echo aye
}

make_indv_ndx () {
for pdb in "${!residue_numbers[@]}"
do
	echo $pdb  a${residue_numbers[$pdb]}
	echo -e a${residue_numbers[$pdb]}'\n' q  | gmx make_ndx -f all-cg.gro -o $pdb.ndx 
	sed "s/a_${residue_numbers[$pdb]}/pdb_$pdb/g" $pdb.ndx -i
	echo -e "pdb_$pdb" '\n' q | gmx editconf -f all-cg.gro -o $pdb.stripped.pdb -n $pdb.ndx
done
}

get_posre_ndx () {
for pdb in "${!residue_numbers[@]}"
do
        start_residue=`echo ${residue_numbers[$pdb]} | cut -f1 -d"-"`
	pos_res=`tail -n 1 posre_${pdb}.itp | awk '{print $1}'`
	grep " $pos_res " Protein_${pdb}.itp | head -n 1
	pos_altered=`echo "$pos_res + $start_residue -1 " | bc`
	echo -n "$pos_altered "
done
}

lipid_binding () {
#group "CARD_&_upper" and within 0.8 of group "pdb_6B21"
echo 'group "'${1}'_&_'${3}'" and same residue as within 0.8 of group "pdb_'$2'"' > select_${1}_${2}.dat
gmx "select" -f ../md_test.pbc.short.xtc -s ../md_test.tpr -os bind_${1}_${2} -sf select_$1_$2.dat -n ../leaflets.ndx -tu ns -b 500 -seltype res_cog 
#grep -v @ ${2}_bind_${i}_redone.xvg | grep -v \# | awk '{print $2}' > ${2}_res_$1.xvg
}

plot_lipid_binding () {
sed "s/#LIPID#/${1}/g" ../PLOT_hist_blank.py > PLOT_hist_${1}_${2}_${3}.py
sed "s/#PDB#/${2}/g" -i PLOT_hist_${1}_${2}_${3}.py
python PLOT_hist_${1}_${2}_${3}.py #plot_${1}_hist.xvg
}

#make_indv_ndx
#make_lipid_ndx

for leaflet in upper lower
do
	mkdir -p ${leaflet}_leaflet
	cd ${leaflet}_leaflet
	for pdb in "${!residue_numbers[@]}"
	do
		for lipid in POPE POPG CARD
		do
			echo $pdb $lipid $leaflet
			#lipid_binding $lipid $pdb $leaflet
			plot_lipid_binding $lipid $pdb
		done
	done
	cd ..
done

#get_posre_ndx
