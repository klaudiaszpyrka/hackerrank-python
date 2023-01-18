# https://www.hackerrank.com/challenges/list-comprehensions/problem

x = 1
y = 1
z = 1
n = 2

# coordinates = []

# for i in range(x+1):
#    for j in range(y+1):
#        for k in range(z+1):
#            coordinates.append([i, j, k])

coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
valid_permutations = [c for c in coordinates if sum(c) != n]

print(valid_permutations)
