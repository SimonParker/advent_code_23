#simon parker, with help from my dad

pathname = "input.txt"
with open(pathname, "r") as file:
	lines = file.readlines()
	file.close()


times = [int(x) for x in lines[0].split()[1:]]
records = [int(x) for x in lines[1].split()[1:]]



total = 1


for i in range(len(times)):
	for j in range(times[i]):
		value = j * (times[i] - j)
		if value > records[i]:
			total *= (times[i] + 1) - (2 * j) #+1 to include the option of holding for 0 seconds
			break


print(total)

