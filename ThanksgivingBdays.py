#!/usr/bin/python3

import datetime

from colorama import Fore, Back

yearRange = range(1970,2086)
dayRange = range(22,29)

PeopleBdays = {
	21 : "This will never happen",
	22 : "P0",
	23 : "P1",
	24 : "P2",
	25 : "P3",
	26 : "P4",
	27 : "P5",
	29 : "This will never happen either",
}

print("Thanksgiving birthdays:")
for yr in yearRange:
	for day in dayRange:
		TheDate = datetime.datetime(yr, 11, day)
		if ( TheDate.strftime('%a') == 'Thu' ):
			try:
				soandsosBday = PeopleBdays[day]
				print(f"\t{TheDate.strftime('%Y/%m/%d')}: {Fore.GREEN}{Back.BLACK}{soandsosBday}{Back.RESET}{Fore.RESET}")
			except:
				pass

