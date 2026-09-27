n = int(input("Введите число: "))

summa = 0

while n > 0:
    number = n % 10
    summa = summa + number
    n = n // 10

print("Сумма цифр:", summa)