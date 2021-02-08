# HackerRank https://www.hackerrank.com/challenges/minimum-swaps-2/problem 

def minimumSwaps(arr):
    swaps = 0
    
    for i in range(len(arr)):
        # go to next iteration if the element is in the right place
        if arr[i] == i + 1:  
            continue
        else:
            # while the element is not in the right place...
            while arr[i] != i + 1:  
                temp = arr[i]
                # swap: the element arr[i] goes to its right place, gets replaced by whatever was in its place
                arr[i], arr[temp-1] = arr[temp-1], arr[i]   
                swaps += 1
     
    return swaps

# sample input format
# 4
# 4 3 1 2

n = int(input())
arr = list(map(int, input().rstrip().split()))
print(minimumSwaps(arr))
