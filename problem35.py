#!/usr/bin/env python
import time
start_time = time.time()

import math

def rotate(l,n):
    return l[-n:] + l[:-n]

def check_prime(value):
    is_prime=True
    for i in xrange(2,int(math.sqrt(value)+1)):
        if value % i == 0:
            is_prime=False
            break
    return is_prime

def check_circ(value):
    is_circ=True
    string=str(value)
    rots=[]
    for i in range(0,len(string)):
        rots.append(rotate(string,i))
    for rot in rots:
        rot_int=int(''.join(map(str,rot)))
        if not check_prime(rot_int):
            is_circ=False
            break
    return is_circ
            

sum=0
for n in range(2,1000000):
    if check_prime(n):
        if check_circ(n):
            print n
            sum +=1

print "the anser is", sum
print("=== %s seconds ===" % (time.time() - start_time))
