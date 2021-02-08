# HackerRank https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    
    list = []

    for n in range(N):
        exp = input().split(" ")
        if exp[0] == "insert":
            list.insert(int(exp[1]), int(exp[2]))
        elif exp[0] == "print":
            print(list)
        elif exp[0] == "remove":
            list.remove(int(exp[1]))
        elif exp[0] == "append":
            list.append(int(exp[1]))
        elif exp[0] == "sort":
            list.sort()
        elif exp[0] == "pop":
            list.pop()
        elif exp[0] == "reverse":
            list.reverse()
