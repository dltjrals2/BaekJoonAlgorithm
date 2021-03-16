# 4344번
from sys import stdin
input = stdin.readline

c = int(input())

for i in range(c):
    sum = 0
    average = 0
    sum_s = 0
    percent = 0
    result = 0
    testCase = list(map(int, input().split()))
    for num in testCase[1:]:
        sum += num

    average = sum / testCase[0]

    for num_s in testCase[1:]:
        if average < num_s:
            sum_s += 1
    percent = sum_s / testCase[0] * 100
    result = round(percent, 3)
    print('{:.3f}%' .format(result))

# 다른 사람 코드
import sys

Case = int(sys.stdin.readline())

for i in range(Case):
    Over = 0

    N = list(map(int, sys.stdin.readline().split()))
    aver = sum(N[1:]) / N[0]
    for j in N[1:]:
        if j > aver:
            Over += 1
    print("%0.3f%" %round((Over / N[0] * 100), 3))
