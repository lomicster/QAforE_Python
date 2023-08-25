#hw1
#1
#print("Hello World!")

#2
# user_name = input("Enter your name: ")
# print(f"Hello {user_name}")

#3
# print("""*********
# *       *
# *       *
# *********""")
#
# print("*********\n" + "*       *\n" + "*       *\n" + "*********")
#4 Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
# Пример:
# Input: 3498
# Output:
# Тысячи - 3
# Сотни - 4
# Десятки - 9
# Единицы - 8

num = int(input("Please enter 4 digits number: "))
print(f"Thousands: {num // 1000} \nHundreds: {num // 100} \nTens: {num // 10} \nOnes: {num // 1}")

#From review class
# a = True
# b = False
# print(int(a))
# print(int(b))
# print(a + b)
#
# m = input("Enter your wish: ")
# print(m)
# ma = m.isdigit() #Проверка число или нет
# print(ma)
# mb = m.capitalize() #Первый символ становится заглавным
# print(mb)
# mc = m.upper() #Все символы становятся заглавными
# print(mc)
#
# md = m.isalpha() #Return True if the string is an alphabetic string, False otherwise
# print(md)