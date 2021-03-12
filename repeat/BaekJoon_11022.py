# 11022번
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i + 1, a, b, a + b))


# 다른 사람 코드
import sys

n = int(input())

for n in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{n+1}: {a} + {b} = {a+b}')
