#simon parker, with help from my dad

pathname = "input.txt"
with open(pathname, "r") as file:
	lines = file.readlines()
	file.close()


times = [x for x in lines[0].split()[1:]]
records = [x for x in lines[1].split()[1:]]

time = int("".join(times))
record = int("".join(records))

print(time)
print(record)

total = 1


for j in range(time):
	value = j * (time - j)
	if value > record:
		total *= (time + 1) - (2 * j) #+1 to include the option of holding for 0 seconds
		break


print(total)

