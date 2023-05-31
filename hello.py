# print("Hello, World!")

class Dog:
    def __init__(self, name, breed) -> None:
        self.name = name
        self.legs = 4
        self.breed = breed

    def speak(self):
        print(self.name + ' is a ' + self.breed + ' who says: Bark!')

my_dog = Dog('Rover', 'Jack Russell')
another_dog = Dog('Fluffy', 'Yorkie')

my_dog.speak()
another_dog.speak()

