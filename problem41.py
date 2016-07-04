#!/usr/bin/env python
# problem41.py

import itertools

def is_prime(i):
    limit=int(i**0.5)+1
    for n in range (2,limit):
        if i % n == 0:
            return False
    return True

def gen_pandig(i):
    result = []
    pans = list(itertools.permutations(range(1,i+1)))
    for pan in pans:
        result.append(int(''.join(str(x) for x in pan)))
    return sorted(result,reverse=True)

def main():
    for i in range(7,2,-1):
        for pan in gen_pandig(i):
            if is_prime(pan):
                return pan

print "the answer is", main()
