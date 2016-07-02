#!/usr/bin/env python
import time
start_time = time.time()

import sys
import math
from bisect import bisect_left
import random
def check_prime(value, primes):
    if value == 1:
        return False
    elif value == 2:
        return True
    max_pos=bisect_left(primes, int(math.sqrt(value)))+1
    for p in primes[:max_pos]:
        if value % p == 0:
            return False
    return True

def check_trunk(value, primes):
    #check left
    if value < 10:
        return False
    string = str(value)
    for i in range(1,len(string)):
        if not check_prime(int(string[i:]), primes) or not check_prime(int(string[:-i]), primes):
            return False
    return True


def gen_primes(max):
    primes=[2,]
    truncs=[]
    answer=0
    for i in xrange(3,max,2):
        if check_prime(i,primes):
            primes.append(i)
            if check_trunk(i, primes):
                truncs.append(i)
                answer+=i
 
    print truncs
    print "the answer is", answer
    return primes

gen_primes(1000000)
