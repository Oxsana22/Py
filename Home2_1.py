# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. 
# Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

a = input('Введите число:   ')
sum = 0
for i in a:
    if i != ',' and i != '-':
        sum += int(i)
print(sum)