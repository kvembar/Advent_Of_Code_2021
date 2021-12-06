#Day 3: Binary Diagnostic
#Keshav V.
#Well, that escalated quickly! That ramp up in difficulty tripped the fuck out of me.
#Didn't help that Alex asked for help either. Slowed me the f down as I had to multitask
#But, I did get it done, i guess.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n") 
    #Gets rid of terminating newline(s) at the end of each line

    return line


################################################SOLUTION################################################
data = []

#Sending raw data to the parser
with open("Day3_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue


################################################PART 1################################################
print("Part 1:")
epsilon = "" #Holds the least common bits in epsilon
gamma = "" #Holds the most common bits in gamma

transpose = ["" for i in range(len(data[0]))] 
#This holds the data, transposed as if it were a matrix.
#The first entry in this array holds all the first bits of the binary numbers, the second entry holds the second bits, etc.


#Creating the transposed matrix
for r in range(len(data)):
    for c in range(len(data[r])):
        transpose[c] += data[r][c]

#Building gamma and epsilon according to prompt. 
#If there are more ones in the first bits, add a 1 to gamma and a 0 to epsilon and vice cersa for more 0s.
for i in transpose:
    if (i.count("0") > i.count("1")):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

#Conversion from binary string to decimal
epsilon = int(epsilon, 2)
gamma = int(gamma, 2)

#Should get 852500 with my data
print(epsilon * gamma)
################################################PART 2################################################
print("Part 2:")

#Holy shit was this a pain in the ass to do... so many errors...

dioxide = "" #Will hold the binary sequence for the CO2 scrubber
oxygen = "" #Will hold the binary sequence for the O2 generator rating
digit_loc = -1 #Specifies which digit we are looking at. Initialized to -1 so that when we enter the loop, we get 0.
scale = 0 #A dummy counter variable
potentials = [i for i in data] #Holds the data before filtering, will slowly get whittled down to one binary number
new_potentials = [] #Holds the data in potentials after filtering

#The meat of the program. While potentials has more than 1 item in it, we do the whittling process
while(len(potentials) != 1):

    digit_loc += 1 #Move to the next digit to analyze
    scale = 0 #Reset counter to 0

    #Count instances of a 1 in the binary at digit_loc.
    for i in potentials:
        if i[digit_loc] == "1":
            scale += 1
        else:
            scale -= 1
    
    #If the count is >= 0, we only look at the ones with a 1 at that position
    #(The equals after > takes care of the preference for 1)
    if(scale >= 0):
        for i in potentials:
            if i[digit_loc] == "1":
                new_potentials.append(i)
    #Else, we only add the binaries with 0 at digit_loc
    else:
        for i in potentials:
            if i[digit_loc] == "0":
                new_potentials.append(i)
    
    #Update potentials with the list of numbers and clear new_potentials for next round.
    potentials = [i for i in new_potentials]
    new_potentials.clear()

oxygen = potentials[0] #Store the only binary number left into oxygen.

#Reinitializing variables and repeating everything from before, 
#except determining dioxide with its own slightly different rules.
digit_loc = -1
scale = 0
potentials = [i for i in data]
new_potentials = []

while(len(potentials) != 1):
    scale = 0
    digit_loc += 1
    for i in potentials:
        if i[digit_loc] == "0":
            scale += 1
        else:
            scale -= 1
    
    #Less than 0 since we're looking for the LEAST common digit. 
    #Same reasoning for the = as before.
    if(scale <= 0):
        for i in potentials:
            if i[digit_loc] == "0":
                new_potentials.append(i)
    else:
        for i in potentials:
            if i[digit_loc] == "1":
                new_potentials.append(i)
    
    potentials = [i for i in new_potentials]
    new_potentials.clear()

dioxide = potentials[0]

#Conversion as before in part 1,
oxygen = int(oxygen, 2)
dioxide = int(dioxide, 2)

#Should get 1007985 with my data
print(oxygen * dioxide)