#!/usr/bin/env python

def is_palindrome(value):
	value_string = str(value);
	value_length = int(len(value_string))/2
	first_half = value_string[0:value_length]
	second_half = value_string[value_length*-1:]
	second_half = second_half[::-1]
	if first_half == second_half:
		return 1
	else:
		return 0

def get_products():
	products=[]
	for x in xrange(100,1000):
		for y in xrange(x,1000):
			products.append(x*y)
	return list(set(products))

products = get_products()
products.sort()

palindromes = []

for i in xrange(0,len(products)):
	if is_palindrome(products[i]):
		palindromes.append(products[i])
		
print palindromes

print "The answer is %d" % palindromes[-1]

