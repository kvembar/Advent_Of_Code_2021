#Day 7: The Treachery of Whales
#Crabs were my bane last year, and who saves me from the whale? A fucking crab.
#This one was a speedy boi to solve, and I got a rank just over 2000 with my solve
#There's a lot of clever ways to solve it, but I went with just the direct version.
#Computers are fast, and the determinant should be my balance of coding speed and efficiency

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n").split(",")
    #Gets rid of terminating newline(s) at the end of each line and formats it into the data

    for i in range(len(line)):
        line[i] = int(line[i])

    return line


################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Day7_input.txt","r") as f:
    for line in f:
        data = parse(line) #Rather than append the data, since it's one line, just set it equal.
        continue


################################################PART 1################################################
print("Part 1:")
costs = [] #Keeps the total cost of fuel for the submarines given a certain point they're conglomerating to.
max_x = max(data) #Holds the max of the data
min_x = min(data) #Holds the min of the data

#If the crabs move anywhere outside the range of the mins and maxes, its just wasted energy
#Some people smarter than I ever was or could figured out an O(1) solution that involves means and medians
#But fuck that, I needed speed.

#Calculate how much fuel itll cost for a crab submarine to get to a given line
for i in range(min_x, max_x + 1):
    cost = 0
    for c in data:
        cost += abs(c-i)
    
    costs.append(cost)

#Should get the minimum cost as 349357
print(min(costs))
################################################PART 2################################################
print("Part 2:")

costs = []

#Here, the cost of fuel for a submarine is related to the triangle numbers, so the fuel cost will be calculated from this.
#In this, the nth members is the nth triangle number, which is critical for the loop below
triangle_nums = [i*(i+1)/2 for i in range(max_x-min_x + 1)]


#Calculate new costs
for i in range(min_x, max_x + 1):
    cost = 0
    for c in data:
        cost += triangle_nums[abs(c-i)] #The cost is the nth triangular number, where n is the distance traveled.

    costs.append(cost)

#You'll get 96708205 for the minimum costs. Hopefully gas is not in shortage...
print(min(costs))