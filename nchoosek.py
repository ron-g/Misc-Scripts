#!/usr/bin/python3
from math import factorial as f
from sys import argv as a

n,k = int(a[1]),int(a[2])
print(f(n)//(f(n-k)*f(k)))
