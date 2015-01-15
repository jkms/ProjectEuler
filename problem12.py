#  problem12.py
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

def triangle_sum(value):
	trianglesum = 0
	for n in xrange(value+1):
		trianglesum += n
	return trianglesum

def get_products(value):
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
	return products

countproducts = 0
testvalue = 0
while countproducts < 500:
	testvalue += 1
	products = get_products(triangle_sum(testvalue))
	countproducts = len(products)

print products
print "the answer is", triangle_sum(testvalue)


