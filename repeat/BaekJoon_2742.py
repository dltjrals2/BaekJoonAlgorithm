#2742번
import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(n - i)

# 다른 사람 코드
print('\n'.join(map(str, range(int(input()), 0, -1))))
