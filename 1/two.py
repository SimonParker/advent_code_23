#simon parker

#this code loops through each line of the input file. It goes throught that line char by char, checking if that char is a number or the start of a string number. if so it updates the
#digits



total_sum = 0
digit1 = None
digit2 = None 
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

path = "input.txt"

def set_digit(number):
    global digit1
    global digit2
    if digit1 is None:
       digit1 = number
    else:
       digit2 = number

with open(path, "r") as f:
  lines = f.readlines()
  for line in lines:
    digit1 = None
    digit2 = None
    i = 0
    while (i < len(line)):
        if line[i].isnumeric():
            set_digit(int(line[i]))
        else: 
            for word in words:
                if len(word) <= (len(line) - i): #if the remaining space in the line could fit the word
                    if line[i:len(word) + i] == word:
                        set_digit(words.index(word) + 1)
                        break
        i += 1
                
    if digit2 is None:
        digit2 = digit1
    total_sum += (digit1 * 10) + digit2



print(total_sum)
