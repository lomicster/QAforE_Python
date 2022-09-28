#Logical operators
"""
x = 5
print(not x < 5) #True
print(not x > 5) #True
print(not x == 5) #False
print(not x != 5) #True """

#if else statements
"""num = 5
if num == 5:
    print("five")
else:
    print("Not equal five")

num = 3
if num == 5:
    print("five")
elif num > 5:
    print("more than five")
else:
    print("less than five")"""

# Проверяем возраст посетителя и в зависимости от вводных данных решаем, может ли он посетить заведение
# age = float(input('Enter your age: '))
# if age < 13:
#     print("Where's your mom?")
# elif age >= 21:
#     print('Welcome!')
# else:
#     print('Go home')

#Loop while
# i = 1
# while i <= 5:
#     print("Hello World!")
#     if i == 3:
#         break
#     i = i + 1

# Обратный отчет с использованием цикла while
"""i = 5
while i > 0:
    print(i, 'Hello')
    i = i - 1
print('Go!')"""

# Использование цикла while с оператором continue
# i = 0
# while i < 5:
#     i = i + 1
#     if i == 3:
#         continue
#     print(i)

"""# Посимвольный вывод введенного слова
name = input('Input your name: ')
for letter in name:
    print(letter)

# Посимвольный вывод введенного слова с указанием индекса символа
name = input('Enter your name: ')
for symbol in name:
    print(f'index {name.index(symbol)} - {symbol}')

# Пример использования выражений, которые приравниваются к булевым (True/False)
number = 0
if name:
    print('true')
else:
    print('false')

#     Использование for цикла в заданном диапазоне range
for i in range(5):
    print(i, 'Hello!')

#     Использование for цикла в заданном диапазоне range с указанием начала, конца и шага (start, stop, end)
for i in range(0, -10, -1):
    print(i)

# Использование for цикла в заданном диапазоне c оператором break

for i in range(5):
    if i == 3:
        break
    print(i)"""

"""Данная программа, проверяет является ли введенная буква гласной. Здесь в else используется вложенное условие -
  если утверждение во внешнем if - ложное, программа перейдет к else  и начнет проверять вложенное if, если 
  оно также ложно, выполнится команда во вложенном else
  Этот пример мы не рассмотрели на уроке, но вы можете сами поиграть с кодом и проверить, 
  что произойдет, если вы вместо letter.isdigit() поставите letter.isalpha(). Какие изменения нужно будет
  внести в условия? -> add not into  first if loop"""

# letter = input()
# vowels = 'ioaue'
# if  letter.isdigit():
#     print('It is not a letter')
# else:
#     if letter in vowels:
#         print('vowel')
#     else:
#         print('consonant')

# Функция для возведения заданного числа в заданную степень
"""def give_me_power(num, n):
    return num ** n

print(give_me_power(2, 5))
print(give_me_power(2, 4))"""