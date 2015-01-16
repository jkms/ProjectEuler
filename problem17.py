#  problem17.py
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

first_column=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
second_column=['zero','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
third_column='hundred'
fourth_column='thousand'
conjunction='and'

def get_words(value):
	def thousand(value):
		return first_column[value] + "" + fourth_column
	def hundred(value):
		return first_column[value] + "" + third_column
	def ending(value):
		if value>0:
			if value<20:
				return first_column[value]
			else:
				if value % 10:
					return second_column[int(str(value)[0])] + "" + first_column[int(str(value)[1])]
				else:
					return second_column[int(str(value)[0])]
		else:
			return ""
	
	stringend = ending(int(str(value)[-2:]))
	if len(str(value))>3:
		stringstart=thousand(int(str(value)[0]))
		if int(str(value)[1])>0:
			stringstart=stringstart + "" + hundred(int(str(value)[1]))
			if int(str(value)[-2:])>0:
				stringstart=stringstart + "and"
		elif int(str(value)[-2:])>0:
			stringstart=stringstart + ""
	elif len(str(value))>2:
		stringstart=hundred(int(str(value)[0]))
		if int(str(value)[-2:])>0:
			stringstart=stringstart + "and"
	else:
		stringstart = ""
		
	return stringstart + stringend

wordsum = 0
for i in range(1,1001):
	temp = get_words(i)
	wordsum += len(temp)
	print temp, len(temp)
	
print "the answer is", wordsum
