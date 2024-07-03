#simon parker

pathname = "input_small2.txt"

with open(pathname, "r") as file:
	lines = [x.strip() for x in file.readlines()]
	file.close()

num_col = len(lines[0])
num_row = len(lines)

lines.reverse()

def find_start(tiles):
	for i in range(num_row):
		row = tiles[i]
		for j in range(num_col):
			if row[j] == 'S':
				return (i, j) 
	return (-1, -1)

start = find_start(lines)
print(lines[start[0]][start[1]] == 'S')

p1 = 'z'
p1_goes = '' 
p2 = 'z'
p2_goes = ''

def set_point(char):
	if p1 == 'z':
		p1 = char
	else:
		p2 = char

if start[0] != num_row - 1:
	match lines[start[0] + 1][start[1]]:
		case '|':
			set_point('|')
			p1_goes = 'n' #we can only assume it's p1 because this is the first spot we check. we need to check for that somehow
		
''' #think im doing this wrong. it's not a maze, its a path. there's only one place my current pipe can go, like if im going right in a '-', look at the dest character only
valid_up = ['|', 'F', '7']
valid_down = ['|', 'L', 'J']
valid_left = ['-', 'L', 'F']
valid_right = ['-', 'J', '7']

starting_point = find_start(lines)
cur_loc = starting_point
last_loc = (-1, -1)

looped = False

steps = 0
while not looped:
	print(cur_loc)
	if cur_loc[1] < num_row and lines[cur_loc[1] + 1][cur_loc[0]] in valid_up and (cur_loc[0], cur_loc[1] + 1) != last_loc: 
		last_loc = cur_loc
		cur_loc = (cur_loc[0], cur_loc[1] + 1)
	
	elif cur_loc[0] < num_col and lines[cur_loc[1]][cur_loc[0] + 1] in valid_right and (cur_loc[0] + 1, cur_loc[1]) != last_loc:
		last_loc = cur_loc
		cur_loc = (cur_loc[0] + 1, cur_loc[1])
	
	elif cur_loc[1] > 0 and lines[cur_loc[1] - 1][cur_loc[0]] in valid_down and (cur_loc[0], cur_loc[1] - 1) != last_loc: 
		last_loc = cur_loc
		cur_loc = (cur_loc[0], cur_loc[1] - 1)

	else:
		last_loc = cur_loc
		cur_loc = (cur_loc[0] - 1, cur_loc[1])

	if cur_loc == starting_point:
		looped == True
	steps += 1

print(steps)
print(steps / 2)
'''
