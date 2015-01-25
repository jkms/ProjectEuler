#  problem24.py
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
MyString="0123456789"
import math

def process_string(MyString='0123456789',findex=[0,0]):
	#~ print "findex", findex
	column=len(MyString)-2
	sections=MyString[:column-findex[0]], MyString[column-findex[0]], MyString[column-findex[0]+1:]
	remainder=sections[1]+sections[2]
	column_char=remainder[findex[1]]
	remainder=list(remainder)
	remainder=sorted(remainder)
	#~ print "init remind", remainder
	remainder.remove(column_char)
	remainder=''.join(remainder)
	#~ print sections[0],column_char,remainder
	reorder=sections[0]+column_char+remainder
	
	return reorder

factorial=[]
for i in range(1,len(MyString)):
	factorial.append(math.factorial(i))
	
def check_column(iteration):
	iteration-=1
	if iteration < 0:
		iteration=0
	column_return=[]
	while iteration:
		for factor in reversed(factorial):
			#~ print "checking factor", factor
			while iteration >= factor:
				#~ print "check_column:",iteration, factor
				if not (iteration%factor):
					#~ print "hit!"
					column_return.append([factorial.index(factor),(iteration/factor)])
					iteration=0
				else:
					column_return.append([factorial.index(factor),(iteration/factor)])
					iteration %= factor
	return column_return
				
def check_string(String="012345679",iteration=1):
	mods = check_column(iteration)
	#~ print mods
	String_Iteration=String
	for mod in mods:
		#~ print String_Iteration, iteration, mod
		String_Iteration = process_string(String_Iteration,mod)
	return String_Iteration

#~ print check_string(MyString,100)

for i in range(10):
	print i, check_string(MyString,i)

for i in range(999995,1000005):
	print i, check_string(MyString,i)
	
