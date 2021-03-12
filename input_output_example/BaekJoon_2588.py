# 2588번

a = int(input())
b = list(input())

b2, b1, b0 = map(int, b[0:3])

print(b0 * a)
print(b1 * a)
print(b2 * a)
print((b0 * a) + (b1 * a * 10) + (b2 * a * 100))


# 다른 사람 코드
# a = int(input())
# b = list(map(int, list(input())))
# for i in range(3):
#     print(a * b[2-i])
# print(a * (100 * b[0] + 10 * b[1] + b[2]))
