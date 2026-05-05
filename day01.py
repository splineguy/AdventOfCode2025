# open input/day01t1.dat and read the lines into a list

with open("input\\day01p1.dat") as f:
    lines = f.readlines()

# convert the lines to integers and store them in a list
# each line is L## or R## where ## is a number

directions = []
for line in lines:
    line = line.strip()
    direction = line[0]
    steps = int(line[1:])
    directions.append((direction, steps))

### Part 1

# loc = 50
# pw = 0

# for direction, steps in directions:
#     if direction == "L":
#         loc = (loc - steps) % 100
#     elif direction == "R":
#         loc = (loc + steps) % 100
#     if loc == 0:
#         pw += 1
    
# print(f"Final location: {loc}, Password: {pw}")


### Part 2
loc = 50
pw = 0
pre = loc

for direction, steps in directions:
    pre = loc
    if direction == "L":
        loc = (loc - steps)
        while loc < 0:
            loc += 100
            pw += 1
        if pre == 0:
            pw -= 1
    elif direction == "R":
        loc = (loc + steps)
        while loc > 100:
            loc -= 100
            pw += 1
        loc = loc % 100

    if loc == 0:
        pw += 1

    

    
    print(f"Direction: {direction}, Steps: {steps}, Location: {loc}, Password: {pw}")

print(f"Final location: {loc}, Password: {pw}")