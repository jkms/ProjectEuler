#  problem23.py
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

perfect_numbers=[]
abundant_numbers=[]
deficient_numbers=[]

def is_perfect(number):
	products = get_products(number)
	productsum=sum(products)
	if productsum > number:
		abundant_numbers.append(number)
		deficient_numbers.append(None)
		perfect_numbers.append(None)
	elif productsum < number:
		abundant_numbers.append(None)
		deficient_numbers.append(number)
		perfect_numbers.append(None)
	else:
		abundant_numbers.append(None)
		deficient_numbers.append(None)
		perfect_numbers.append(number)
	return None

def get_products(value):
	"List proper divisors"
	products = []
	stop = value/2
	n=0
	while n < stop:
		n+=1
		if value % n == 0:
			products.append(n)
			products.append(value/n)
			stop = value/n
	products = list(set(products))
	products.sort()
	return products[:-1]
	
for i in range(28124):
	is_perfect(i)

magic_numbers=[]
for n in range(28124):
	#~ print n
	x=1
	while x <= n:
		if x == n:
			#~ print n, "is a miss!"
			magic_numbers.append(n)
		if abundant_numbers[x]:
			#~ print n,x,abundant_numbers[n-x]
			if abundant_numbers[(n - abundant_numbers[x])]:
				#~ print n, "is a hit!"
				break
		x+=1

print magic_numbers
print sum(magic_numbers)

#~ print abundant_numbers
#~ print perfect_numbers
#~ print abundant_numbers
#~ print deficient_numbers
