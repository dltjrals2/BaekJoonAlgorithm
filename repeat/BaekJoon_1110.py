# 1110번
num = int(input())
checkNum = num
len = 0

while True:
    ten = num // 10
    one = num % 10
    total = ten + one
    len += 1
    num = int(str(num % 10) + str(total % 10))
    if(num == checkNum):
        break
print(len)
