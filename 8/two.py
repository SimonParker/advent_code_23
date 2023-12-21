#simon parker

from datetime import datetime



start = datetime.now().time()


path = "input.txt"
total_sum = 0

with open(path, "r") as file:
	lines = file.readlines()
	file.close()

instructions = []
lines[0] = lines[0].strip('\n')
for i in range(len(lines[0])):
	instructions.append(0 if lines[0][i] == 'L' else 1)


paths = {}
current_locations = []



for line in lines[2:]:
	values = line[6:].strip('()\n').split(', ')
	location = line[0:3]
	paths[location] = values
	if line[2] == 'A':
		current_locations.append(location)



for k in range(len(current_locations)):
	steps = 0
	i_ctr = 0
	c_start = c_end = 0
	cur_loc = current_locations[k]
	seen_locs = [(cur_loc, 0)]
	while True:
		steps += 1
		cur_loc = paths[cur_loc][instructions[i_ctr]]
		i_ctr += 1
		info = (cur_loc, i_ctr)
		if info in seen_locs:
			c_start = seen_locs.index(info)
			seen_locs.append(info)
			break
		seen_locs.append(info)
		if i_ctr >= len(instructions):
			i_ctr = 0
		
	cycle = seen_locs[c_start:]
	
	print(len(cycle) - 1)
	print(seen_locs[:10])
	print(cycle[:5])
	print(cycle[-5:])
	begins_at = len(seen_locs) - len(cycle)
	print(begins_at)
	
	zs = []
	for i in range(len(cycle)):
		if cycle[i][0][2] == 'Z':
			zs.append((cycle[i][0], i))
	
	print(len(zs))
	print(zs)
	print()

#do math to find how that compares to the length of the directions, the true cycle len is when the location loop restarts at a instruction reset
#look at each of the cycles, find when each one hits a z?? think about that more

