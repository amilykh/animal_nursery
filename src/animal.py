from datetime import datetime


class Animal:
    def __init__(self, name, age, date_of_birth=""):
        self.name = name
        self.age = age
        self.date_of_birth = datetime.strptime(
            date_of_birth, '%d-%m-%Y').date()

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")
        print(self.date_of_birth)
