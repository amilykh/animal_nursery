from animal import Animal


class PackAnimal(Animal):
    def __init__(self, name, age, date_of_birth):
        super().__init__(name, age, date_of_birth)
        self.place = "out of home"


class Horse(PackAnimal):
    def __init__(self, name, age, date_of_birth):
        super().__init__(name, age, date_of_birth)
        self.type = "horse"


class Camel(PackAnimal):
    def __init__(self, name, age, date_of_birth):
        super().__init__(name, age, date_of_birth)
        self.type = "camel"


class Donkey(PackAnimal):
    def __init__(self, name, age, date_of_birth):
        super().__init__(name, age, date_of_birth)
        self.type = "donkey"
