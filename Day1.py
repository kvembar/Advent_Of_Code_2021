#Day 1: Sonar Sweep (AOC Day 1)
#Keshav V.

#This one was completed very very very late, but I sitll managed to solve it in a good amount of time
#Fell victim to a simple OBOE that would've screwed me over later though and made me lose to the top of
#the leaderboard

#Side note: This is the first time I've coded in Python after doing 261 and 262
#Quite the whiplash to go back to Python from C++!

count = 0 #Dummy variable to keep track of the elevation increase
depth = -99 #Variable to keep track of the depth, set to a negative value to guarantee detection of the first line.

#Part 1
#Opted to do it all while the file was open rather than store it in an array
#In retrospect, probably should've just done it in an array as in part 2.

with open("Day1_input.txt","r") as f:
    for line in f:
        if(depth == -99):
            #First line detection. Store it in depth and continue.
            depth = int(line)
            continue

        #If the current line is bigger than the previosu depth measured, add one to count
        if(int(line) > depth):
            count += 1
        
        #Store value in depth for the next line.
        depth = int(line)

#Should get 1502 with my input.
print(count)

#Part 2
#Similar, better setup.
depths = []
count = 0 #Reset counter
with open("Day1_input.txt","r") as f:
    for line in f:
        depths.append(int(line))

#Adding 3-depth windows together
truedepths = []
for i in range(0, len(depths) - 2): #Fell victim to OBOE here, writing -3 instead of -2. Gotta watch out for them!
    truedepths.append(depths[i] + depths[i+1] + depths[i+2])

#Count depth increases in an easier manner than part 1. Stupid Keshav!
for i in range(0, len(truedepths) - 1):
    if(truedepths[i + 1] > truedepths[i]):
        count += 1

#Should get 1538 with my input
print(count)