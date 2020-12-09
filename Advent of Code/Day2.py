file  = open("Day2.txt", "r")
contents = list()

for line in file:
    line = line.split()
    contents.append(line)

valid = 0

'''
# Part 1
for x in contents:
    times = 0

    minimum = x[0].split("-")
    maximum = int(minimum[1])
    minimum = int(minimum[0])

    x[1] = x[1].strip(":")

    for y in x[2]:
        if x[1] == y:
            times = times + 1
    
    if maximum >= times >= minimum:
        valid = valid + 1

print(valid)
'''

# Part 2
for x in contents:
    times = 0

    instance = x[0].split("-")
    secondposition = int(instance[1]) - 1 # With -1 it works on index 0
    firstposition = int(instance[0]) - 1

    x[1] = x[1].strip(":")

    iterating = list(x[2])

    if (iterating[firstposition] == x[1] and iterating[secondposition] != x[1]) ^ (iterating[firstposition] != x[1] and iterating[secondposition] == x[1]):
        valid = valid + 1

print(valid)