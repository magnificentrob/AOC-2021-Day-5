file = open('input.txt', 'r')
coords = []
large = 999
for line in file:
	line = line.replace(' -> ', ',')
	line = line.replace(' ', '')
	line = line.strip()
	line = line.split(',')
	coords.append([int(i) for i in line if i.isdigit()])

coordPlane = [[0]*large for _ in range(large)]

for items in coords:
	x2 = items[2]
	y2 = items[3]
	x1 = items[0]
	y1 = items[1]
	xline = x2 - x1
	yline = y2 - y1
	if(xline > 0 and yline == 0):
		coordPlane[x1][y1] += 1
		while x1 != x2:
			x1 += 1
			coordPlane[x1][y1] += 1
	if(xline < 0 and yline == 0):
		coordPlane[x1][y1] += 1
		while x1 != x2:
			x1 -= 1
			coordPlane[x1][y1] += 1
	if(xline == 0 and yline < 0):
		coordPlane[x1][y1] += 1
		while y1 != y2:
			y1 -= 1
			coordPlane[x1][y1] += 1
	if(xline == 0 and yline > 0):
		coordPlane[x1][y1] += 1
		while y1 != y2:
			y1 += 1
			coordPlane[x1][y1] += 1
	if(abs(xline) == abs(yline) and xline < 0 and yline >0):
		coordPlane[x1][y1] += 1
		while(x1 != x2 and y1 != y2):
			x1 -= 1
			y1 += 1
			coordPlane[x1][y1] += 1
	if(abs(xline) == abs(yline) and xline < 0 and yline <0):
		coordPlane[x1][y1] += 1
		while(x1 != x2 and y1 != y2):
			x1 -= 1
			y1 -= 1
			coordPlane[x1][y1] += 1
	if(abs(xline) == abs(yline) and xline > 0 and yline >0):
		coordPlane[x1][y1] += 1
		while(x1 != x2 and y1 != y2):
			x1 += 1
			y1 += 1
			coordPlane[x1][y1] += 1
	if(abs(xline) == abs(yline) and xline > 0 and yline < 0):
		coordPlane[x1][y1] += 1
		while(x1 != x2 and y1 != y2):
			x1 += 1
			y1 -= 1
			coordPlane[x1][y1] += 1	
value = 0
for i in coordPlane:
	for j in i: 
		if j > 1: value +=1
print(value)
