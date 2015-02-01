#  problem30py
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

fpowers=[]

for n in xrange (10,1000000):
	fpowers.append(''.join(sorted(str(n))))
	
fpowers = sorted(list(set(fpowers)))

print "checking", len(fpowers)

finalSum = 0
for power in fpowers:
	#~ print power
	sum = 0
	for x in range(len(power)):
		sum += (int(str(power)[x]))**5
	#~ print ''.join(sorted(str(sum))), power
	if ''.join(sorted(str(sum))) == power:
		print "hit", sum
		finalSum += sum
	
print "the answer is", finalSum
