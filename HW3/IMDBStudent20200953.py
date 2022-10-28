#!/usr/bin/python3

f = open("movie.dat", "rt")
output = open("movieoutput.txt", "wt")

cnt = 0

genre = dict()

for line in f:
	cnt = 0
	for s in line.split("::"):
		cnt += 1
		if cnt == 3:
			for g in s.split("|"):
				if "\n" in g:
					g = g.strip('\n')
				if g not in genre:
					genre[g] = 1
				else:
					genre[g] += 1

strGenre = ""

for key, value in genre.items():
	strGenre += key + ' '
	strGenre += str(value) + '\n'

output.write(strGenre)


output.close()
