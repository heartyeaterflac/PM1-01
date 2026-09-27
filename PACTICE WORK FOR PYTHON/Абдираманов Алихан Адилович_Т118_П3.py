salary = int(input())

if salary <= 200000:
    tax = salary * 0.05
elif salary <= 500000:
    tax = salary * 0.10
else:
    tax = salary * 0.15

nettto_salary = salary - tax

print("Налог:", tax)
print("Зарплата после налога:", nettto_salary)