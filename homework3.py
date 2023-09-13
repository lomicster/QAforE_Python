# #3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ["a", "b",[1, 2, 3], "d"]
print(*my_list[2])

# #3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# #   - получите сумму всех чисел,
# #   - распечатайте все строки, где есть буква 'a'
list_1 = ["Hi", "ananas", 2, None, 75, "pizza", 36, 100]
list_2 = [x for x in list_1 if isinstance(x,(int, float))]
#list_2 = list(filter(lambda x:isinstance(x, int), list_1 ))
print(sum(list_2))
print([x for x in list_1 if type(x) == str and "a" in x])

# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
list_3 = ["cat", "dog", "horse", "cow"]
print(tuple(list_3))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
family_1 = input("Enter first family's members: ")
family_2 = input("Enter second family's members: ")
if len(family_1.split(", ")) > len(family_2.split(", ")):
    print("First family is bigger")
elif len(family_1.split(", ")) < len(family_2.split(", ")):
    print("Second family is bigger")
else:
    print("Families are equal")

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
dict_mov = {
    "title": "Back to the Future",
    "director": "Zemeckis",
    "year": 1985,
    "budget": "$19000000",
    "main_actor": "Michael J. Fox",
    "slogan": "The only question is what time is it?"
}
print(*dict_mov.keys())
print(*dict_mov.values())
print(*dict_mov.items())

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {
    'num1': 375,
    'num2': 567,
    'num3': -37,
    'num4': 21
}
print("\nResult:", sum(my_dictionary.values()))

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
list_raw = [1, 2, 3, 4, 5, 3, 2, 1]
print("\nOriginal list: ", list_raw)
print("Shortened list: ", list(set(list_raw)))

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

print("\nCommon values: ", set2.intersection(set1))
print("Diffent values: ", set1.difference(set2))
print("Totaly different values: ", set1.symmetric_difference(set2))
print(set2.issuperset(set1))
print(set2.issubset(set1))