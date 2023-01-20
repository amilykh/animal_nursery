from animal import Animal


class PetAnimal(Animal):
    def __init__(self, name, age, date_of_birth):
        super().__init__(name, age, date_of_birth)
        self.place = "home"


class Dog(PetAnimal):
    def __init__(self, name, age, date_of_birth):
        super().__init__(name, age, date_of_birth)
        self.type = "dog"


class Cat(PetAnimal):
    def __init__(self, name, age, date_of_birth):
        super().__init__(name, age, date_of_birth)
        self.type = "cat"


class Hamster(PetAnimal):
    def __init__(self, name, age, date_of_birth):
        super().__init__(name, age, date_of_birth)
        self.type = "hamster"
