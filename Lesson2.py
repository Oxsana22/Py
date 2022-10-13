# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

# 1 Вариант решения:
# n = int(input())
# for i in range(n - 1):
#     print((-3) ** i, end=',  ')
# print((-3) ** (n - 1))

# 2 Вариант решения
# n = int(input())
# a = []
# for i in range(n):
#     a.append((-3) ** i)
# print(*a, sep=', ')

# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# (Без словаря, так как словарь ещё не праходили)

# n = int(input())
# print('{', end='')
# for i in range(1, n):
#     print(f'{i}:{3 * i + 1}', end=', ')
# print(f'{n}:{3 * n + 1}', end='}')



# 3. Напишите программу, в которой пользователь
# будет задавать две строки, а программа - определять 
# количество вхождений одной строки в другой.

# 1. Вариант решения
# some_str_1 = input()
# some_str_2 = input()
# print(some_str_1.count(some_str_2) or some_str_2.count(some_str_1))

# 2. Вариант решения    НО! ОН НЕ СОВСЕМ КОРРЕКТНЫЙ.
# print(input().count(input()) or input().count(input()))  

# 3.  Вариант решения с помощью АЛГОРИТМА с использованием count (часто используется на собеседовании)
# some_str_1 = input()
# some_str_2 = input()
# len_str_2 = len(some_str_2)
# i = 0
# count = 0
# while i < len(some_str_1):
#     if some_str_1[i:i + len_str_2] == some_str_2:
#         count += 1
#     i += 1
# print(count)

# 4. Вариант решения с помощь АЛГОРИТМА
some_str_1 = input()
some_str_2 = input()
len_str_2 = len(some_str_2)
i = 0
count = 0
while i < len(some_str_1):
    if some_str_1[i:i + len_str_2] == some_str_2:
        count += 1
        i += 2
    else:
        i += 1
print(count)


