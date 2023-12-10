#simon parker

path = "input.txt"
total_sum = 0

with open(path, "r") as file:
	lines = file.readlines()
	file.close()

def prev_in_seq(last_seq):
	if last_seq == [x for x in last_seq if x == 0]: 
		return 0
	else:
		differences = []
		for i in range(len(last_seq) - 1):
			differences.append(last_seq[i + 1] - last_seq[i])
		return last_seq[0] - prev_in_seq(differences)
		
		

for line in lines:
	data = [int(x) for x in line.split(' ')]
	total_sum += prev_in_seq(data)

print(total_sum)
