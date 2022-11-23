#!/bin/bash

# which route my friend?
# MraY only. Might need to make system specific

DIR=/sansom/s156a/bioc1535/MraY/MraY_mutations/UDP1/Data/PO4_pos

get_flip () {
# first get all flips
# get centre of membrane
centre=`grep -v -e '\@' -e '\#' $DIR/$rep.$sys.xvg | head -n 1 | awk '{sum=0; for(i=2; i<=NF; i++){sum+=$i}; sum/=(NF-1); print sum}'`
echo $centre
wc=`awk '{print NF}' $DIR/$rep.$sys.xvg | tail -n 1`
for (( i=1; i<${wc}; i++ ))
do
	init=`grep -v -e '\@' -e '\#' $DIR/$rep.$sys.xvg | awk -v var=$((i+1)) '{print $var}' | head -n 1`
        flip=`awk -v var=$i '{print $var}' $DIR/$rep.$sys.xvg | if grep -q "^[3-5]" && grep -q "^[7-9]"; then echo y ; fi`
	echo $i $init $flip
done
}

path_flip () {
# just thingy flips?
:
}

for sys in WT #UDP1_2
do
	for rep in {1..1}
	do
		get_flip	
	done
done
