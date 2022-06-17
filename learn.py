#!/usr/bin/env python

from random import sample
from sys import argv

fc = tuple(open(argv[1], 'r').read().splitlines())
fd = {}
greenBold = "\033[1;32m"
greenItalic = "\033[3;32m"
redBold = "\033[1;31m"
redItalic = "\033[3;31m"
reset = "\033[0;0m"

for i in fc:
    k, v = i.split(': ')
    v = v.split(', ')
    fd.update({k: v})

while True:
    ri = tuple(sample(range(len(fd)), len(fd)))
    for i in ri:
        q = tuple(fd.keys())[i]
        c = fd.get(q)
        ans = input(f"{q}: ")
        if ans in c: print(f"{greenBold}Correct!{reset}")
        else:
            w = []
            s = ''
            for ci in range(len(c)):
                w.append(c[ci].replace(ans, ''))
                if ans+w[ci] == c[ci]:
                    s += f"{greenItalic}{ans}{redItalic}{w[ci]}{reset}, "
                elif w[ci]+ans == c[ci]:
                    s += f"{redItalic}{w[ci]}{greenItalic}{ans}{reset}, "
                else:
                    s += f"{redItalic}{c[ci]}{reset}, "
            s=s[:-2]
            print(f"{redBold}Wrong!{reset} ({s})")
