from animal import Animal

class Dog(Animal):
    def __init__(self, name, age, weight, breed='Terrer'):
        super().__init__(name, age, weight)
        self.breed = breed

    def is_barking(self):
        print('Dog is barking')
