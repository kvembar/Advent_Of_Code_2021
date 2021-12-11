#Day 10: Syntax Scoring
#Just as Day 9 Part 2 used a queue, this uses a stack to keep track of which parentheses are complete
#and which aren't!
#These were a bit painful, but I managed to get them in the end, so I could focus on Day 9.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n") 
    #Gets rid of terminating newline(s) at the end of each line

    return line


################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Day10_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue

################################################PART 1################################################
print("Part 1:")
score = 0
starters = ["{","[","(","<"] #Identifies the starting brackets

for line in data:
    stack = []
    for char in line:
        #The basic process is as follows:
        #1) If we encounter a starting character, we append it to the stack
        #2) If we encounter a terminating character, we remove it's matching front character if its at the top of the stack
        #   If we cannot, we identified a corrupted line. Add to the score and then we move on to the next line.
        if (char in starters):
            stack.append(char)
            continue
        
        if((char == "}") and (stack[-1] != "{")):
            score += 1197
            break
        elif(char == "}"):
            del stack[-1]
            continue

        if((char == "]") and (stack[-1] != "[")):
            score += 57
            break
        elif(char == "]"):
            del stack[-1]
            continue

        if((char == ")") and (stack[-1] != "(")):
            score += 3
            break
        elif(char == ")"):
            del stack[-1]
            continue

        if((char == ">") and (stack[-1] != "<")):
            score += 25137
            break
        elif(char == ">"):
            del stack[-1]
            continue

#Should get 364389 with my input
print(score)
################################################PART 2################################################
print("Part 2:")
#Code is nearly identical here, except for two crucial changes:
#1) We store the scores of the incomplete lines in the array below
#2) Introducing a bool that identifies an incomplete line.

scores = []
incomplete = True
starters = ["(","[","{","<"] #Order is changed to reflect the point values.

for line in data:
    stack = []
    incomplete = True

    for char in line:
        if (char in starters):
            stack.append(char)
            continue

        #This time, if a matching character is not at the top of the stack, its a corrupted, not incomplete line,
        #Thus, the incomplete bool is set to False.

        if((char == "}") and (stack[-1] != "{")):
            incomplete = False
            break
        elif(char == "}"):
            del stack[-1]
            continue

        if((char == "]") and (stack[-1] != "[")):
            incomplete = False
            break
        elif(char == "]"):
            del stack[-1]
            continue

        if((char == ")") and (stack[-1] != "(")):
            incomplete = False
            break
        elif(char == ")"):
            del stack[-1]
            continue

        if((char == ">") and (stack[-1] != "<")):
            incomplete = False
            break
        elif(char == ">"):
            del stack[-1]
            continue

    #If some of the lines were valid, we'd need an extra condition that the stack is empty, 
    #but all of the lines are wrong in some way, so this is what we have instead: nothing.

    #Calculate the score. The stack is in the opposite order of the characters needed to complete it, so we iterate in reverse.
    if(incomplete):
        score = 0
        for ind in range(len(stack)-1,-1,-1):
            i = stack[ind]
            score *= 5
            score += (starters.index(i)) + 1
        
        scores.append(score)
            
#Sort the scores, find the middle.
scores.sort()
mids = int((len(scores) - 1)/2)

#Should get a whopping 2,870,201,088 as the answer!
print(scores[mids])