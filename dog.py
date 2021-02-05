import datetime

class Dog:
    def __init__(self, name, age, sex, last_heat = None):
        self.name = name
        self.age = age
        self.sex = sex
        self.last_heat = last_heat

    def set_heat(self, month, day, year):
        pass
