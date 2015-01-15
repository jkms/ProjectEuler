#  problem9.py
#  
#  Copyright 2015 John Stafford <john@jkms.mec>
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

#!/usr/bin/env python

import math

sum = 1000

def Get_Squares(squaremax):
	"Get a list of perfect squares to a maximum number"
	square = 1
	squares = []
	while square <= squaremax:
		squares.append(int(math.pow(square,2)))
		square += 1
	return squares

def check_squares(squares, squaresum):
	"Check for count squares in sum squaresum"
	squareresult = []
	for a in range(0,len(squares)):
		for b in range(a+1,len(squares)):
			for c in range(b+1,len(squares)):
				if squares[a] + squares[b] == squares[c]:
					print "Whoa!!"
					if math.sqrt(squares[a]) + math.sqrt(squares[b]) + math.sqrt(squares[c]) == 1000:
						squareresult.append([math.sqrt(squares[a]), math.sqrt(squares[b]), math.sqrt(squares[c])])
						squareresult.append(math.sqrt(squares[a]) * math.sqrt(squares[b]) * math.sqrt(squares[c]))
	
	print "here's some junk"
	print squareresult
	return squareresult[-1]
	
				
print Get_Squares(sum)

squaresproduct = check_squares(Get_Squares(sum), sum)
print "the answer is", squaresproduct
