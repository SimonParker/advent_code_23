#simon parker


import re

path = "input.txt"
total_sum = 0

with open(path, "r") as file:
	Lines = file.readlines()
	file.close()

digits = []
valid_part = False

for i in range(len(Lines)):
	for j in range(len(Lines[0]) - 1):
		char = Lines[i][j]
		if char.isnumeric():
			digits.append(char)
			prev_row = (i - 1) if (i - 1) > -1 else 0
			next_row = (i + 1) if (i + 1) < len(Lines) else len(Lines) - 1
			prev_col = (j - 1) if (j - 1) > -1 else 0
			next_col = (j + 1) if (j + 1) < len(Lines[0]) - 1 else len(Lines[0]) - 2
			for row in range(prev_row,next_row + 1):
				for col in range(prev_col,next_col + 1):
					char = Lines[row][col]
					if re.search("[^0-9.]", str(char)) is not None:
						#print(char)
						valid_part = True
		else:
			if valid_part is True:
				total_sum += int(''.join(digits))
			valid_part = False
			digits = []

print(total_sum)

