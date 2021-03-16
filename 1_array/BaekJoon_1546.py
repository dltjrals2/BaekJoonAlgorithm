# 1546번
import sys

n = int(sys.stdin.readline())
array = list(map(int, input().split(' ')))
max = max(array)
sum = 0

for i in range(n):
    array[i] = (array[i] / max) * 100
    sum += array[i]

print(sum / n)

# 다른 사람 코드
from sys import stdin
input = stdin.readline

count = int(input())
score = list(map(int, input().split()))
mx_score = max(score)
new_score = []

for num in score:
    n_num = num / mx_score * 100
    new_score.append(n_num)

sum = 0
for num in new_score:
    sum += num
print(sum / count)
