#  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет


a = int(input('Введите день недели: '))
if a > 0 and a < 8:   
    if a<6 and a>0:
        print('Нет, сегодня будний день!')
    else:
        print('Да, сегодня выходной!')
else:
    print('Введите число от 1 до 7.')
        