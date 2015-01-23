#  problem18.py
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

file = open('problem18.txt', 'r')

def colorize():
	pyr_colors=[]
	for i in range(100):
		if i <= 13:
			pyr_colors.append(30)
		elif i <=25:
			pyr_colors.append(30)
		elif i <=38:
			pyr_colors.append(30)
		elif i <=50:
			pyr_colors.append(30)
		elif i <=63:
			pyr_colors.append(30)
		elif i <=75:
			pyr_colors.append(35)
		elif i <=88:
			pyr_colors.append(36)
		else:
			pyr_colors.append(37)
	return pyr_colors

colors = colorize()
#~ print colors

pyramid = []
for line in file:
	pyramid.append(list(line.split()))

def draw_pyramid(pyramid,xoffset=0,yoffset=0,distance=""):
	if distance == "":
		distance=len(pyramid)-yoffset
	for y in xrange(distance):
		tempstring=""
		for x in xrange(y+1):
			#~ tempstring = tempstring + "\033[0;;" + str(colors[int(pyramid[y+yoffset][x+xoffset])]) + "m" + str(pyramid[y+yoffset][x+xoffset]) + "\033[0m"
			tempstring = tempstring + str(pyramid[y+yoffset][x+xoffset]) + " "
		print tempstring

def sum_tree(pyramid,xoffset=0,yoffset=0):
	sum=0
	for y in range(len(pyramid)- yoffset):
		for x in range(xoffset, xoffset+y+1):
			#~ print y+yoffset,x,pyramid[y+yoffset][x]
			#~ sum += int(pyramid[y+yoffset][x]) # without the probabilities
			sum += float(pyramid[y+yoffset][x])/(y+1) * min((x-xoffset)+1,(xoffset+y+1)-x)
			#~ print "my divisor is", y+1, "my multiplier is", min((x-xoffset)+1,(xoffset+y+1)-x)
	#~ print "sum from", pyramid[yoffset][xoffset], "at", y+yoffset, xoffset, ":", sum
	return sum
		
def get_treesum(pyramid,xoffset=0,yoffset=0):
	totalsum=0
	for y in range(yoffset, len(pyramid)):
		#~ print pyramid[y][xoffset] #this shows the path
		left=sum_tree(pyramid,xoffset,y+1)
		right=sum_tree(pyramid,xoffset+1,y+1)
		totalsum += int(pyramid[y][xoffset])

		if y < len(pyramid)-1:
			#~ print "left:", left, pyramid[y+1][xoffset] #DEBEUG
			#~ print "right:", right, pyramid[y+1][xoffset+1] #DEBEUG
			#~ print "left-right", left-right, int(pyramid[y+1][xoffset+1]) - int(pyramid[y+1][xoffset])  #DEBEUG
			choiceoffset = int(pyramid[y+1][xoffset]) - int(pyramid[y+1][xoffset+1])
			if right - left > choiceoffset/2:
				xoffset+=1
	return totalsum
		
def produce_answer(pyramid,xoffset=0):
	totalsum=0
	for y in range(len(pyramid)):
		print pyramid[y][xoffset]
		left=get_treesum(pyramid,xoffset,y+1)
		right=get_treesum(pyramid,xoffset+1,y+1)
		totalsum += int(pyramid[y][xoffset])
		#~ print "left:", left
		#~ print "right:", right
		if right > left:
			xoffset+=1
	return totalsum

print "here's a pyramid"
draw_pyramid(pyramid,0,0)

sum_tree(pyramid)

print get_treesum(pyramid)
print produce_answer(pyramid)

#Best answers are 1074, 7185 for 18 and 67 respectively
