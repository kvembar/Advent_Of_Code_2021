#Day 4: Giant Squid
#Keshav V.
#Ooooh boy, this one was a beefy one. I can expect the next few problems to be beefy
#Tried to solve it quickly, but had to step away and try it again a bit later.
#When I returned, I solved it in 10 fucking minutes. I'm just happy that I did solve it.

################################################FUNCTIONS################################################

#Parse function used during input after the first line for reading boards
def parse(line):
    line = line.rstrip("\n").split(" ")
    #Gets rid of terminating newline(s) at the end of each line and splits based on spaces

    proper = []
    for i in range(len(line)):
        if line[i] != "":
            #Sometimes there are double spaces and they leave empty strings in the array.
            #This ignores those to avoid issues down the line.
            proper.append(line[i])

    return proper

#Debuting a function for a solution!
#This function does one thing and one thing only: Check for a bingo using the marker I describe in Part 1.

#Note: I made the function return the row/column with a bingo, but I could've just as easily replaced these
#with a true/false and it would've honestly made more sense, but you know... gotta go fast.
def check_board(b):
    #Checking the rows of the board
    for r in b:
        if [i[-1] for i in r] == ["X" for x in r]:
            return r

    #Constructing the column and checking the column for a bingo
    for r in range(len(b)):
        col = []
        for c in range(len(b[r])):
            col.append(b[c][r])
        
        if [i[-1] for i in col] == ["X" for x in col]:
            return col

    return [] #Serves as the 'no bingo detected' signal.

################################################PARSING################################################
bingo = [] #Holds the numbers pulled
boards = [] #Holds the entire set of boards
board = [] #Temporary 2d array storing the board

#Detection for 1st and 2nd lines.
first = True
second = False #<-- I hate that I need this variable, but without it, the program breaks.

#Sending raw data to the parser
with open("Day4_input.txt","r") as f:
    for line in f:
        #Read in the bingo numbers
        if(first):
            bingo = line.split(",")
            first = False
            second = True
            continue

        #Skips the 2nd line for parsing reasons. Without this, one of the boards would be dead empty.
        #In retrospect, should've just manually removed the newline in the input.
        if(second):
            second = False
            continue

        #Newline delimits new boards. Add board to boards and reset board to empty
        if(line == "\n"):
            boards.append(board)
            board = []
        #Parse the line of the board you're reading.
        else:
            board.append(parse(line))

################################################PART 1################################################
print("Part 1:")
matching_board = [] #Will carry the first board that gets a bingo
complete = 0 #Will carry the number that gets the bingo
unmarked = 0 #Will carry the sum of the unmarked numbers.

#For each number in the drawing...
for i in bingo:
    
    #FOURFORLOOPCEPTION
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c in range(len(boards[b][r])):
                #If the number drawn is on the board, mark it with an X at the end. 
                #Will help detect bingos later with check_board.
                if boards[b][r][c] == i:
                    boards[b][r][c] += "X"

                    #The real big brain move.
                    complete = int(i)
                    #Store the number we just marked off. If it results in a bingo, we exit the loop and we have the number that completed the board!
                    #If not, it'll get overwritten by the next number in 'bingo'
    
    #Check to see if we have a bingo in any of the boards
    for board in boards:
        if(check_board(board) != []):
            #If we found a bingo on any of the boards, congrats! 
            #Store it in matching_board and exit the loop.
            matching_board = board
            break
    
    #Found a bingo? No need to look any further. complete also stores the number that made it work.
    if(matching_board != []):
        break

#Calculate unmarked part of the score.
for i in matching_board:
    for j in i:
        if j[-1] != "X":
            unmarked += int(j)

#Should get 44 and 497 for a product of 41668.
print(f"{complete} * {unmarked} = ",complete * unmarked)
################################################PART 2################################################
print("Part 2:")

rem = []
unmarked = 0

#Start fresh. Remove all marked bits of each board and start all over.
for b in range(len(boards)):
    for r in range(len(boards[b])):
        for c in range(len(boards[b][r])):
            if boards[b][r][c][-1] == "X":
                boards[b][r][c] = boards[b][r][c][:-1]

#From the top!
for i in bingo:
    
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c in range(len(boards[b][r])):
                if boards[b][r][c] == i:
                    boards[b][r][c] += "X"
                    complete = int(i)
    
    #Any completed boards are now removed from boards by storing them in rem, removing them, then resetting rem.
    for board in boards:
        if(check_board(board) != []):
            rem.append(board)
    
    for b in rem:
        boards.remove(b)
    rem = []

    #If there's only one board left, its the last board to be completed. Exit the loop.
    if(len(boards) == 1):
        break

#Find the number that gives you bingo and store it in completed
for i in bingo:

    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c in range(len(boards[b][r])):
                if boards[b][r][c] == i:
                    boards[b][r][c] += "X"
                    complete = int(i)
    
    if(check_board(boards[0]) != []):
        break


for i in boards[0]:
    for j in i:
        if j[-1] != "X":
            unmarked += int(j)   

#Should get 31 and 338 for a product of 10478
print(f"{complete} * {unmarked} = ",complete * unmarked)