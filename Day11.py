#Day 11: Dumbo Octopus
#Part 1 was ROUGH AS HELLLLLLLL, but with a lot of perseverance

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = list(line.rstrip("\n"))

    for i in range(len(line)):
        line[i] = int(line[i])

    return line

#Similar neighbors_coord from Day 9, but a bit more robust and including diagonals.
#This function was a pain in my ass to code, and had at least 3 different code-breaking errors, because I thought I was clever.
def neighbors_coord(grid, index):
    n = []
    
    #These four bools indicate if we're at the top, bottom, leftmost, or rightmost position in the grid.
    top = (index[0] == 0)
    bottom = (index[0] == len(grid) - 1)
    left = (index[1] == 0)
    right = (index[1] == len(grid[0]) - 1)
    
    #Adding to the list depending on where we are in the grid.
    if(not top):
        n.append([index[0] - 1, index[1]])
        if(not left):
            n.append([index[0] - 1, index[1] - 1])
        if(not right):
            n.append([index[0] - 1, index[1] + 1])
    
    if(not left):
        n.append([index[0], index[1] - 1])
        
    if(not right):    
        n.append([index[0], index[1] + 1])
    
    if(not bottom):
        n.append([index[0] + 1, index[1]])
        if(not left):
            n.append([index[0] + 1, index[1] - 1])
        if(not right):
            n.append([index[0] + 1, index[1] + 1])

    return n

################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Day11_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue

################################################PART 1################################################
print("Part 1:")
flashes = 0

#*Gets Day 6 and Conway Cube Vietnam Flashbacks*
#I was fully prepared to deal with efficiency problems or if worst comes to worst, running it overnight again,
#But PArt 2 was a pleasant surprise in that... well, you'll see.

for day in range(100):

    #Increasing the energy level of each octopus by one, wrapping back to 0 in the case of a flash.
    for r in range(len(data)):
        for c in range(len(data[r])):
            data[r][c] = (data[r][c] + 1) % 10
    
    #Stores the coordinates of the octopi that will flash
    flashing = []

    for r in range(len(data)):
        for c in range(len(data[r])):
            if(data[r][c] == 0):
                flashing.append([r,c])
    
    #Stores the coordinates of the octopi energy levels we need to add to due to the other cells flashing
    add_to = []

    for x in flashing:
        neighbors = neighbors_coord(data, x)

        for n in neighbors:
            add_to.append(n)
    
    for n in add_to:
        #Increment neighbors by one if they already aren't flashed
        if(data[n[0]][n[1]] != 0):
            data[n[0]][n[1]] = (data[n[0]][n[1]] + 1)%10

            #But: this was my Achilles Heel to deal with. If the neighboring cells bring the energy value all the way up to 0,
            #We need to add ITS neighbors to add_to, so that way they are accounted for in the calculation.
            if(data[n[0]][n[1]] == 0):
                neighbors = neighbors_coord(data, n)
                for x in neighbors:
                    add_to.append(x)
                       
    #Count the number of flashes.
    for r in data:
        for c in r:
            if c == 0:
                flashes += 1

#Should get 1673. Pretty small and tame number
print(flashes)

################################################PART 2################################################
print("Part 2:")
synchronized = False
days = 100

#ALL of this code is copy paste from Part 1 except for the last for loop, which merely checks to see if the octopi and synchronized
#I fully expected this to take like a trillion days, but it ended up with a surprisingly small number that I could brute force.
while(not synchronized):
    synchronized = True
    days += 1

    for r in range(len(data)):
        for c in range(len(data[r])):
            data[r][c] = (data[r][c] + 1) % 10
    
    flashing = []

    for r in range(len(data)):
        for c in range(len(data[r])):
            if(data[r][c] == 0):
                flashing.append([r,c])
    
    add_to = []

    for x in flashing:
        neighbors = neighbors_coord(data, x)

        for n in neighbors:
            add_to.append(n)
    
    for n in add_to:
        if(data[n[0]][n[1]] != 0):
            data[n[0]][n[1]] = (data[n[0]][n[1]] + 1)%10

            if(data[n[0]][n[1]] == 0):
                neighbors = neighbors_coord(data, n)
                for x in neighbors:
                    add_to.append(x)
    
    #Check to see if they're synchronized.
    for r in data:
        for c in r:
            if c != 0:
                synchronized = False
                break
        if (not synchronized):
            break

#Should get 279 steps (I called it days, since I was rushing.) 
#Rather small by all accounts, and I get the answer incredibly fast!
print(days)