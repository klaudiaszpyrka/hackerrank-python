# https://www.hackerrank.com/challenges/python-sort-sort/problem

# Sample input:
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

nm = input().split()
n = int(nm[0])
m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

# sort an object using some of object's indices as keys
arr_sorted = sorted(arr, key=lambda arr_unsorted: arr_unsorted[k])

for a in arr_sorted:
    print(*a)  # print the elements of a list separated by space on one line
