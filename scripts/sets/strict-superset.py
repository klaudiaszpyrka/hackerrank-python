# HackerRank https://www.hackerrank.com/challenges/py-check-strict-superset/problem 

superset_to_test = set([int(x) for x in input().split(" ")])
#print(superset_to_test)
#print(len(superset_to_test))

other_sets = []
n = int(input())

for _ in range(n):
    other_sets.append(set([int(x) for x in input().split(" ")]))

#print(other_sets)

for other_set in other_sets:
    #print(len(other_set))
    if (not other_set.issubset(superset_to_test)) or (len(superset_to_test) <= len(other_set)):
        print(False)
        break
else:
    print(True)
    