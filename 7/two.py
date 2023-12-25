#simon parker


path = "input.txt"

with open(path, "r") as file:
	lines = file.readlines()
	file.close

hands = []


for line in lines:
	hand = (line.split()[0], int(line.split()[1].strip()))
	hands.append(hand)

card_nums = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
				'4': 4, '3': 3, '2': 2}
fives = []
fours = []
full_hs = []
threes = []
twos = []
ones = []
HKs = []

def classify_hand(hand_tuple):
	hand = hand_tuple[0]
	x = {}
	for i in range(len(hand)):
		if hand[i] in x:
			x[hand[i]] += 1
		else:
			x[hand[i]] = 1
	length = len(x)
	match length:
		case 1:
			fives.append(hand_tuple)
			return
		case 2:
			if 'J' in x:
				fives.append(hand_tuple)
				return
			else:
				for value in x.values():
					if value == 4:
						fours.append(hand_tuple)
						return
				full_hs.append(hand_tuple)
				return
		case 3:
			if 'J' in x:
				has_pair = False
				for value in x.values():
					if value == 2:
						has_pair = True
				if has_pair and x['J'] == 1:
					full_hs.append(hand_tuple)
					return
				else:
					fours.append(hand_tuple)
					return
			else:
				for value in x.values():
					if value == 3:
						threes.append(hand_tuple)
						return
				twos.append(hand_tuple)
				return
		case 4:
			if 'J' in x:
				threes.append(hand_tuple)
				return
			else:
				ones.append(hand_tuple)
				return
		case 5:
			if 'J' in x:
				ones.append(hand_tuple)
				return
			else:
				HKs.append(hand_tuple)
				return
		case _:
			print("???")
			return
				

def compare_hands(hand1, hand2):
	for i in range(5):
		if card_nums[hand1[i]] > card_nums[hand2[i]]:
			return hand1
		elif card_nums[hand1[i]] < card_nums[hand2[i]]:
			return hand2
	
def bubble_sort(list_of_hands):
	for i in range(len(list_of_hands)):
		for j in range(len(list_of_hands) - 1):
			h1 = list_of_hands[j][0]
			h2 = list_of_hands[j + 1][0]
			bigger_hand = compare_hands(h1, h2)
			if bigger_hand == h1:
				list_of_hands[j], list_of_hands[j + 1] = list_of_hands[j + 1], list_of_hands[j]


for hand in hands:
	classify_hand(hand)




bubble_sort(fives)
bubble_sort(fours)
bubble_sort(full_hs)
bubble_sort(threes)
bubble_sort(twos)
bubble_sort(ones)
bubble_sort(HKs)

all_hands_sorted = []

list_of_lists = [HKs, ones, twos, threes, full_hs, fours, fives]

for listt in list_of_lists:
	for value in listt:
		all_hands_sorted.append(value)

sums = 0

for i in range(len(all_hands_sorted)):
	sums += (i + 1) * (all_hands_sorted[i][1])

print(sums)
