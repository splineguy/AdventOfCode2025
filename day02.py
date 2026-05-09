# Read in the input file with only one line of text
from math import ceil, floor


with open("input/day02t1.dat", "r") as f:
    line = f.readline().strip()

# Parse input into a list of tuples
# First, split at commas, then split at hyphens
pairs = []
for part in line.split(","):
    range1, range2 = part.split("-")
    pairs.append((int(range1), int(range2)))

# Count number of values in range that are divisible by x
# count = 0
# sum = 0
# for range1, range2 in pairs:
#     print(range1, range2)
#     length = len(range2)
#     start = int(range1)
#     end = int(range2)
#     xs = []
#     for n in range(length//2):
#         if length % (n+1) == 0:
#             xs.append(str(10**n)*(length//(n+1)))
#     for x in xs[-1:]:
#         x = int(x)
#         init = ceil(start / x) * x
#         for n in range(init, end+1, x):
#             print(n)
#             count += 1
#             sum += n
# print(count)
# print(sum)

sum = 0
for range1, range2 in pairs:
    valid = []
    len1 = len(str(range1))
    len2 = len(str(range2))
    for n in range(len1, len2+1):
        xs = []
        for i in range(n//2):
            if n % (i+1) == 0:
                xs.append(int(str(10**i)*(n//(i+1)))//(10**i))
        for x in xs:
            # print(f'{x=}')
            init = ceil(range1 / x) * x
            # print(f'{init=}')
            for number in range(init, range2+1, x):
                if len(str(number)) == n and number not in valid:
                    print(number)
                    sum += number
                    valid.append(number)
print(sum)