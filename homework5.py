# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
# - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого
# атрибута нужно использовать методы get и set

class Students:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def learning(self):
        return "Student should learn Python!"


student = Students("Alex", "Ivanov")
print("Name: ", student.name, "Last name: ", student.student_id)
print(student.learning())


class FreshmanStudent(Students):
    def __init__(self, name, student_id, graduation_year):
        super().__init__(name, student_id)
        self.__graduation_year = graduation_year

    def get_graduation_year(self):
        return f'My graduation year is {self.__graduation_year}'

    def set_graduation_year(self, year):
        self.__graduation_year = year

    def welcome(self):
        return "Congratulations! Welcome to the college!"


class SophomoreStudent(FreshmanStudent):
    def __init__(self, name, student_id, graduation_year, score):
        super().__init__(name, student_id, graduation_year)
        self.score = score


student1 = Students("Alex", 215454545)
print("Name: ", student1.name, "Student ID: ", student1.student_id)
print(student1.learning())

new_student = FreshmanStudent("Anna", 1845848, 2021)
print("Name:", new_student.name, "ID:", new_student.student_id)
print(new_student.welcome())

second_year_student = SophomoreStudent("Mary", 51484545, 2019, 4.8)
# print(second_year_student.graduation_year)

student2 = SophomoreStudent("Gary", 2545848, 2020, 3.7)
# student2.set_graduation_year(2020)
print(student2.get_graduation_year())

print(dir(FreshmanStudent))
print(dir(SophomoreStudent))


"""5.2. Cоздайте репозиторий на Github и отправьте файл с домашним заданием в этот удаленный репозиторий
Repo was made:   https://github.com/lomicster/QAforE_Python.git
"""