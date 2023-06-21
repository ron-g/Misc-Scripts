#!/usr/bin/python3

from sys import argv as a

try:
  n = int(a[1])
except:
  print(f"{a[1]} isn't an int")
  exit(1)

SYM='⟁'
top, bottom = '', ''

for i in range(n):
  if i%2 == 0:
    top += f"{SYM*i + SYM: ^{n*2}}\n"
    bottom += f"{SYM*i + SYM: ^{n}}{SYM*i + SYM: ^{n}}\n"
print(f"{top}{bottom}")

