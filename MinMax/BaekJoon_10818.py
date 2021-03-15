# 10818번
n = int(input())
a = list(map(int, input().split(' ')))

a.sort()
print(a[0], a[n-1])

# 다른 사람 코드
import sys

a, b* = map(int, sys.stdin.read().split())
print(min(b), max(b))
