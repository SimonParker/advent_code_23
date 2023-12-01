#simon parker

#this code reads a line from an input file, extracts the first and last numbers from that to create a 2 digit number, and adds that value to a running sum

total_sum = 0
digit1 = None
digit2 = None

path = "input.txt"


with open(path, "r") as f:
	lines = f.readlines()
	for line in lines:
		for char in line:
			if char.isnumeric():
				digit1 = int(char)
				break
		for char in line[::-1]:
			if char.isnumeric():
				digit2 = int(char)
				break
		num = (digit1 * 10) + digit2
		total_sum += num

print(total_sum)
