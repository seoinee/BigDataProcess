#!/usr/bin/python3
import openpyxl
import math

wb = openpyxl.load_workbook( "student.xlsx" )
ws = wb['Sheet1']
scoreList = []

row_id = 1;
for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value 
		ws.cell(row = row_id, column = 7).value = sum_v
		scoreList.append(sum_v)
	row_id += 1

scoreList.sort(reverse=True)
cnt = ws.max_row - 1

aCnt = math.floor(cnt * 0.3)
apCnt = math.floor(cnt * 0.15)
bCnt = math.floor(cnt * 0.7)
bpCnt = math.floor(cnt * 0.5)
cpCnt = math.floor(cnt * 0.85)

for i in range(0, apCnt):
	for j in range(1, ws.max_row + 1):
		if scoreList[i] == ws.cell(row = j, column = 7).value:
			ws.cell(row = j, column = 8).value = "A+"
for i in range(apCnt, aCnt):
	for j in range(1, ws.max_row + 1):
		if scoreList[i] == ws.cell(row = j, column = 7).value:
			ws.cell(row = j, column = 8).value = "A" 

for i in range(aCnt, bpCnt):
	for j in range(1, ws.max_row + 1):
		if scoreList[i] == ws.cell(row = j, column = 7).value:
			ws.cell(row = j, column = 8).value = "B+"

for i in range(bpCnt, bCnt):
	for j in range(1, ws.max_row + 1):
		if scoreList[i] == ws.cell(row = j, column = 7).value:
			ws.cell(row = j, column = 8).value = "B"

for i in range(bCnt, cpCnt):
	for j in range(1, ws.max_row + 1):
		if scoreList[i] == ws.cell(row = j, column = 7).value:
			ws.cell(row = j, column = 8).value = "C+"

for i in range(cpCnt, cnt):
	for j in range(1, ws.max_row + 1):
		if scoreList[i] == ws.cell(row = j, column = 7).value:
			ws.cell(row = j, column = 8).value = "C"
wb.save( "student.xlsx" )

