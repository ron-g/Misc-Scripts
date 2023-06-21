#!/usr/bin/python3

from colorama import Fore, Back

top, bottom = '', ''
symbol = '▲'
size = 20

for i in range(size):
    if i%2 == 0:
        top += f"{symbol*i + symbol: ^{size*2}}\n"
        bottom += f"{symbol*i + symbol: ^{size}}{symbol*i + symbol: ^{size}}\n"

print(
        Fore.LIGHTYELLOW_EX,
        f"{top}{bottom}",
        Fore.RESET,
        sep='',
        end=''
        )

