# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


lis = [2, 3, 5, 6]
lis1 = []
x = 0
s = 0
count = 0
for i in range(0, len(lis)):
    if len(lis)% 2==0:
        if i < len(lis)//2:  
            x = lis[i]
            s = lis[-1]
            count = x*s
            i +=1
            lis[-1] -= 1
            lis1.append(count)
    else:
        if i <= len(lis)/2:
            x = lis[i]
            s = lis[-1]
            count = x*s
            i += 1
            lis[-1] += -1
            lis1.append(count)
print(lis1)










#     # if i <= len(lis
#)/2 and lis
#[i] >= len(lis
#)/2:
#         # lis
# = lis
#[i] - 1
#         x = lis
#[0]
#         s = lis
#[-1]
#         count = x * s
#         if i <= len(lis
#)//2 and lis
#[i] >= len(lis
#)//2:
#             i += 1
#             lis
#1.append(count)
                    
# print (lis
#1)

# lis
#1 = [1, 2, 3, 4, 5]
# lis
#2 = lis
#1
# lis
#1[0] = 123
# lis
#2[1] = 333
# for e in lis
#1:
#     print(e)
# print()
# for e in lis
#2:
#     print(e)   