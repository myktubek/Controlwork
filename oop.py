# 1. Инкапсуляция
class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age >= 0:
            self._age =age
        else:
            raise ValueError("Возраст не может быть отрицательным")

    def get_age(self):
        return self._age

p = Person()
p.set_age(25)
print(p.get_age())


# 2. Наследование
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Животные"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.name, dog.speak())
print(cat.name, cat.speak())

# 3. Полиморфизм
class Vehicle:
    def move(self):
        return "движется"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicycle()
print(move(car))
print(move(bike))


# 4. Абстракция
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())  # Вывод: 50
print(circle.area())  # Вывод: ~153.94