#  problem21.py
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
	return products

my_sum=0
for i in range(1,10001):
	#~ print get_products(i)[:-1]
	temp1 = sum(get_products(i)[:-1])
	temp2 = sum(get_products(temp1)[:-1])
	#~ print i, temp1, temp2
	if i==temp2 and i != temp1 :
		print "hit!!!", i, temp1
		my_sum+=i

print "the answer is", my_sum
		
