#!/bin/bash

NUC=(ATP ADP) ## ADP)

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
			cat ${NUC[f]}_${TIMES[j]}_${i}_1270.xvg ${NUC[f]}_${TIMES[j]}_${i}_1271.xvg ${NUC[f]}_${TIMES[j]}_${i}_1272.xvg ${NUC[f]}_${TIMES[j]}_${i}_1273.xvg ${NUC[f]}_${TIMES[j]}_${i}_1274.xvg ${NUC[f]}_${TIMES[j]}_${i}_1275.xvg ${NUC[f]}_${TIMES[j]}_${i}_1276.xvg > ${NUC[f]}_${TIMES[j]}_${i}_half2.xvg
			python PLOT_rama_hist_lines.py ${NUC[f]}_${TIMES[j]}_${i}_half2.xvg
			forbidden=`grep "^6\|^7\|^8\|^9\|^10" ${NUC[f]}_${TIMES[j]}_${i}_half2.xvg | awk '{print $2}' | grep "^10\|^11\|^12\|^13\|^14\|^15\|^16\|^17" | wc -l`
			contact1=`grep -A1 1270 ../${NUC[f]}_distance/timespent_${NUC[f]}_${TIMES[j]}_${i}.xvg | tail -n 1`
			contact2=`grep -A1 1271 ../${NUC[f]}_distance/timespent_${NUC[f]}_${TIMES[j]}_${i}.xvg | tail -n 1`
			contact3=`grep -A1 1272 ../${NUC[f]}_distance/timespent_${NUC[f]}_${TIMES[j]}_${i}.xvg | tail -n 1`
			contact4=`grep -A1 1273 ../${NUC[f]}_distance/timespent_${NUC[f]}_${TIMES[j]}_${i}.xvg | tail -n 1`
			contact5=`grep -A1 1274 ../${NUC[f]}_distance/timespent_${NUC[f]}_${TIMES[j]}_${i}.xvg | tail -n 1`
			contact6=`grep -A1 1275 ../${NUC[f]}_distance/timespent_${NUC[f]}_${TIMES[j]}_${i}.xvg | tail -n 1`
			contact7=`grep -A1 1276 ../${NUC[f]}_distance/timespent_${NUC[f]}_${TIMES[j]}_${i}.xvg | tail -n 1`
			contact=`echo "$contact1 + $contact2 + $contact3 + $contact4 + $contact5 + $contact6 + $contact7" | bc`
			echo ${NUC[f]} ${TIMES[j]}_${i} $forbidden $contact >> ${NUC[f]}_forbidden_half2.xvg
		done
	done
done
