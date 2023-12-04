#simon parker

path = "input.txt"
total_sum = 0

with open(path, "r") as file:
	lines = [x for x in file.readlines() if x != '\n']
	file.close()


for card in lines:
	winning_numbers = [x for x in card.split(":")[1].split("|")[0].split(" ") if x != '']
	your_numbers = [x for x in card.split(":")[1].split("|")[1].split(" ") if x != '']
	winnings = 0
	for number in your_numbers:
		for winning_number in winning_numbers:
			if int(number) == int(winning_number):
				if winnings == 0:
					winnings += 1
				else:
					winnings *= 2
	total_sum += winnings

print(total_sum)
