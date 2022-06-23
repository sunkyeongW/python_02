#For 실습

#예제1

for v1 in range(10): #0부터 시작
    print('v1 is:', v1)
print()
for v2 in range(1, 11): #1 ~ 10
    print('v2 is:', v2)
print()
#짝수
for v3 in range(2, 11, 2): #2번 step
    print('v3 is:', v3)
print()
#홀수
for v4 in range(1, 11, 2): #2번 step
    print('v4 is:', v4)
print()

#예제2
#1~1000합

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 Sum:', sum1)
print('1 ~ 1000 4의 배수의 합:', sum(range(1,1001))) #함수를 이용

#자료형 반복

#예제3
names = ['Kim', 'Park', 'Won']

for n in names:
    print('You are:', n)
