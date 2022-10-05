# OOP
# class Employee:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def work(self):
#         return ("I am working!")
#
#
# class Developer(Employee):
#     def __init__(self, name, surname, language):
#         super().__init__(name, surname)
#         self.__language = language
#
#     def coding(self):
#         return("I am coding")
#
#     def work(self):
#         return("I am coding")
#
#     def get_language(self):
#         return f"My language is {self.__language}"
#
#     def set_language(self, newlang):
#         self.__language = newlang
#
# class Tester(Employee):
#     def __init__(self, name, surname, language, test_framework):
#         super().__init__(name, surname)
#         self.language = language
#         self.test_framework = test_framework
#
#     def testing(self):
#         return ("I can write tests!")
#
#     def work(self):
#         return("I am write tests!")
#
#
# dev1 = Developer("Max", "Frolov", "Python")
# print(dev1.name)
# dev1.name = "Maksim"
# print(dev1.name)
# print(dev1.surname)
#
# print(dev1.get_language())
# dev1.__language = "JavaScript"
# print(dev1.__dict__)
# print(dev1.__language)
# print(dev1.get_language())
# dev1.set_language("Java")
# print(dev1.get_language())
#
# print(dev1.work())
# print(dev1.coding())
# print(issubclass(Developer, Employee))
# print("~"*20)
#
# dev2 = Developer("Alisa", "S", "Go")
# dev2._Develper__language = "Java"
# print(dev2.__dict__)
#
# test1 = Tester("Anna", "Fedorova", "Java", "TestNG")
# print(test1.testing())
# print(test1.work())
# print("~"*20)
#
# employee1 = Employee("Alex", "Smith")
# print(employee1.name)
# print(employee1.surname)
# print(employee1.work())
# print("~"*20)
#
# employee2 = Employee(surname="Popov", name="Vladimir")
# print(employee2.name)
# print(employee2.surname)
# print("~"*20)

#Review
from gibrid import Gibrid
from animal import Animal
from dog import Dog
from cat import Cat


animal = Animal(name='Tuzik', weight=10, age=2)
print(animal.__dict__)
# print(animal.name)
animal.print_info()
print(animal.color)
print(Animal.color)
print('*' * 40)

#encapsulation
animal.set_name('Lelik')
print(animal.color)
print(Animal.color)
print("*" * 40)

#inheritance
dog1 = Dog('Barbos', 5, 10, 'Yardterrer')
print(dog1.__dict__)
dog1.print_info()
dog1.is_barking()
print("*" * 40)

#polymorfism
cat1 = Cat('Vasya', 12, 10)
print(cat1.__dict__)
cat1.print_info()
print("*" * 40)

gibrid1 = Gibrid('Puch', 12, 25)
gibrid1.print_create()
print(gibrid1.__dict__)
