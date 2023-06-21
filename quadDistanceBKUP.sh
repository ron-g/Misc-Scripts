#!/bin/bash

P1X=$1
P1Y=$2
P2X=$3
P2Y=$4

RISE=$(($P2Y-$P1Y))
RUN=$(($P2X-$P1X))

echo "sqrt($RISE*$RISE+$RUN*$RUN)" | bc -l
