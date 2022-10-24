# Colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(Colors) 
# data.close()


# # Если нам потребуется каждый раз дописывать новою порцию данных, то используем метод write. См ниже.
# Colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(Colors)
# data.write('LINE 12\n')
# data.write('LINE 13\n')
# data.close()

# # Ещё один вариант решения 
# with open('file.txt', 'w') as data:
#     data.write('line 111\n')
#     data.write('line 222\n')

# # Ниже рассмотрим чтение данных из файла?
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()



# # # Это фрагмент программы использования функционал одгного файла другим файлом (см. файл HELLO.py)
# import HELLO

# print(HELLO.f(1))


# # аналогично, только сокрвщено написание с помощью  as h
# import HELLO as h

# print(h.f(1))


# # ФУНКЦИИ
# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# # print(concatenatio('a', 's', 'd', 'w')) -> asdw 
# # print(concatenatio('a', '1')) -> a1 


# int
# def concatenatio(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4,))  --->> 10

# # РЕКУРСИЯ (+ числа Фибоначи)
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)
# # 1 1 2 3 5 8 13 21 34 


# # КОРТЕЖИ - неизменный список (если кортеж состоит из одной цифры, то оюязаткльно должна стоять запятая (3,)    )
# # Кортеж - это тип данных
# a = (3, 1, 41, 4)
# print(a)
# print(a[-2])

# a = (3, 4, 5)
# for item in a:
#     print(item)



# СЛОВАРИ
# dictionari = {}
# dictionari = {
#         'up': '1',
#         'left': '2',
#         'down': '3',
#         'right': '4'
#     }
# for k in dictionari.keys():
#     print(k)
# # up
# # left
# # down
# # right


# dictionari = {}
# dictionari = {
#         'up': '1',
#         'left': '2',
#         'down': '3',
#         'right': '4'
#     }
# for k in dictionari.values():
#     print(k)
# # 1
# # 2
# # 3
# # 4


# # МНОЖЕСТВА
# colors = {'red', 'green', 'blue'} 

# print(colors) 
# #  {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)
# #  {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)
# #  {'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors)
# #  {'green', 'blue', 'gray'}
# colors.discard('red')
# #  ok
# print(colors)
# #  {'green', 'blue', 'gray'}
# colors.clear()
# # { }
# print(colors)
# #  set()


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# # c = {1, 2, 3, 5, 8}
# u = a.union(b)
# # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)
# # i = {8, 2, 5}
# dl = a.difference(b)
# # dl = {1, 3}
# dr = b.difference(a)
# # dr = {13, 21}

# q = a\
#     .union(b) \
#         .difference(a.intersection(b))
# # {1, 2, 3, 13}

# s = frozenset(a)
# # Выше замороженное множество, его поменять не получится.



# #  СПИСКИ
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list1[0] = 123
# list2[1] = 333
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)


# # Как удалять последний элемент нашего списка
# list1 = [1, 2, 3, 4, 5]

# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# # Так же можно вставить элемент на нужную позицию (см. ниже)
# list1 = [1, 2, 3, 4, 5]
# print(list1.insert(2,11))
# print(list1)

# Если нужно добавить в конец списка см. ниже 
list1 = [1, 2, 3, 4, 5]
print(list1.append(11))
print(list1)



