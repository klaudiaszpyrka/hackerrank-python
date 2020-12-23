# HackerRank https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True

    return leap


years = [2000, 2400, 1800, 1900, 2100, 2200, 2300, 2500]
for y in years:
    print(is_leap(y))
