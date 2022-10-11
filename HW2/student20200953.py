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

aCnt = scoreList[math.floor(cnt * 0.3)]
apCnt = scoreList[math.floor(cnt * 0.15)]
bCnt = scoreList[math.floor(cnt * 0.7)]
bpCnt = scoreList[math.floor(cnt * 0.5)]
cpCnt = scoreList[math.floor(cnt * 0.85)]

row_id = 1;

for row in ws:
	if row_id != 1:
		if ws.cell(row = row_id, column = 7).value > apCnt:
			ws.cell(row = row_id, column = 8).value = "A+"
		elif ws.cell(row = row_id, column = 7).value > aCnt:
			ws.cell(row = row_id, column = 8).value = "A"
		elif ws.cell(row = row_id, column = 7).value > bpCnt:
			ws.cell(row = row_id, column = 8).value = "B+"
		elif ws.cell(row = row_id, column = 7).value > bCnt:
			ws.cell(row = row_id, column = 8).value = "B"
		elif ws.cell(row = row_id, column = 7).value > cpCnt:
			ws.cell(row = row_id, column = 8).value = "C+"
		else:
			ws.cell(row = row_id, column = 8).value = "C"
	row_id += 1
wb.save( "student.xlsx" )
