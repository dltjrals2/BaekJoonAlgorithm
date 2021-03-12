# 1000번 문제
# input.split()
# input은 기본적 str형
# split()은 문자열을 쪼갤때 사용한다. 괄호안에 쪼개는 조건 넣기

# a, b = input().split()
#
# c = int(a) + int(b)
# print(c)

# 다른 방식
a, b = map(int, input().split(' '))
print(a + b)
