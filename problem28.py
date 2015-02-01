#  problem27.py
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

def count_corners(ns_len=25):
	CornerSum=0
	point = 1
	CornerSum += point
	EdgeLength=2
	while point < ns_len - EdgeLength:
		for x in range (4):
			point += EdgeLength
			#~ print point
			CornerSum += point
		EdgeLength+=2
	return CornerSum
			
	
print "the answer is", count_corners(1001**2)
