#!/usr/bin/env python

import math

def is_prime(value):
	"check for primes"
	is_prime=1
	for i in xrange(2,int(math.sqrt(value))):
		if value % i == 0:
			is_prime=0
	return is_prime
			

def get_factor(value):
	"get factors"
	factors = []
	for i in xrange(2, int(math.sqrt(value))):
		if value % i == 0:
			factors.append(i)
			factors.append(value/i)
	return factors

factors = get_factor(600851475143)
factors.sort()
print factors

largest_prime = []

for i in xrange(0,len(factors)):
	if is_prime(factors[i]):
		print "%d is prime!" % factors[i]
		largest_prime.append(factors[i])
	else:
		print "%d is not a prime" % factors[i]

print largest_prime
print "The answer is %d" % largest_prime[-1]
