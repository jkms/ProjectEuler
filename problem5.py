#!/usr/bin/env python

import math

def is_prime(value):
	"check for primes"
	is_prime=1
	for i in xrange(2,value):
		if value % i == 0:
			is_prime=0
	return is_prime

def get_primes(max):
	"Get the primes up until number 'max'"
	primes = []
	for i in range(2,max+1):
		if is_prime(i):
			primes.append(i)
	return primes

primes = get_primes(20)

def get_products(product):
	products = []
	for i in range(0,len(primes)):
		if product % primes[i] == 0:
			products = [primes[i], product/primes[i]]
			break
	for j in range(0,len(products)):
		if products[j] == 1:
			products.remove(1)
		elif is_prime(products[j]) == 0:
			temp = products[j]
			products.remove(temp)
			products = products + get_products(temp)
	return products
							
			
allproducts = []

for x in range(2,21):
	products = []
	products = get_products(x)
	allproducts.append(products)

formula = []

for x in range(0,len(allproducts)):
	for y in range(0,len(primes)):
		if allproducts[x].count(primes[y]) > formula.count(primes[y]):
			if formula.count(primes[y]) != 0:
				formula.remove(primes[y])
			formula += allproducts[x]

formula.sort()
print formula

answer = 1
for x in range(0,len(formula)):
	answer = answer * formula[x]
	
print "The answer is ", answer
