#simon parker

#this will grab the game ID from the start of each line, then split the remaining line several times until im left with a number and a color
#then check against max vals, sum as needed


total_sum = 0
max_vals = {'red':12, 'green':13, 'blue':14}

path = "input.txt"
with open(path, "r") as file:
	lines = file.readlines()
	file.close()

for line in lines:
	valid_game = True
	game = line.split(':')
	header = game[0]
	game_num = header.split(' ')[1]
	data = game[1]
	handful_list = data.split(';')
	for handful in handful_list:
		rgb_list = handful.split(',')
		for rgb in rgb_list:
			if rgb[0] == ' ':
				rgb = rgb[1:]
			outcome = rgb.split(' ')
			num = int(outcome[0])
			color = (outcome[1].split())[0] #splitting here to remove newlines
			if num > max_vals[color]:
				valid_game = False
				break	
		if not valid_game:
			break
	if valid_game:
		total_sum += int(game_num) 


print(total_sum)
