#!/usr/bin/env python
import time
start_time = time.time()

import sys
import math
from bisect import bisect_left
import random
def check_prime(value, primes):
    is_prime=True
    max_pos=bisect_left(primes, int(math.sqrt(value)))+1
    for p in primes[:max_pos]:
        if value % p == 0:
            is_prime=False
            break
    return is_prime

def gen_primes(max):
    primes=[2,]
    for i in xrange(3,max,2):
        if check_prime(i,primes):
            primes.append(i)
    return primes

def main():
    if sys.argv[1].isdigit():
        search = int(sys.argv[1])
        print "searching for primes up to", search
        primes = gen_primes(search)
        finish_time=(time.time() - start_time)
        print("=== %s seconds ===" % finish_time )
        print "I found", len(primes), " prime numbers."
        print "that's", int(len(primes)/finish_time), "primes per second!"
        print "up to", search, "the prime ratio is 1 to", int(search/len(primes))
        print "A random prime for your consideration:", random.choice(primes)
        print "The largest prime I found is:", primes[-1]
    else:
        print str(sys.argv[1]), "is not an integer"

main()
