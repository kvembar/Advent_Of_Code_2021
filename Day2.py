#Day 2: Dive!
#Keshav V.
#For this AOC, I caved and made myself a template (partially inspired by @sumnerevans' format)
#This day's problem was solved hella fast, but I could've been a bit faster tbh

################################################FUNCTIONS################################################

#Parse function used during input. 
#This will make debugging hella easier, along with this function section.
#Expect to see some common comments and structure between days.
def parse(line):
    line = line.rstrip("\n").split(" ")
    #Gets rid of terminating newline(s) at the end of each line and splits based on the space
    #This creates an array of size 2 arrays, where line[0] is the direction and line[1] is the value

    return line


################################################SOLUTION################################################
data = []

#Sending raw data to the parser
with open("Day2_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue


################################################PART 1################################################
print("Part 1:")

forward = 0 #Stores the amount forward we have moved (x-coordinate)
depth = 0 #Stores the depth we have moved to (y-coordinate)

#Scan through data, find the instruction and edit x and y accordingly
for i in data:
    if(i[0] == "forward"):
        forward += int(i[1])
    elif(i[0] == "up"):
        depth -= int(i[1])
    else:
        depth += int(i[1])
    #Since there wasn't a 'backwards' instructions, why code for it? Throw it into the else!

#Should get a horizontal of 1815 and a vertical of 908 for a product of 1648020 from my data.
print(f"{forward} * {depth} = ")
print(forward * depth)

################################################PART 2################################################
print("Part 2:")
#Reset variables and add 'aim' variable.
aim = 0
forward = 0
depth = 0

#Scan through data, this time editing aim accordingly and changing depth accordingly
for i in data:
    if(i[0] == "forward"):
        forward += int(i[1])
        depth += int(i[1]) * aim
    elif(i[0] == "up"):
        aim -= int(i[1])
    else:
        aim += int(i[1])

#Should get a horizontal of 1815 as before, but now with a vertical of 969597 for a total of 1759818555.
#I should be getting the submarine equivalent of airmiles (seamiles?) for this. Note: also kill that one elf that lost the keys in the first place.
print(f"{forward} * {depth} = ")
print(forward * depth)