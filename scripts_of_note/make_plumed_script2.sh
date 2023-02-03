#!/bin/bash

##takes input $1 POPE, POPG, CARD or BB

#if [[ $1 == "POPE" ]];then
	#BB_beads=$(grep "PO4 $1" md-fit-$1.pdb | awk '{print $2}')
#elif [[ $1 == "POPG" ]];then
	#BB_beads=$(grep "PO4 $1" md-fit-$1.pdb | awk '{print $2}')
#elif [[ $1 == "CARD" ]];then
	#BB_beads=$(grep "PO2 $1" md-fit-$1.pdb | awk '{print $2}')
#elif [[ $1 == "BB" ]];then
	#BB_beads=$(grep " $1 " md-fit-$1.pdb | awk '{print $2}')	
#else
	#echo "please define lipid/protein in command: POPE, POPG, CARD or BB"
#fi 

if [[ -z $1 ]]; then "please define lipid/protein in command: POPE, POPG, CARD or BB" ; exit 0 ; fi

if [[ $1 == "POPE" ]];then
	BB_beads=$(grep "PO4 $1" md-centre-$1.pdb | awk '{print $2}')
elif [[ $1 == "POPG" ]];then
	BB_beads=$(grep "PO4 $1" md-centre-$1.pdb | awk '{print $2}')
elif [[ $1 == "CARD" ]];then
	BB_beads=$(grep "PO2 $1" md-centre-$1.pdb | awk '{print $2}')
elif [[ $1 == "BB" ]];then
	BB_beads=$(grep " $1 " md-centre-$1.pdb | awk '{print $2}')	
fi 


#echo "MOLINFO STRUCTURE=md-fit-"$1".pdb"
echo "MOLINFO STRUCTURE=md-centre-"$1".pdb"

for bead in $BB_beads; do
echo "B$bead: CENTER ATOMS=$bead NOPBC"
done
echo ""

for bead in $BB_beads; do
echo pos$bead: POSITION ATOM=B$bead NOPBC
done

printf "PRINT "
for bead in $BB_beads; do
if [ $bead = "1" ]; then
printf "ARG=pos$bead.x"
else
printf ",pos$bead.x"
fi
done 
echo " FILE="$1"_POS_X STRIDE=1"

printf "PRINT "
for bead in $BB_beads; do
if [ $bead = "1" ]; then
printf "ARG=pos$bead.y"
else
printf ",pos$bead.y"
fi
done 
echo " FILE="$1"_POS_Y STRIDE=1"

printf "PRINT "
for bead in $BB_beads; do
if [ $bead = "1" ]; then
printf "ARG=pos$bead.z"
else
printf ",pos$bead.z"
fi
done 
echo " FILE="$1"_POS_Z STRIDE=1"



