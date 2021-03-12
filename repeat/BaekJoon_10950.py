# 10950번

caseNum = int(input())

c = list()

for i in range(caseNum):
    a, b = map(int, input().split())
    c.insert(i, a + b)

for j in range(caseNum):
    print(c[j])
