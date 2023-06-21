#!/bin/bash

for n in {1..10}
do
	for k in $(seq 1 $n)
	do
		echo -e "$n $k $(./nchoosek.sh $n $k)"
	done
done


