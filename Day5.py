#Day 5: Hydrothermal Venture
#Did pretty alright for myself here. Certainly didn't go as bad as Day 3 and 4
#Ran into a fair few issues, but nothing too insane! Regex can suck it.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n").split(" -> ") 
    #Gets rid of terminating newline(s) at the end of each line and split it into two strings
    #The first being the starting coordinate and the second being the ending coordinate

    #Splitting them even further into actual arrays of size 2 and then converting them to ints
    start = line[0].split(",") 
    end = line[1].split(",")

    for i in range(2):
        start[i] = int(start[i])
        end[i] = int(end[i])

    if((start[0] == end[0]) or (start[1] == end[1])): #This returns starting and ending coordinates for vents in a horizontal/vertical line
        return [start, end]
    elif(abs(start[0] - end[0]) == abs(start[1]-end[1])): #This returns the coordinates for diagonal lines for part 2.
        return [start, end]
    else:
        return None #Returns None if the line is invalid


################################################PARSING################################################
starting = [] #Contains starting coordinates for vertical and horizontal lines
ending = [] #Ending coordinates for their corresponding starting coordinates
maximum = 0 #Maximum value encountered for constructing the grid. This way, all of lines (even the invalid ones) can be represened

#Diagonal starting and ending coordiantes for Part 2. They hold the same 1-to-1 correspondence as starting and ending above.
diagonals_starting = []
diagonals_ending = []

#Sending raw data to the parser
with open("Day5_input.txt","r") as f:
    for line in f:
        x = parse(line)

        for i in x:
            for j in i:
                if j > maximum:
                    maximum = j

        if((x != None) and ((x[0][0] == x[1][0]) or (x[0][1] == x[1][1]))):
            starting.append(x[0])
            ending.append(x[1])
        elif(x != None): #If the rows and columns are not equal and yet the function does not return None, they're diagonal coordinates
            diagonals_starting.append(x[0])
            diagonals_ending.append(x[1])
        else:
            continue

################################################PART 1################################################
print("Part 1:")
count = 0 #Our answer will be in this number: number of coordinates with value >= 2.

#Constructing the grid based on our identified maximum and initializing them all to 0
grid = [[0 for i in range(maximum + 1)] for j in range(maximum + 1)]

#Constructing and identifying where the vents are.
for i in range(len(starting)): 
    vents = [starting[i], ending[i]] #The current line of vents we are looking at.

    #To help read this code (which, yes, is very very oblique, I am very smooth brained), think of it like this:
    #vents[ 0 = starting coordinates, 1 = ending coordinates ][ 0 = x coordinate, 1 = y coordinate ]

    #Simple swapper for if the identified vents run in reverse so that the range() function does't just go kaput for x and y (thus the range(2) part)
    for x in range(2):
        if(vents[0][x] > vents[1][x]):
            temp = vents[0][x]
            vents[0][x] = vents[1][x]
            vents[1][x] = temp

    #Rows are the same, columns change and add 1 to each of the vals in between
    if(vents[0][0] == vents[1][0]):
        for y in range(vents[0][1], vents[1][1] + 1):
            grid[vents[0][0]][y] += 1
    #Columns are the same, rows change if the rows aren't equal, thanks to our parser
    else: 
        for x in range(vents[0][0], vents[1][0] + 1):
            grid[x][vents[0][1]] += 1

#Calculating the count of numbers >= 2.
for row in grid:
    for val in row:
        if val >= 2:
            count += 1

#Should get 5576 with my puzzle input.
print(count)
################################################PART 2################################################
#I saw what Part 2 would be from a MILE away. Helped to let it sink in faster.
print("Part 2:")

count = 0 #Reset counter to 0

#Continue the code, keeping the same grid from earlier, just adding in the diagonal vents.
for i in range(len(diagonals_starting)):
    x_ascending = True
    y_ascending = True
    vents = [diagonals_starting[i], diagonals_ending[i]] #Same definition as before

    #Identify the direction of the vents by figuring out if x/y are increasing or decreasing in between.
    if vents[1][0] < vents[0][0]:
        x_ascending = False
    if vents[1][1] < vents[0][1]:
        y_ascending = False

    #Redefining vents so that it doesn't just contain the starting and ending, but ALL of the points in between. 
    #range() isn't going to save me here. IT HAS FAILED ME AND SO MANY OTHER AOC PLAYERS IN THIS PART!
    vents = [diagonals_starting[i]]

    #Continue this process until we've hit the ending coordinate.
    while vents[-1] != diagonals_ending[i]:
        coord = [i for i in vents[-1]] #Temporary variable to generate the next coordinate in the line

        #Implementing the 2 bools from earlier
        if(x_ascending):
            coord[0] += 1
        else:
            coord[0] -= 1
        
        if(y_ascending):
            coord[1] += 1
        else:
            coord[1] -= 1
        
        #Add next coordinate in line to vents.
        vents.append(coord)

    #Add 1 to each of the coordinates we've identified
    for c in vents:
        grid[c[0]][c[1]] += 1

#Same counter as before
for row in grid:
    for val in row:
        if val >= 2:
            count += 1

#Should get 18144 from my input.
print(count)