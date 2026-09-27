a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
znak = input("Введите знак (+, -, *, /): ")

if znak == "+":
    print(a + b)

if znak == "-":
    print(a - b)

if znak == "*":
    print(a * b)

if znak == "/":
    if b == 0:
        print("Ошибка")
    else:
        print(a / b)