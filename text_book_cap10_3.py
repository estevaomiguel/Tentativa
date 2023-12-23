class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Instance method
    def __str__(self):
        return f"{self.name}, is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    def _speak(self):
        pass

class JackRussellTerrier(Dog):
    def speak(self, sound = "Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
miles.speak()

#Exercise 1

class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return super().speak(sound)

#Exercise 2

class Rectangle:

    def __init__(self, leght, width):
        self.leght = leght
        self.width = width

    def area(self):
        return self.leght * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
square = Square(4)
print(square.area())


