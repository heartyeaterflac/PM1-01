def share_cost(total, people):
    return total / people

def read_integer(prompt, minimum):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Введите целое число')
        else:
            if value < minimum:
                print('Минимальное значение:', minimum)
            else:
                return value

total = read_integer("Стоимость поездки, тенге: ", 0)
people = read_integer("Количество участников: ", 1)
result = share_cost(total, people)
print("С каждого участника:", round(result, 2), "тенге")