#Day 8: Seven Segment Search
#This one was a pain in the ass, and how I chose to solve Part 1 and 2 gave me Vietnam flashbacks
#I cheesed Part 1 and it bit me in the ass for Part 2, even though I saw it coming and submitted it late.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n").split(" | ")
    #Gets rid of terminating newline(s) at the end of each line and splits it based on the delimiter

    #Splits the data even further by spaces for conveniences sake.
    line[0] = line[0].split(" ")
    line[1] = line[1].split(" ")

    #Sorts each signal pattern alphabetically. It makes comparison easier for each display.
    for i in line:
        for entry in range(len(i)):
            i[entry] = sorted(i[entry])
            i[entry] = "".join(i[entry])

    return line

#Determines if a certain pattern x is contained in y (x is forced to be smaller than y).
def shared(x, y):
    if(len(x) > len(y)):
        temp = x
        x = y
        y = temp
    for i in x:
        if(i not in y):
            return False
    return True

################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Day8_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue

#Checking the parsing (if necessary):
#print(data[1])

################################################PART 1################################################
print("Part 1:")
#I wasn't kidding when I said I cheesed it. Part 1 is solved in 6 lines, Part 2 needed around 50 lines.
count = 0

for i in data:
    for digit in i[1]:
        #Yeah, I know. I was stupid. All I did was check if the pattern was of length 2,3,4, or 7 and added it to count
        if(len(digit) in [2,3,4,7]):
            count += 1

#Should get 488 from my input
print(count)

################################################PART 2################################################
print("Part 2:")
#Since part 2 required that you decode which pattern belonged to which, this 
total = 0

for display in data:
    key = display[0] #Holds the 10 unique patterns that correspond to 0-9, but not in that order.
    magic = display[1] #Holds the number that we need to translate
    translation = ["" for i in range(10)] #Holds the patterns' translations based on index. 
    #The pattern at index 0 translates to 0, index 2 translates to 2, etc.

    finale = "" #Will hold the final number

    translation[8] = "abcdefg"

    #Firstly, the unique patterns from part 1. Length of 2 means it's a 1 and so on.
    for pattern in key:
        if len(pattern) == 2:
            translation[1] = pattern
        elif len(pattern) == 3:
            translation[7] = pattern
        elif len(pattern) == 4:
            translation[4] = pattern
    
    #The only 7 segment number that contains the pattern for 1 of length 5 is 3,
    #and the only number that does NOT contain the pattern for 1 of length 6 is 6. 
    #We check to see if the signals for 1 are/aren't in each.
    for pattern in key:
        if (len(pattern) == 5 and shared(translation[1], pattern)):
            translation[3] = pattern
        if (len(pattern) == 6 and (not shared(translation[1], pattern))):
            translation[6] = pattern
    
    #Remove the patterns we identified from the key. Helps down the road.
    #I lost a couple hours of coding by putting these inside the loop. Ended up skipping over a bunch of patterns
    #And screwing me over. NEVER .REMOVE() IN A LOOP!
    key.remove(translation[3])
    key.remove(translation[6])
    
    #Finding the letter that encodes the upper right line in the display
    for i in translation[8]:
        if(i not in translation[6]):
            determinant = i
            break
    
    #And use that 'determinant' to distinguish 5 and 2.
    for pattern in key:
        if(len(pattern) == 5 and (determinant in pattern)):
            translation[2] = pattern
        elif(len(pattern) == 5):
            translation[5] = pattern
    
    #Same removal procedure for 2 and 5 to prevent screwups down the line.
    key.remove(translation[2])
    key.remove(translation[5])
    
    #Finding the letter that encodes the bottom left line in the display
    for i in translation[8]:
        if((i not in translation[3]) and (i not in translation[5])):
            determinant = i
            break

    #Using that to distinguish the 0 and 9.
    for pattern in key:
        if((len(pattern) == 6) and (determinant in pattern)):
            translation[0] = pattern
        elif(len(pattern) == 6):
            translation[9] = pattern
    
    #Translating the 4 digit number to actual digits, now that we have the translation scheme.
    for digit in magic:
        finale += str(translation.index(digit))
    
    #Add to total
    total += int(finale)

#Should get 1,040,429 from my input. God that took soooooo long.
print(total)