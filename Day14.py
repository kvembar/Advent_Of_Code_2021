#Day 14: Extended Polymerization

################################################FUNCTIONS################################################

#Parse function used during input
def parse(line):
    line = line.rstrip("\n").split(" -> ")
    #Gets rid of terminating newline(s) at the end of each line and split based on delimiter

    return line

def step(init, pairs):
    inserted = []
    for i in range(len(init) - 1):
        l = "".join(init[i:i+2])
        inserted.append(pairs[l])
    
    r = []
    for i in range(len(init) - 1):
        r.append(init[i])
        r.append(inserted[i])
    r.append(init[-1])

    return r


################################################PARSING################################################
rules = dict()
start = ""
chain = ""

#Sending raw data to the parser
with open("Day14_input.txt","r") as f:
    for line in f:
        if(chain == ""):
            chain = line.rstrip("\n")
            start = line.rstrip("\n")
            continue
        
        p = parse(line)
        rules[p[0]] = p[1]
        continue

################################################PART 1################################################
print("Part 1:")

for steps in range(10):    
    chain = step(chain, rules)

counts = dict()

for i in chain:
    if i not in counts:
        counts[i] = 0
    else:
        counts[i] += 1

print(max(counts.values()) - min(counts.values()))
################################################PART 2################################################
print("Part 2:")

hashings = dict()
truecounts = dict()

for key in rules.keys():
    hashings[key] = 0

for i in range(len(start) - 1):
    hashings[start[i:i+2]] += 1

    if(start[i] in truecounts):
        truecounts[start[i]] += 1
    else:
        truecounts[start[i]] = 1

if(start[-1] in truecounts):
    truecounts[start[-1]] += 1
else:
    truecounts[start[-1]] = 1

for steps in range(40):
    new_hashings = dict()
    for key in hashings.keys():
        new_hashings[key] = 0
    
    for key in hashings.keys():
        add_to = [key[0] + rules[key], rules[key] + key[1]]
        magnitude = hashings[key]
        
        new_hashings[key[0] + rules[key]] += magnitude
        new_hashings[rules[key] + key[1]] += magnitude

        if(magnitude > 0):
            if(rules[key] in truecounts):
                truecounts[rules[key]] += magnitude
            else:
                truecounts[rules[key]] = magnitude

    hashings = new_hashings

print(max(truecounts.values()) - min(truecounts.values()))