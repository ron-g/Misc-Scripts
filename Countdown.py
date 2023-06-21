#!/usr/bin/python3

import datetime, time

SleepDuration = 1/3
LaunchTime = datetime.datetime(2022,12,22,17,30,0)

while True:
	CountDown = LaunchTime - datetime.datetime.now()
	CountDown = str(CountDown).split('.')[0]
	padding = len(CountDown) + 1
	print(' '*2*padding, '\r', end='')
	time.sleep(SleepDuration)
	print(f"{CountDown:>{padding}}", end='')
	#time.sleep(SleepDuration)
	#print('\r', end='')


