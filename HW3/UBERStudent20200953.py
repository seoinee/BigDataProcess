#!/usr/bin/python3

import sys
from datetime import datetime, date

def what_day(date):
	days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = date.weekday()
	return days[day]

a = sys.argv[1]
b = sys.argv[2]

f = open(a, "rt")
output = open(b, "wt")

cnt = 0
cnt2 = 0
for line in f:
	cnt = 0
	for s in line.split(","):
		cnt += 1
		if cnt == 2:
			cnt2 = 0
			for d in s.split("/"):
				cnt2 += 1
				if cnt2 == 1:
					month = int(d)
				elif cnt2 == 2:
					day = int(d)
				else:
					year = int(d)
			weekday = what_day(datetime(year, month, day))
			line = line.replace(s, weekday)
			output.write(line)
output.close()
