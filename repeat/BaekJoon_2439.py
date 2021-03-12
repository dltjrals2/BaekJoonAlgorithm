# 2439번
import sys

n = int(sys.stdin.readline())
star = '*'

for i in range(n):
    print('%{}s'.format(n) % (star * (i + 1)))
