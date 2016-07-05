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
    pans = list(itertools.permutations(range(0,i)))
    for pan in pans:
        result.append(int(''.join(str(x) for x in pan)))
    return sorted(result,reverse=True)

def main():
    count = 0
    for pan in gen_pandig(10):
        if int(''.join(str(pan)[1:4])) % 2 == 0:
            if int(''.join(str(pan)[2:5])) % 3 == 0:
                if int(''.join(str(pan)[3:6])) % 5 == 0:
                    if int(''.join(str(pan)[4:7])) % 7 == 0:
                        if int(''.join(str(pan)[5:8])) % 11 == 0:
                            if int(''.join(str(pan)[6:9])) % 13 == 0:
                                if int(''.join(str(pan)[7:10])) % 17 == 0:
                                    count += pan
    return count

print "the answer is", main()
