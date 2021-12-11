#Day 9: Smoke Basin
#Because of extraneous circumstances in my life, I was not in a headspace to complete this problem
#When it was done. I attempted this problem on Day 10, and solved it with a delta of 12 minutes.
#This one was actually quite fun to do, as Day 9 and Day 10 are like two sides of the same coin.
#Day 10 (both parts) was solved with a stack, and Day 9 (part 2) was solved with a queue!

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = list(line.rstrip("\n"))
    #Gets rid of terminating newline(s) at the end of each line and turns it into
    #a character-wise list.

    for i in range(len(line)):
        line[i] = int(line[i]) #Turn all the numbers into ints for comparison and solving purposes

    return line

#Returns the values of the neighbors (if they exist) of a cell at a given index in the grid.
#(Index being a vector of size two with row and col coordinates)
def neighbors(grid, index):
    n = []
    if(index[0] != 0):
        n.append(grid[index[0] - 1][index[1]])
    
    if(index[0] != len(grid) - 1):
        n.append(grid[index[0] + 1][index[1]])
    
    if(index[1] != 0):
        n.append(grid[index[0]][index[1] - 1])
    
    if(index[1] != len(grid[index[0]]) - 1):
        n.append(grid[index[0]][index[1] + 1])
    
    return n

#Returns the coordinates of the neighbors of a cell at a given index in the grid.
def neighbors_coord(grid, index):
    n = []
    if(index[0] != 0):
        n.append([index[0] - 1, index[1]])
    
    if(index[0] != len(grid) - 1):
        n.append([index[0] + 1, index[1]])
    
    if(index[1] != 0):
        n.append([index[0], index[1] - 1])
    
    if(index[1] != len(grid[index[0]]) - 1):
        n.append([index[0], index[1] + 1])
    
    return n
################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Day9_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue

################################################PART 1################################################
print("Part 1:")
risklevel = 0
seeds = []

#Simple checker to see if a given cell is smaller than its neighbors
for r in range(len(data)):
    for c in range(len(data[r])):
        if(data[r][c] < min(neighbors(data, [r,c]))):
            seeds.append([r,c]) #If we found a low point, it will be in its own basin. Save its coordinate for part 2
            risklevel += data[r][c] + 1

#Should get 528 from my given input
print(risklevel)
################################################PART 2################################################
print("Part 2:")
basin_sizes = [] #Will store the basin sizes corresponding to the seeds identified earlier

for seed in seeds:

    basin = [seed]
    
    #Simple BFS Search by iterating through the list.
    for s in basin:
        m = neighbors_coord(data, s)
        for potential_neighbor in m:
            #We skip over the potential neighbors we already identified and the 'walls' of the area idenitified with a 9.
            if(potential_neighbor in basin):
                continue

            if(data[potential_neighbor[0]][potential_neighbor[1]] == 9):
                continue

            #We will eventually identify ITS neighbors until there are none left to look for.
            basin.append(potential_neighbor)
    
    basin_sizes.append(len(basin))

#Sort and print the sizes of the basins
#Should get 920448 from my input.
basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])