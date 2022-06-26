#예제1

def first_func(w):
    print('Hello,', w)

word = "Goodboy"

first_func(word)
print()

#예제2

def return_func(d):
    value = "Hello, " + str(d)
    return value

x = return_func('Goodboy2')
print(x)
print()

#예제3(다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x, y, z)
print()

#예제3(형 변환)
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)
print(type(q), q, list(q), set(q))
print()

#예제4(사전 리턴)
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}

p = func_mul3(30)
print(p.get('v2'), p.items(), p.keys(), p.values())
print()

#예제5
# *args(언팩킹)
def args_func(*args):
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('------')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Won')
print()

#**kwargs(언팩킹)
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('------')

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Won')
print()

#전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'lee', 'kim', 'won', age1 =20, age2=30, age3=40)
print()

#중첩함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
print()

#람다(Lambda)
#예제6
#일반적 함수
def mul_func(x, y):
    return x * y

q = mul_func(10, 50)
print(q)

mul_func_var = mul_func
print(mul_func_var(20, 50))

#람다 함수
lambda_mul_func = lambda x, y: x * y

print(lambda_mul_func(50,50))

def func_final(x, y, func):
    print(x * y * func(100,100))

func_final(10, 20, lambda x, y: x * y)




