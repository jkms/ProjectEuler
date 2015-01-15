#  problem10.py
#  
#  Copyright 2015 John Stafford <john@jkms.me>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#!/usr/bin/env python

import math

def is_prime(value):
	"check for primes"
	is_prime=1
	for i in xrange(2,int(math.sqrt(value))+1):
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

def sum_list(list):
	"Sum all numbers in a list"
	listsum=0
	for n in range(len(list)):
		listsum += list[n]
	return listsum
	
primes = get_primes(2000000)
print primes
print sum_list(primes)
