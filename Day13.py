#Day 13: Transparent Origami
#NEW RECORD FOR RANK (2409/1746) AND DELTA (3m16s) LESS GOOOOOO
#But nah, in all seriousness, this was a very fun problem. Part 2 was completely expected
#And unexpected at the same time. It's actually kinda cool!
#Thankfully, Part 1 telegraphed Part 2 so goddamn hard that I could gain the foresight to create a fold function to make Part 2 easier
#And to have a crazy delta like 3:16 (not the Bible verse, tho).

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n").split(",")
    #Gets rid of terminating newline(s) at the end of each line

    #Turns all the coordinates into ints, you know the drill.
    for i in range(len(line)):
        line[i] = int(line[i])

    return line

#Our magical fold function. I'm glad that Part 2 was obvious (but not so obvious in what they were looking for)
#This fold function works on the magic of knowing that the folds will always be perfectly in half.
#If the folds weren't in half, idk what the heck I would do.
def fold(axis, val, grid):
    new_grid = [] #What we will return.

    #Y and X are nearly identical, just with some things swapped, so I'll only explain the axis = y case.
    if(axis == "y"):
        #y is only going up to the fold's coordinate, stored in 'val'
        for y in range(val):
            new_row = []
            #x however, is going all the way across.
            for x in range(len(grid[y])):
                #If either a given coordinate or it's reflection across the fold assuming the fold is perfectly halfway (-1 to prevent an OBOE) is a hashtag,
                #Then the folded version will also be a hashtag.
                if(grid[y][x] == "#" or grid[len(grid)-1-y][x] == "#"):
                    new_row.append("#")
                #Otherwise, it'll just be empty
                else:
                    new_row.append(".")
            new_grid.append(new_row) #Append the new row to the folded grid.
        return new_grid

    elif(axis == "x"):
        for y in range(len(grid)):
            new_row = []
            for x in range(val):
                if(grid[y][x] == "#" or grid[y][len(grid[y])-1-x] == "#"):
                    new_row.append("#")
                else:
                    new_row.append(".")
            new_grid.append(new_row)
        return new_grid

################################################PARSING################################################
data = [] #Holds coordinates for the dots on the grid
instructions = [] #Holds folding instructions. Each element contains the axis of the fold followed by the coordinate of the fold

#Sending raw data to the parser
with open("Day13_input.txt","r") as f:
    for line in f:
        #Skip the empty line separating the coordinates from the fold instructions
        if(line == "\n"):
            continue

        #Detect if our line is folding instructions by the first letter 'f'
        if(line[0] != "f"):
            data.append(parse(line))
        else:
            line = line.rstrip("\n").split(" ")
            instructions.append(line[-1].split("="))


################################################PART 1################################################
print("Part 1:")
#Note: x refers to columns, y refers to rows keeping in line with the question's description.

#Holds the first fold instruction.
direction = instructions[0]

#Learnt my lesson from Day 5. No need to construct a for loop to find the max when Python already has this lol.
max_x = max([i[0] for i in data])
max_y = max([i[1] for i in data])

#Construct the grid accurate to maximum coordinates of x and y. No cheesing it like in Day 5, since the coordinates matter.
grid = [["." for i in range(max_x + 1)] for j in range(max_y + 1)]

#Marking the grid according to the data.
for coord in data:
    grid[coord[1]][coord[0]] = "#"

#Run the fold in accordance with the fold function.
folded_map = fold(direction[0],int(direction[1]),grid)

#Simple hash counter.
c = 0
for i in folded_map:
    for j in i:
        if j == "#":
            c += 1

#Should get 747 from my data! (Looks like the infrared manufacturers are big fans of Boeing?)
print(c)
################################################PART 2################################################
print("Part 2:")
#This part was really cool, since instead of a number, you get a sequence of letters in ASCII Art.
#Props to the creator of this problem, this one was a cool one, made even cooler by how I called it!

#Resetting the grid to before the fold... I... don't know why I did this, but I guess I wanted to be sure that it was reset?
#Even though the grid wasn't tampered with? IDK, I guess I was a bit too excited.
max_x = max([i[0] for i in data])
max_y = max([i[1] for i in data])

grid = [["." for i in range(max_x + 1)] for j in range(max_y + 1)]

for coord in data:
    grid[coord[1]][coord[0]] = "#"

#Now run all the fold instructions, updating the grid each time.
for i in instructions:
    grid = fold(i[0], int(i[1]), grid)

#If you read this ASCII Art, You should get ARHZPCUH from my data.
for i in grid:
    for j in i:
        if(j == "#"):
            print(j, end = "")
        else:
            print(" ", end = "")
    print("")

#I probably would've gotten a delta sub 3 minutes if I wasn't a goober and 
#1) Not bothered with resetting the grid, it wasn't necessary.
#2) Misread the ASCII art as ARHZPOUH because of the dots (in an earlier version of the code, this removes the dots) and costed myself a minute.