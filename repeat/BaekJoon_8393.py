# 8393번
n = int(input())
sum = 0

for i in range(n + 1):
    sum += i

print(sum)

# 다른 사람 코드
print(sum(range(int(input)) + 1)))
