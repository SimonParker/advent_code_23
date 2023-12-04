#simon parker

path = "input.txt"
total_sum = 0

with open(path, "r") as file:
	lines = [x for x in file.readlines() if x != '\n']
	file.close()

card_counts = {}

for i in range(len(lines)):
	card_counts[i + 1] = 1

for i in range(len(lines)):
	num_matches = 0
	winning_numbers = [x for x in lines[i].split(":")[1].split("|")[0].split(" ") if x != '']
	your_numbers = [x for x in lines[i].split(":")[1].split("|")[1].split(" ") if x != '']
	for number in your_numbers:
		for winning_number in winning_numbers:
			if int(number) == int(winning_number):
				num_matches += 1
	for j in range(num_matches):
		card_counts[i + j + 2] += card_counts[i + 1] 
	total_sum += card_counts[i + 1]	



print(total_sum)
