# https://www.hackerrank.com/challenges/zipped/problem

# Sample input:
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86
# 91 92 83 89 90.5

x = int(input().split()[1])

student_marks = []

for _ in range(x):
    line = list(map(float, input().split()))
    student_marks.append(line)

# print(student_marks)
# print(list(zip(*student_marks)))

for element in zip(*student_marks):
    print("{:.1f}".format(sum(element) / len(element)))
