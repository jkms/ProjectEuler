#  problem14.py
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

def collatz(number):
	if number % 2:
		number = (number*3)+1
	else:
		number /= 2
	return number


def test_collatz(maxnumber):
	startnumber = maxnumber-1
	maxchain=0
	actual_chain = []
	actual_chain.append(1)
	while startnumber > 1:
		chain = []
		number = startnumber
		while number > 1:
			chain.append(number)
			number = collatz(number)
			if len(chain) > maxchain:
				actual_chain = chain
				maxchain = len(chain)
		startnumber -= 1
	actual_chain.append(1)
	return actual_chain
	
print "the answer is", test_collatz(100000)[0]
