#!/usr/bin/python3

import argparse

top, bottom = '', ''

parser = argparse.ArgumentParser(description="Make a Legend of Zelda Triforce.")

parser.add_argument(
	"--height",
	type=int,
	default = "8",
	help="Integer. The height of the triforce."
	)

parser.add_argument(
	"--char",
	type=str,
	default = '⟁',
	help="Character/String. The character to be repeated."
	)

args = parser.parse_args()

try:
	n = args.height
except:
	print(f"'{args.height}' isn't an integer")
	exit(1)

try:
	SYM = args.char[0]
except:
	print(f"'{args.char}' isn't a valid string/character.")
	exit(2)

for i in range(n):
	if i%2 == 0:
		top += f"{SYM*i + SYM: ^{n*2}}\n"
		bottom += f"{SYM*i + SYM: ^{n}}{SYM*i + SYM: ^{n}}\n"

print(f"{top}{bottom}")

