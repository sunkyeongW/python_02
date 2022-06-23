#예제1

if True:
    print('Good')

if False:
    print('Bad')
print()

#예제2
if False:
    print('Bad!')
else:
    print('Good!')
print()
print('관계 연산자')
#관계 연산자
#>, >=, ==, <=,<, !=
x = 15
y = 10

#양변이 같을 때
print(x == y)

#양변이 다를 때
print(x != y)

#왼쪽이 클 때 참
print(x > y)

#왼쪽이 크거나 같을 때 참
print(x >= y)

#오른쪽이 클 때 참
print(x < y)

#오른쪽이 크거나 같을 때 참
print(x <= y)

#예제3

#True일 때
city = "seoul"
if city:
    print("You are in:", city)
else:
    print("plz enter your city")

#False일 때
city = ""
if city:
    print("You are in:", city)
else:
    print("plz enter your city")
print()
print("논리연산자")

#논리연산자

a = 75
b = 40
c = 20
#and 예제문
print('and:', a > b and b > c)
#or 예제문
print('or:', a > b or b < c)
#not 예제문
print('not:', not b > c),
print('not:', not a < b),
print(not True)
print(not False)
print()
#산술, 관계, 논리 우선순위

#예제4
print('e1 :', 3 + 10 > 4 + 3 )
print('e2 :', 5 + 3 * 3 < 4 + 3 * 2 )
print('e3 :', 5 + 10 > 3 and 3 * 2 == 6 )
print('e4 :', 5 + 10 > 3 and not 3 * 2 == 6 )
print('e4 :', 5 + 10 > 3 and not 3 * 3 == 6 )
print()

#복수의 조건이 모두 참일 경우 실행
#예제5
score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')
print()
#예제6
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('user')

if id2 == 'admin' and grade == 'platinum':
    print('super user')
print()
#다중 조건문
#예제7
num = 40

if num >= 90:
    print('Grade: A')
elif num >= 80:
    print('Grade: B')
elif num >= 70:
    print('Grade: C')
else:
    print('Fail')
print()

#중첩 조건문
#예제8

grade = 'A'
total = 75

if grade =='A':
    if total >= 90:
        print('100%')
    elif total >= 80:
        print('80%')
    else:
        print('50%')
else:
    print('장학금 없음')
print()

#in, not in

q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name": "Won", "City": "Incheon", "Grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("Incheon" in e.values())


