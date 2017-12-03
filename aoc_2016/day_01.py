directions = ["R4", "R3", "L3", "L2", "L1", "R1", "L1", "R2", "R3", "L5", "L5", "R4", "L4", "R2", "R4", "L3", "R3", "L3", "R3", "R4", "R2", "L1", "R2", "L3", "L2", "L1", "R3", "R5", "L1", "L4", "R2", "L4", "R3", "R1", "R2", "L5", "R2", "L189", "R5", "L5", "R52", "R3", "L1", "R4", "R5", "R1", "R4", "L1", "L3", "R2", "L2", "L3", "R4", "R3", "L2", "L5", "R4", "R5", "L2", "R2", "L1", "L3", "R3", "L4", "R4", "R5", "L1", "L1", "R3", "L5", "L2", "R76", "R2", "R2", "L1", "L3", "R189", "L3", "L4", "L1", "L3", "R5", "R4", "L1", "R1", "L1", "L1", "R2", "L4", "R2", "L5", "L5", "L5", "R2", "L4", "L5", "R4", "R4", "R5", "L5", "R3", "L1", "L3", "L1", "L1", "L3", "L4", "R5", "L3", "R5", "R3", "R3", "L5", "L5", "R3", "R4", "L3", "R3", "R1", "R3", "R2", "R2", "L1", "R1", "L3", "L3", "L3", "L1", "R2", "L1", "R4", "R4", "L1", "L1", "R3", "R3", "R4", "R1", "L5", "L2", "R2", "R3", "R2", "L3", "R4", "L5", "R1", "R4", "R5", "R4", "L4", "R1", "L3", "R1", "R3", "L2", "L3", "R1", "L2", "R3", "L3", "L1", "L3", "R4", "L4", "L5", "R3", "R5", "R4", "R1", "L2", "R3", "R5", "L5", "L4", "L1", "L1"]
visited = {}
x = 0
y = 0
d = 0
for direction in directions:


	if direction[0] == "R":
		d = (d + 1) % 4
	else:
		d = (d + 3) % 4
	
	steps = int(direction[1:])

	for step in range(steps):

		if d == 0:
			y += 1
		elif d == 1:
			x += 1
		elif d == 2:
			y -= 1
		else:
			x -= 1
		
		if "%d,%d" % (x,y) in visited:
			print("Visited here before: %d,%d" % (x,y))
			break;
		else:
			visited["%d,%d" % (x,y)] = 1


	print("d=%d x=%d y=%d" % (d,x,y))

print("distance = %d" % (abs(x)+abs(y)))
