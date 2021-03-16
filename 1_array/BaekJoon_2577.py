# 2577번
import sys

array = list()

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
multiply = a * b * c
array = list(str(multiply))

print(array.count('0'))
print(array.count('1'))
print(array.count('2'))
print(array.count('3'))
print(array.count('4'))
print(array.count('5'))
print(array.count('6'))
print(array.count('7'))
print(array.count('8'))
print(array.count('9'))

# 다른 사람 코드
a = int(input())
b = int(input())
c = int(input())

x = list(str(a * b * c))
for i in range(10):
    y = x.count(str(i))
    print(y)
