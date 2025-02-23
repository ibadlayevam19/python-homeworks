import json
import random


class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name} says {self.sound}!"
    
    def sleep(self):
        return f"{self.name} is sleeping."

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Moo")
    
    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cluck")
    
    def lay_egg(self):
        return f"{self.name} laid an egg."

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Baa")
    
    def shear(self):
        return f"{self.name} is being sheared."