# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# import math
# def square(side):
#     return(side * 4, side ** 2, round(side * math.sqrt(2),2),)
#
# print(square(int(input("Enter suare side: "))))

# 4.2. Напишите функцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
#
# def func(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# func(name = "John", last_name = "Smith", age = 35, position = "web developer")

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x >= 0, my_list)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# filtered = filter(lambda x: x >= 0, my_list)
# print(reduce(lambda x,y: x*y, filtered))

# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.


# import my_calc as c
# print(c.subs(10, 5))
# print(c.prod(0, 5))
# print(c.sum_it(584848, 118515))
# print(c.div(12, 3))
# print(c.div(14, 0))

