#simon parker


import re

path = "input.txt"
total_sum = 0

gear_records = []

with open(path, "r") as file:
	Lines = file.readlines()
	file.close()

digits = []
gear_locations = []

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
                                        if str(char) == "*":
                                                gear_locations.append(f"{row} {col}")

                elif len(digits) != 0:
                        num = int(''.join(digits))
                        digits = []
                        gear_locations = list(set(gear_locations)) #stripping away duplicates
                        for location in gear_locations:
                                new_record = {
                                        "loc":location,
                                        "times_touched":1,
                                        "touched_by":[num]
                                }
                                touched_previously = False
                                for record in gear_records:
                                        if record["loc"] == location:
                                                record["times_touched"] += 1
                                                record["touched_by"].append(num)
                                                touched_previously = True
                                if not touched_previously:
                                        gear_records.append(new_record)
                        gear_locations = []


for record in gear_records:
        if record["times_touched"] == 2:
                total_sum += record["touched_by"][0] * record["touched_by"][1]

print(total_sum)
