#simon parker

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

for line in lines[2:]:
	values = line[6:].strip('()\n').split(', ')
	paths[line[0:3]] = values


instruction_counter = 0
current_loc = 'AAA'
while True:
	current_loc = paths[current_loc][instructions[instruction_counter]]
	instruction_counter = instruction_counter + 1 if instruction_counter + 1 < len(instructions) else 0
	total_sum += 1
	if current_loc == 'ZZZ':
		break


print(total_sum)
