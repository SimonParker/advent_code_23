#simon parker

#this will split up the line like in part 1, but for each game keep track of the min of each color cube needed. Then finds the power of those 3 numbers, and adds that to a running sum

total_sum = 0

path = "input.txt"
with open(path, "r") as file:
	lines = file.readlines()
	file.close()

for line in lines:
	handful_list = line.split(':')[1].split(';')
	max_rgb = {'red':0, 'green':0, 'blue':0}
	for handful in handful_list:
		rgb_list = handful.split(',')
		for rgb in rgb_list:
			if rgb[0] == ' ':
				rgb = rgb[1:]
			outcome = rgb.split(' ')
			num = int(outcome[0])
			color = outcome[1].split()[0] #splitting here to remove newlines
			if num > max_rgb[color]:
				max_rgb[color] = num
	total_sum += (max_rgb['red'] * max_rgb['green'] * max_rgb['blue'])

print(total_sum)
