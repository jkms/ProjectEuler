#  problem22.py
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

file = open('names.txt', 'r')

for line in file:
	names = list(line.split(","))
file.close()

for name in range(len(names)):
	names[name]=names[name][1:-1]										#Strip out quotes

names=sorted(names)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',			#Alphabet
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z']

#~ for letter in range(len(alphabet)):										#Add Numerical Values
	#~ alphabet[letter] = [alphabet[letter],letter+1]

My_Sum=0

for name in range(len(names)):
	Name_Sum=0
	for letter in range(len(names[name])):
		Name_Sum += alphabet.index(names[name][letter].lower()) +1
	Name_Sum = Name_Sum * (name+1)
	print names[name], Name_Sum
	My_Sum += Name_Sum

print "The Answer is", My_Sum
