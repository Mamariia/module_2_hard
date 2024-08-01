import random

first_number = random.randint(3, 20)
result = []

# Нахождение чисел, на которые первое число делится без остатка
list_ = []
for n in range(first_number + 1):
    if n > 2 and first_number % n == 0:
        list_.append(n)

# Подбор пароля
for i in range(1, int(first_number/2 + 1)):
    for j in list_:
        if j > i and (j/2) < (j-i):
            result.append(i)
            result.append(j - i)

print('Первое число:', first_number)
print('Пароль:', *result)