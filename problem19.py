#  problem19.py
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

#~ You are given the following information, but you may prefer to do some research for yourself.
#~ 
#~ 1 Jan 1900 was a Monday.
#~ Thirty days has September,
#~ April, June and November.
#~ All the rest have thirty-one,
#~ Saving February alone,
#~ Which has twenty-eight, rain or shine.
#~ And on leap years, twenty-nine.
#~ A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#~ 
#~ How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#!/usr/bin/env python

Months = [[['January',31], #Define the months as Months[LeapYear][MonthName][NumberOfDays]
['February',28],
['March',31],
['April',30],
['May',31],
['June',30],
['July',31],
['August',31],
['September',30],
['October',31],
['November',30],
['December',31]],
[['January',31],
['February',29],
['March',31],
['April',30],
['May',31],
['June',30],
['July',31],
['August',31],
['September',30],
['October',31],
['November',30],
['December',31]]]

DaysOfWeek = ['Monday',
'Tuesday',
'Wednesday',
'Thursday',
'Friday',
'Saturday',
'Sunday']

def Get_Day(days):
	return DaysOfWeek[days % len(DaysOfWeek)]

def Calc_Year(StartYear,EndYear):
	DayCount=0
	SundayCount=0
	CalcYear=1900
	for Year in range(CalcYear,EndYear):
		LeapYear = Is_LeapYear(Year)
		for month in range(len(Months[0])):										#For twelve Months
			for date in range(1,Months[LeapYear][month][1]+1):							#For Every Day in that Month
				if Year >= StartYear:
					#~ print Year,Months[LeapYear][month][0], date, Get_Day(DayCount)				#Print the Date
					SundayCount += Is_First_Sunday(date,DayCount)					#increase Sunday Counter
				DayCount += 1													#Incrase Day Counter
	return SundayCount

def Is_LeapYear(Year):
	if (Year % 4):														
		LeapYear=0
	elif not(Year % 100) and (Year % 400):
		LeapYear=0
	else:
		LeapYear=1
	return LeapYear

def Is_First_Sunday(date,DayCount):
	if (date == 1) and (Get_Day(DayCount) == Get_Day(0)):				#If the first day of the month is Sunday
		return 1
	else:
		return 0

print "The answer is", Calc_Year(1901,2000)
