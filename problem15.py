#  problem15.py
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

gridsize=20
grid = []

for y in range(0,gridsize+1):
	temparray = []
	for x in range(0,gridsize+1):
		if y == 0:
			if x== 0:
				temparray.append(0)
			else:
				temparray.append(1)
		elif x == 0:
			temparray.append(grid[0][y])
		else:
			value = grid[y-1][x] + temparray[x-1]
			temparray.append(value)
	grid.append(temparray)

print grid
print "the answer is", grid[gridsize][-1]

