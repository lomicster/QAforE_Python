from animal import Animal


class Cat(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def print_info(self):
        print(f'Cat with weight {self.weight} kg and age {self.age} years')
