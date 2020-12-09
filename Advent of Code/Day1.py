file  = open("Day1.txt", "r")
contents = list()

for line in file:
    try:
        contents.append(int(line))
    except:
        continue

for x in contents:
    for y in contents:
        for z in contents: # Part 2
            if y + x + z == 2020:
                print(y, x, z)
                quit()
