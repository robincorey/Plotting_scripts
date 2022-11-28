#!/bin/bash

mkdir -p bind

do_mindist () {
# find distance between selected TMs for all frames
echo -e r_$res '\n' r_$res2 | gmx mindist -f md_TLR2_$i.pbc -s md_TLR2_$i -n TMs -o bind/$res.$res2.$i -od bind/$res.$res2.$i
} 

frames () {
# use mindist to select frames of interest, and write to xtc
echo -e '"'r_$res'"' '|' '"'r_$res2'"' '\n' q | gmx make_ndx -f md_TLR2_$i -n TMs -o bind/$res.$res2.$i.ndx
echo "r_${res}_r_${res2}" | gmx trjconv -f md_TLR2_$i.pbc -s md_TLR2_$i -drop bind/$res.$res2.$i.xvg -dropover 0.6 -o bind/$res.$res2.$i.xtc -n bind/$res.$res2.$i.ndx
}

for i in 1 2 3
do
for res in 1-51 368-418 735-785 1102-1152 1469-1519 1836-1886 2203-2253 2570-2620 2937-2987 
do
	for res2 in 1-51 368-418 735-785 1102-1152 1469-1519 1836-1886 2203-2253 2570-2620 2937-2987 
	do
		r1=`echo $res | cut -d "-" -f 1`
		r2=`echo $res2 | cut -d "-" -f 1`
		if [[ $r2 -gt $r1 ]]
		then
			do_mindist $res $res2
			frames $res $res2
			#echo $res $res2
		fi
	done
done
done

rm -f bind/*#*

find bind/ -type f -empty -print -delete

# combine xtcs into a big un, for VMD or clustering or what not.
gmx trjcat -f bind/*xtc -o all_bind.xtc -cat
