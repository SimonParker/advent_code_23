#simon parker

closest_loc = -1
path = "input.txt"

seed_soil = []
soil_fert = []
fert_h2o = []
h2o_lit = []
lit_temp = []
temp_hum = []
hum_loc = []
mappings = [seed_soil, soil_fert, fert_h2o, h2o_lit, lit_temp, temp_hum, hum_loc]

true_intervals = []
'''each sublist [start, end, offset] in here represents an interval in seed-space,
as well as the offset required to move that interval into a new space via a given mapping. gets updated for each mapping, so eventually
we have a mapping for intervals in seed space to location space, and an offset to get there. combine the smallest seed in the interval
with the offset for that interval to get the smallest location for that interval. check for all intervals to get the smallest location
overall'''

def update_true_intervals(mappings):
        old_intervals = true_intervals
        new_intervals = []
        while len(old_intervals) > 0:
                interval = old_intervals[0]
                old_intervals.remove(interval)
                start = interval[0] + interval[2]
                end = interval[1] + interval[2]
                found_match = False
                for mapping in mappings:
                        mapping_interval = [mapping[1], mapping[1] + mapping[2] - 1]
                        overlap = [start if start > mapping_interval[0] else mapping_interval[0],
                                                end if end < mapping_interval[1] else mapping_interval[1]]
                        if overlap[0] <= overlap[1]: #if there is any overlap at all
                                found_match = True
                                new_intervals.append([overlap[0] - interval[2], overlap[1] - interval[2], interval[2] + (mapping[0] - mapping[1])])
                                if start < mapping_interval[0]:
                                        old_intervals.append([start - interval[2], mapping_interval[0] - 1 - interval[2], interval[2]])
                                if end > mapping_interval[1]:
                                        old_intervals.append([mapping_interval[1] + 1 - interval[2], end - interval[2], interval[2]])
                                break
                if not found_match:
                        new_intervals.append(interval)
        return new_intervals


#load file
with open(path, "r") as file:
        sections = [x.split(':')[1] for x in file.read().split('\n\n')]
        file.close()
        seed_intervals = [int(x) for x in sections[0].split(' ') if x != '']

#initialize true_intervals
for i in range(int(len(seed_intervals) / 2)):
        start = seed_intervals[2 * i]
        end = start + seed_intervals[(2 * i) + 1] - 1
        true_intervals.append((start, end, 0))

#initialize mappings
for i in range(1, len(sections)):
        line = [x for x in sections[i].split('\n') if x != '']
        for part in line:
                mappings[i - 1].append([int(x) for x in part.split(' ')])

#update true_intervals for all given mappings
for i in range(len(mappings)):
        true_intervals = update_true_intervals(mappings[i])

#calculate which loc is closest based off of the true_intervals
for i in range(len(true_intervals)):
        if true_intervals[i][0] + true_intervals[i][2] < closest_loc or closest_loc == -1:
                closest_loc = true_intervals[i][0] + true_intervals[i][2]

print(closest_loc)

