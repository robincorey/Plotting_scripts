#!/bin/bash

NUC=(ATP ADP)

CD=`pwd`

for (( f=0; f<${#NUC[@]}; f++ )); do 
	cd $CD
	mkdir -p ${NUC[f]}_rama
	cd ${NUC[f]}_rama
	echo "" > ${NUC[f]}_comparison.xvg
	cp ../PLOT_rama_hist.py .
	cp ../PLOT_rama_hist_lines.py .
	if [ ${NUC[f]} == 'ATP' ]; then
		TIMES=(70 80 110)
	elif [ ${NUC[f]} == 'ADP' ]; then
		TIMES=(50 65 80)
	else
		echo NUC loop failed
		exit 0
	fi
	for (( j=0; j<${#TIMES[@]}; j++ )); do
		for i in {0..4}; do
			cat ../${NUC[f]}_${TIMES[j]}_${i}_rama/half1.xvg ../${NUC[f]}_${TIMES[j]}_${i}_rama/half2.xvg > ${NUC[f]}_${TIMES[j]}_${i}_rama_both.xvg
			if [ ${NUC[f]} == 'ATP' ]; then
				XTC="../../${NUC[f]}/RQH_full_Data_Archer/RQH_full_${TIMES[j]}/RQH_full_${TIMES[j]}_${i}.xtc"
				TPR="../../${NUC[f]}/RQH_full_Data_Archer/RQH_full_${TIMES[j]}/RQH_full_${TIMES[j]}_${i}.tpr"
			 elif [ ${NUC[f]} == 'ADP' ]; then
				XTC="../../${NUC[f]}/RQH_full_Data_BC3_Ian/RQH_full_${NUC[f]}_${TIMES[j]}/RQH_full_${NUC[f]}_${TIMES[j]}_${i}.secondpart.xtc"
				TPR="../../${NUC[f]}/RQH_full_Data_BC3_Ian/RQH_full_${NUC[f]}_${TIMES[j]}/RQH_full_${NUC[f]}_${TIMES[j]}_${i}.secondpart.tpr"
			fi
			for k in {1260..1277}; do
				grep "${k}$" ${NUC[f]}_${TIMES[j]}_${i}_rama_both.xvg > ${NUC[f]}_${TIMES[j]}_${i}_${k}.xvg
				python PLOT_rama_hist.py ${NUC[f]}_${TIMES[j]}_${i}_${k}.xvg
				python PLOT_rama_hist_lines.py ${NUC[f]}_${TIMES[j]}_${i}_${k}.xvg
				forbidden=`grep "^6\|^7\|^8\|^9\|^10" ${NUC[f]}_${TIMES[j]}_${i}_${k}.xvg | awk '{print $2}' | grep "^10\|^11\|^12\|^13\|^14\|^15\|^16\|^17" | wc -l`
				contact=`grep -A1 ${k} ../${NUC[f]}_distance/timespent_${NUC[f]}_${TIMES[j]}_${i}.xvg | tail -n 1`
				echo ${NUC[f]} $k $forbidden $contact >> ${NUC[f]}_comparison.xvg
			done
		done
	done
done
