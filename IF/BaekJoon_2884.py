# 2884번

a, b = map(int, input().split(' '))

if b < 45:
    a -= 1
    b += 15
    if a < 0:
        a = 23
else:
    b -= 45

print(a, b)

# 다른 사람 코드
# // 나누기 이후 소수점 버리기
a, b = map(int, input().split())
t = a * 60 + b - 45
print(t//60%24, t%60)
