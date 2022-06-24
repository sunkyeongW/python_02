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
print()

#예제4
lotto = [14, 45, 56, 26, 56, 78]

for l in lotto:
    print("Currnet number :", l)

#예제5
word = 'Beautiful'

for s in word:
    print('word :', s)
print()

#예제6
my_info = {
    "Name": 'Won',
    "Age": 26,
    "City": 'Seoul'
}
print()
for w in my_info:
    print('key :', my_info.get(w))
print()
for key in my_info:
    print('key :', my_info[key])
print()
for v in my_info.values():
    print('values :', v)
print()

#예제6
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
print()

#예제7
#break

numbers = [14, 4, 6, 78, 34, 67, 12]

for n in numbers:
    if n == 6:
        print('Found : 34!')
        break
    else:
        print('No :', n)

print()

#continue

lt = ["1", 2, 5, True, 3.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("Current type:", v, type(v))
print()

#예제8
#for- else

numbers = [14, 4, 6, 78, 34, 67, 12]

for num in numbers:
    if num == 99:
        print("Found!")
        break
else:
    print("Not Found")

#예제9
for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i *j), end='')
    print()

#변환 예제
name2 = 'Acyue'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))