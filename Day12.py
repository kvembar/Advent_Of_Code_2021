#Day 12: Passage Pathing
#Now introducing Recursion into the mix! I wonder what Day 13 will bring to the table.
#Here, the real meat of the programming (and a majority of my headache for part 2) lies in the functions. The actual code is boring af.
#This one was interesting to do, and really shows off the magic of recursion done properly, unlike last year.

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n").split("-")
    #Gets rid of terminating newline(s) at the end of each line and splits based on the dash

    return line

#And now we're doing Recursion. Deal with it.
def Part1Recurse(paths, visited, node):
    #Base case: we encounter the end, so we have found 1 valid path. Return 1.
    if(node == "end"):
        return 1

    #Recursive case: we have reached a node that isn't the end.
    #The basic process is to find its neighbors, prune out the lowercase smaller caves that we have already visited 
    #and recursively find the number of paths to the end from those neighbors.

    neighbors = paths[node] #Grab the direct neighbors from the graph(dictionary) that we passed in
    trueneighbors = [] #Will hold the actual neighbors we can visit given our visited array.

    #We have visited this node, so append it.
    visited.append(node)

    #If the lowercase neighbor is not in visited, or if its an uppercase bigger cave, we add it.
    for i in range(len(neighbors)):
        if((neighbors[i] not in visited) or (neighbors[i].isupper())):
            trueneighbors.append(neighbors[i])

    #Nums has a member of 0 just in case we hit a dead-end pathway. Therefore, 0 valid paths from this neighbor.
    nums = [0]

    for x in trueneighbors:
        #For each of these neighbors, 
        nums.append( Part1Recurse(paths, visited, x) )

    #Remove the last element of visited (beacuse Python always passes variables by reference and we analyzed every possible path from this node)
    #and return the sum of the number of pathways.
    del visited[-1]
    return sum(nums)

#This one is nearly identical to Part 1, except for a small set of 10 or so lines that makes the magic work.
#Initially, the first solution generated ALL paths that visited any number of lowercase caves twice, and then we throw away
#the ones that visited more than one lowercase cave twice. It worked fine for the smaller examples, but it took FOREVER
#for the actual input. We're talking longer than 20 minutes to execute. I was planning on sleeping on it... again, but a
#better solution came to me, and it executed in about 5 seconds.
def Part2Recurse(paths, visited, node):
    #Base case
    if(node == "end"):
        #print(visited)
        return 1

    #Recursive case
    neighbors = paths[node]
    trueneighbors = []
    visited.append(node)

    for i in range(len(neighbors)):
        
        #Our detection to see if we can visit a lowercase cave twice
        twice = False #A bool to detect if we already visited a lowercase cave twice
        uniq = {i for i in visited} #A set holding the unique caves we visited

        #If we visited a lowercase cave twice, we can't do it again, and set the bool to true.
        for x in uniq:
            if(visited.count(x) == 2 and not x.isupper()):
                twice = True
                break
        
        #If we haven't visited a lowercase cave twice, we can add a lowercase cave we encountered to the list of neighbors.
        #That particular path will have twice resolve to true, in which case, we switch back to if its not in the list at all or if its upper, like in Part 1.
        if(not twice):
            if( ((visited.count(neighbors[i]) < 2) and (neighbors[i] != "start")) or (neighbors[i].isupper()) ):
                trueneighbors.append(neighbors[i])
        else:
            if((neighbors[i] not in visited) or (neighbors[i].isupper())):
                trueneighbors.append(neighbors[i])


    nums = [0]

    for x in trueneighbors:
        nums.append( Part2Recurse(paths, visited, x) )

    del visited[-1]
    return sum(nums)
################################################PARSING################################################
data = []

#Sending raw data to the parser
with open("Day12_input.txt","r") as f:
    for line in f:
        data.append(parse(line))
        continue


################################################PART 1################################################
print("Part 1:")
#Construct the graph in a dictionary
graph = {}

#For each entry in graph, construct each edges going both ways
for i in data:
    if(i[0] not in graph):
        graph[i[0]] = [i[1]]
    else:
        graph[i[0]].append(i[1])
    
    if((i[1] not in graph)):
        graph[i[1]] = [i[0]]
    else:
        graph[i[1]].append(i[0])

#Should get 3497.
#The parameters take in the graph to analyze, the array of caves we visited, and the node we're analyzing (intialized to 'start')
print(Part1Recurse(graph, [], "start"))
################################################PART 2################################################
print("Part 2:")

#Should get 93686 from my input. Who knew one little change could cause so much headache.
print(Part2Recurse(graph, [], "start"))