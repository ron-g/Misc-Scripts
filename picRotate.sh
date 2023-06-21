#!/bin/bash

#a(x/sqrt(1-x*x)) * (180/3.141592654)
#-.51618517636254271869

#x=(5617-5569)/(4607-1276)

if [ "$#" -lt "4" ]
then
	echo -e "Given two planar coordinates, $(basename $0) returns the angle in degrees between the vector and horizontal.\nUseful for rotating pictures."
fi

if [ "$#" -ne "4" ] 
then
	echo -e "Usage is:\n$(basename $0) x1 y1 x2 y2"
	exit
fi

echo "pi=3.141592654;x=($4-$2)/($3-$1); a(x/sqrt(1-x*x)) * (180/pi)" | bc -l
