from cat import Cat
from dog import Dog


class Gibrid(Cat, Dog):
    def print_create(self):
        print(f'We created catdog')