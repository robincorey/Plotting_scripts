#!/bin/bash

# this is ok

for sys in CLA SOD PROT
do
	rm -f Fd_$sys.txt
	for rep in {1..4}
	do
		awk -F ',' '{for(i=1;i<=NF;i++)$i=(a[i]+=$i)/NR}END{print}' ${sys}_$rep.txt >> Fd_$sys.txt
	done
done

for sys in CLA SOD PROT
do
        rm -f Pf4_$sys.txt
        for rep in {1..4}
        do
		awk -F ',' '{for(i=1;i<=NF;i++)$i=(a[i]+=$i)/NR}END{print}' ${sys}_${rep}_Pf4.txt >> Pf4_$sys.txt
        done
done
