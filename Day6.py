#Day 6: Lanternfish (Keshav V.)
#An efficiency problem. THE CRAB RETURNS WITH A VENGENANCE INDEED!
#BUT I FUCKING GOT IT, AND I DIDN'T HAVE TO WAIT OVERNIGHT FOR IT TO RUN!

#Explanation time: last year, the Crab card game was an efficiency problem much like this one.
#I legitimately took the naive solution of my code and let it run overnight. 
#No, I'm not joking and I have the repo to prove it.
#I was fully ready to let this one run overnight like last time when Part 2 came,
#but I RAN OUT OF RAM HALFWAY THROUGH (no cap, seriously!) so I was forced to adapt.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n").split(",")
    #Gets rid of terminating newline(s) at the end of each line.
    
    for i in range(len(line)):
        line[i] = int(line[i])

    return line


################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Day6_input.txt","r") as f:
    for line in f:
        data = parse(line)
        continue

################################################PART 1################################################
print("Part 1:")

#This is essentially the naive solution. In retrospect, probably should've seen the efficiency problem a mile away.
#This solution, despite having fewer days simulated, runs SLOWER than Part 2 with more days.
#If that doesn't speak to how much I needed CSCI 262, I don't know what does.

for day in range(80):

    for i in range(len(data)):
        #Simulates each day according to the instructions.
        if data[i]>0:
            data[i] -= 1
    
        elif data[i] == 0:
            data[i] = 6
            data.append(8)

#Should get 388419 with my long-ass input
print(len(data))
################################################PART 2################################################
print("Part 2:")

#Reset data from earlier back to the initial day.
with open("Day6_input.txt","r") as f:
    for line in f:
        data = parse(line)
        continue

#Hashtable (thanks CS262!) holding the number of lanternfish a number of days away from spawning
count = [0 for i in range(9)]

#Initialize data based on initial population for i in data:
for i in data:
    count[i] += 1

#Now, for each day...
for day in range(256):

    #Noting how many fish are about to spawn
    new_eights = count[0]

    #Shift all fish in a+1 down to a days until spawning
    for i in range(8):
        count[i] = count[i+1]
    
    #Set number of eights to the number of 0s we saw earlier, and all the 0s become 6s.
    count[8] = new_eights
    count[6] += new_eights

#Count the total number of fish in hashtable
total = 0
for i in count:
    total += i

#Should get.. get this: 1,740,449,478,328 (1.7 trillion) after 256 days.
#Lanternfish put rabbits to shame by sheer numbers!
print(total)