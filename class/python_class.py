#예제1
class Dog:
    species = 'firstdog' #클래스 변수

    def __init__(self, name, age): #인스턴스 변수
        self.name = name
        self.age = age
print(Dog)

#예제2(인스턴스화)
a = Dog("Star", 17)
b = Dog("Cookie", 5)
c = Dog("Baby", 3)
d = Dog("Star", 17)

print(a == b, id(a), id(b))
print(a == d, id(a), id(d))

#예제3(네임스페이스)
print('dog1', a.__dict__)
print('dog2', b.__dict__)

#예제4(인스턴스 속성)
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

#예제5
class selftest:
    def func1():
        print('Func1 called')
    def func2(self):
        print('Funcs called')

f = selftest()

print(id(f))
f.func2() #self로 호출
selftest.func1() #클래스로 바로 호출
print()

#예제6
class room:
    stock_num = 3 #재고

    def __init__(self, name):
        self.name = name
        room.stock_num += 1
    
    def __del__(self):
        room.stock_num -= 1

user1 = room('lee')
user2 = room('won')

print(room.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(room.__dict__)

del user1
print(room.__dict__)
print()

#예제7
class Dog2:
    species = 'firstdog' #클래스 변수

    def __init__(self, name, age): #인스턴스 변수
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

C = Dog2('star', 5)
print(C.info())
print(C.speak('wal wal!'))