a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > b:
    if a > c:
        print(a)

if b > a:
    if b > c:
        print(b)

if c > a:
    if c > b:
        print(c)

if a == b:
    if a == c:
        print('равны')