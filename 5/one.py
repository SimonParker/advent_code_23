#simon parker

closest_loc = -1
path = "input_small.txt"

seeds = []
seed_soil = []
soil_fert = []
fert_h2o = []
h2o_lit = []
lit_temp = []
temp_hum = []
hum_loc = []
mappings = [seed_soil, soil_fert, fert_h2o, h2o_lit, lit_temp, temp_hum, hum_loc]


with open(path, "r") as file:
	sections = [x.split(':')[1] for x in file.read().split('\n\n')]
	file.close()
	seeds = [int(x) for x in sections[0].split(' ') if x != '']	
	for i in range(1, len(sections)):
		line = [x for x in sections[i].split('\n') if x != '']
		for part in line:
			mappings[i - 1].append([int(x) for x in part.split(' ')])


def pass_through_map(number, mapping):
	result = number
	for line in mapping:
		if line[1] <= number < line[1] + line[2]:
			result = number + (line[0] - line[1])
			break 
	return result



for seed in seeds:
	number = seed
	for i in range(len(mappings)):
		number = pass_through_map(number, mappings[i])
	if number < closest_loc or closest_loc < 0:
		closest_loc = number

print(closest_loc)
