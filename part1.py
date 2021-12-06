file = open('input.txt', 'r')
coords = []
for line in file:
	line = line.replace(' -> ', ',')
	line = line.replace(' ', '')
	line = line.strip()
	line = line.split(',')
	coords.append([int(i) for i in line if i.isdigit()])
coordPlane = [[0]*999 for _ in range(999)]


for items in coords:
	x2 = items[2]
	y2 = items[3]
	x1 = items[0]
	y1 = items[1]
	xline = x2 - x1
	yline = y2 - y1

	if(abs(xline) != abs(yline)):
		if(xline > 0):
			for x in range(x1, x2+1):
				if coordPlane[y1][x] != 2:
					coordPlane[y1][x] += 1
		if(xline < 0):
			for x in range(x1, x2-1, -1):
				if coordPlane[y1][x] != 2:
					coordPlane[y1][x] += 1
		if(yline < 0):
			for y in range(y1, y2-1, -1):
				if coordPlane[y][x1] != 2:
					coordPlane[y][x1] += 1
		if(yline > 0):
			for y in range(y1, y2+1):
				if coordPlane[y][x1] != 2:
					coordPlane[y][x1] += 1
value = 0
for i in coordPlane:
	for j in i:
		if j == 2:
			value += 1
print(value)
