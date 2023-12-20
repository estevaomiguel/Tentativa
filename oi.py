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

miles = Dog("Miles", 4)
print(miles)

