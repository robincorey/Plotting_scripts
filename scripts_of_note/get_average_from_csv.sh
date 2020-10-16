#!/bin/bash

for res in {1..550}
do
	tot=""
	for j in 1 2 3
	do
		val=`grep "^$res," subs_$j.csv | awk -F ',' '{print $2}'`
		if [[ -z $val ]]
		then
			tot=$tot,0.00
		else
			tot=$tot,${val::4}
		fi
	done
	if [[ $tot == *[1-9]* ]]
	then
		echo $res$tot
	fi
done
