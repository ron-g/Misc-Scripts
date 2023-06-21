#!/bin/bash
function factorial(){
	NUMBER=$1
	RESULT=1
	if [ $NUMBER -lt 1 ]
	then
		return $RESULT
	else
	while [ $NUMBER -gt 0 ]
	do
		RESULT=$(echo "$RESULT*$NUMBER" | bc)
		NUMBER=$(echo "$NUMBER-1" | bc)
	done
	fi
	echo $RESULT | tr -d '\\ [a-zA-Z]'
}

n=$1
k=$2
if [ "$n" -lt "$k" ]
then
	exit
fi
if [ "$n" -eq "$k" ]
then
	nminusk=1
else
	nminusk=$(echo "$n"'-'"$k" | bc)
fi
nF=$(factorial $n)
kF=$(factorial $k)
nminuskF=$(factorial $nminusk)

echo "($nF)/($kF*$nminuskF)" | bc
