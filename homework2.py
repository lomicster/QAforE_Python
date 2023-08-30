"""Задание 2.1
Напишите программу, которая проверяет здоровье персонажа в игре.
Если оно равно или меньше нуля, выведите на экран False, в противном случае True."""
#
# character_health = 100
# if character_health <= 0:
#     print(False)
# else:
#     print(True)

"""Задание 2.2
Напишите программу, которая проверяет является ли введенное число четным. 
Если да, выведите на экран текст “Четное” (Even), а иначе - “Нечетное”(Odd)"""
# num = int(input("Enter a number for check: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

"""Задание 2.3
Напишите программу, которая проверяет является ли год високосным.
Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). 
Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)"""

# year = int(input("Please enter a year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("This is a leap year.")
# else:
#     print("This is a common year.")

"""Задание 2.4
Напишите программу, которая печатает введенный текст заданное количество раз, построчно. 
Текст и количество повторений нужно ввести с помощью input()"""
# i= 0
# text = input("Please enter your text: ")
# qty = int(input("Please enter quantity of iterations: "))
# while i < qty:
#     i += 1
#     print(f"{i} {text}")

"""Задание 2.5.
Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное
арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result} """

# import my_calc as calc
# x = int(input("Please enter first number: "))
# y = int(input ("Please enter second number: "))
# operator = str(input("Please enter operator: "))
#
# if operator in ("+", "sum", "addition", "сложение"):
#    print(f"{x} {operator} {y} = {calc.sum(x, y)}")
# elif operator in ("-", "subtraction", "вычитание"):
#    print(f"{x} {operator} {y} = {calc.subs(x, y)}")
# elif operator in ("*", "multiplication", "умножение"):
#    print(f"{x} {operator} {y} = {calc.prod(x, y)}")
# elif operator in ("/","division ", "деление"):
#    print(f"{x} {operator} {y} = {calc.div(x, y)}")

#Review session
