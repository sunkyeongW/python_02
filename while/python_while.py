#예제1

n = 5

while n > 0:
    print(n)
    n = n - 1

#예제2

a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

print()

#예제3
##break

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')
print()

#예제4
#continue

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')
print()

#예제5
#if 중첩

i = 1

while i <= 10:
    print('i :', i)
    if i == 7:
        break
    i += 1

print()
#예제6

n = 10

while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

print('예제7')

#예제7

a = ['foo', 'ba', 'baz', 'df']
s = 'dfdf'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, "not found")

#예제8

a = ['foo', 'ba', 'baz', 'df']

while True:
    if not a:
        break
    print(a.pop())