# 3052번
import sys

array = list()
value = 0
len = 0

for i in range(10):
    value = int(sys.stdin.readline()) % 42
    if value not in array:
        len += 1
    array.append(value)

print(len)

# 다른 사람 코드
# set은 중복과 순서가 없으므로 그것을 이용하는구나
lst = []
for i in range(10):
    lst.append(int(input()) % 42)

lst = list(set(lst))
print(len(lst))
