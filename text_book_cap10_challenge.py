class Animal:

    position = 0
    stuff_belly = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello, I am {self.name} and I have {self.age} years"
    def speak(self, sound):
        return f"{self.name}, says {sound}"

    def walk(self, walked_distance):
        self.position = self.position + walked_distance
        return self.position

    def running(self, run_distance):
        self.position = self.position + run_distance
        return self.position

    def eating(self):
        self.stuff_belly = self.stuff_belly + 1
        if self.stuff_belly > 3:
            self.poop()
        else:
            return f"{self.name} is eating"
    def is_hungry(self):
        if self.stuff_belly < 2:
            return f"{self.name} is hungry"
        else:
            return f"{self.name} is not hungry"
    def poop(self):
        self.stuff_belly = 0
        return f"{self.name} ate too much..."


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self, sound = "Bark"):
        return super().speak(sound)

class Sheep(Animal):
    pass

class Pig(Animal):
    pass

miles = Dog("Miles", 4, "Golden Retriever")
print(miles)
print(miles.speak())
