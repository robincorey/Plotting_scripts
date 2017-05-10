#!/bin/bash
#ARRAY=(WT1 PRL1)
ARRAY=(WT1 WT2 WT3 710RED1 710RED2 710RED3 PRL1 PRL2 PRL3 710OX1 710OX2 710OX3 710OX4 710OX5)
ARRAYLEN=`echo "${#ARRAY[@]} - 1" | bc`
TILT=(bending radius rise rotation tilt twist)
TILTLEN=`echo "${#TILT[@]} - 1" | bc`


for m in `seq 0 ${TILTLEN}`; do
<<"END"

for i in `seq 0 ${ARRAYLEN}`; do
	cat ${ARRAY[i]}_${TILT[m]}.xvg | egrep -v "\@|\#|\;" | awk '{print $1}' > ${ARRAY[i]}_time.xvg
	for j in `seq 1 21`; do
		rm ${ARRAY[i]}_${TILT[m]}_${j}.xvg
		echo ${ARRAY[i]}_${TILT[m]}_${j} > ${ARRAY[i]}_${TILT[m]}_${j}.xvg
		cat ${ARRAY[i]}_${TILT[m]}.xvg | egrep -v "\@|\#|\;" | awk "{print $"${j}"}" >> ${ARRAY[i]}_${TILT[m]}_${j}.xvg
	done
done

longest=`for file in $(find *_time.xvg)
do
	if [ -f $file ]; then
		wc -l $file
	fi
done | sort -n | tail -n 1 | awk '{print $2}'`

END

ARRAY2=(WT 710RED PRL 710OX)
for l in `seq 0 3`; do
	for k in `seq 1 21`; do
		rm ${ARRAY2[l]}_${k}.xvg
		paste -d ',' ${ARRAY2[l]}*${TILT[m]}_${k}.xvg > ${ARRAY2[l]}_${k}.xvg
		#tail -n +2 ${ARRAY2[l]}_${k}.xvg > ${ARRAY2[l]}_${k}_data.xvg
		cp ${ARRAY2[l]}_${k}.xvg ${ARRAY2[l]}_${k}_data.xvg
		<<"END"
		rm ${ARRAY2[l]}ave_${k}.xvg 
        	#
		### Read in data - loop
		#
		while read h; do
                sum=0
                vals=0
                vals=`echo $h | awk '{print NF}'`
                for num in $h; do
			sum=`echo "scale=5; $sum + $num " | bc`
                        ave=`echo "scale=10; $sum / $vals " | bc`
                        err=`echo $h | awk -vM=$ave '{
                                                for (i = 1; i <= NF; i++) {
                                                        sum+= (($i)-M) * (($i)-M) 
                                                };
                                                print sqrt (sum/NF)
                                                }'`
                done
                echo $ave"," $err >> ${ARRAY2[l]}ave_${k}.xvg
        	done < ${ARRAY2[l]}_${k}_data.xvg
	echo "${ARRAY2[l]}_${k} done"
END
	done
done
# mktimes

for j in `seq 1 21`; do
	paste -d ',' WT_${j}_data.xvg 710RED_${j}_data.xvg PRL_${j}_data.xvg 710OX_${j}_data.xvg> all_pos_${j}.xvg
#	leng=`wc -l ${TILT[m]}_pos_${j}.xvg`
#	for l in `seq 0 ${ARRAYLEN}`; do
#                sed '1s/^/@ legend s'${l}' "'${ARRAY[l]}'"\n/' ${TILT[m]}_pos_${j}.xvg -i
#        done
#	sed '1s/^/@ yaxis "${TILT[m]} (degrees)"\n/' ${TILT[m]}_pos_${j}.xvg -i
#	sed '1s/^/@ xaxis "time(ps)"\n/' ${TILT[m]}_pos_${j}.xvg -i
done


paste -d ',' all_pos_*.xvg > ${TILT[m]}_ALL3.xvg

done
