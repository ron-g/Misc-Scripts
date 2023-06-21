#!/usr/bin/python3

import string as S

'''
valid plates:
	start with at least two letters
	contain 2-6 chars
	numbers at the end
	first number can't be zero
	no periods, spaces, punct marks allowed
	inputs must be uppercase
'''

plate = input("Plate: > ")

if plate.isupper():
	pass
else:
	print(f"'{plate}' isn't uppercase.")
	exit(1)

if len(plate) >= 2 and len(plate) <= 6:
	pass
else:
	print(f"'{plate}' should be 2-6 chars.")
	exit(2)

if plate[:2].isalpha():
	pass
else:
	print(f"'{plate}' first two chars should be letters.")
	exit(3)

if len(plate.strip(S.ascii_uppercase + S.digits)) == 0:
	pass
else:
	print(f"'{plate}' contains illegal chars.")
	exit(4)

if ( plate + '_' ).strip(S.ascii_uppercase)[0] != '0':
	pass
else:
	print(f"'{plate}' can't have a zero as the first digit.")
	exit(5)

if plate[-1].isdigit() and plate.strip(S.ascii_uppercase).isdigit():
	pass
else:
	print(f"'{plate}' must have numbers at the end.")
	exit(4)


print(f"'{plate}' seems valid.")


