#!/bin/bash

for sys in CLA SOD PROT
do
	rm -f Fd_$sys.txt
	for i in {1..4}
	do
		awk -F ',' '{for (i=1;i<=NF;i++) sum[i]+=$i} END{for (i in sum) printf "%5.2f,", sum[i]/NR }' ${sys}_$i.txt >> Fd_$sys.txt
		echo -e '' >> Fd_$sys.txt
	done
done

for sys in CLA SOD PROT
do
        rm -f Pf4_$sys.txt
        for i in {1..4}
        do
                awk -F ',' '{for (i=1;i<=NF;i++) sum[i]+=$i} END{for (i in sum) printf "%5.2f,", sum[i]/NR }' ${sys}_$i.txt >> Pf4_$sys.txt
                echo -e '' >> Pf4_$sys.txt
        done
done
