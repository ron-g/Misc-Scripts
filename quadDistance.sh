#!/bin/bash

P1X=$1
P1Y=$2
P2X=$3
P2Y=$4

RISE=$(echo "scale=5;$P2Y-$P1Y" | bc -l)
RUN=$(echo "scale=5;$P2X-$P1X" | bc -l)

echo "sqrt($RISE*$RISE+$RUN*$RUN)" | bc -l
