# 8958번
from sys import stdin
input = stdin.readline

n = int(input().strip())
testCase = []

for i in range(n):
    testCase.append(list(input().strip()))
    score = 0
    count = 0
    for num in testCase[i][0:]:
        if num == 'X':
            count = 0
        elif num =='O':
            count += 1
            score += count
    print(score)
