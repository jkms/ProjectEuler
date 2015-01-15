#!/usr/bin/env python

import math

def is_prime(value):
	"check for primes"
	is_prime=1
	for i in xrange(2,int(math.sqrt(value))+1):
		if value % i == 0:
			is_prime=0
	return is_prime

testnumber = 2
primes = []
primecount = 0
while primecount <= 10001:
	if is_prime(testnumber):
		primes.append(testnumber)
	testnumber += 1
	primecount = len(primes)

print primes
print "the answer is", primes[10000]
