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
vehicles = dict()
trips = dict()
bind = dict()

for line in f:
	cnt = 0
	for s in line.split(","):
		cnt += 1
		if cnt == 1:
			first = s
		elif cnt == 2:
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
			first = first + "," + weekday
		elif cnt == 3:
			if first not in vehicles:
				vehicles[first] = int(s)
			else:
				vehicles[first] += int(s)
		else:
			if first not in trips:
				trips[first] = int(s)
			else:
				trips[first] += int(s)
for key in vehicles:
	if key not in bind:
		bind[key] = str(vehicles[key]) + "," + str(trips[key])
strBind = ""

for key, value in bind.items():
	strBind += key + ' '
	strBind += value + '\n'
output.write(strBind)

output.close()
