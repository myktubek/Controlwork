from abc import ABC, abstractmethod
import math

# 1. Инкапсуляция — класс Person
class Person:
    def __init__(self):
        self._age = None  # приватный атрибут

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self._age = age

    def get_age(self):
        return self._age

# 2. Наследование — классы Animal, Dog, Cat
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# 3. Полиморфизм — Vehicle, Car, Bicycle и функция move()
class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

# 4. Абстракция — абстрактный класс Shape, Rectangle и Circle
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
        return math.pi * self.radius ** 2

# --- Примеры использования всех классов и функций ---

if __name__ == "__main__":
    # Тест инкапсуляции
    p = Person()
    p.set_age(25)
    print("Person age:", p.get_age())
    # p.set_age(-5)  # раскомментируй — будет ошибка

    # Тест наследования
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    print(dog.name, dog.speak())
    print(cat.name, cat.speak())

    # Тест полиморфизма
    car = Car()
    bike = Bicycle()
    print(move(car))
    print(move(bike))

    # Тест абстракции
    rect = Rectangle(10, 5)
    circle = Circle(7)
    print("Rectangle area:", rect.area())
    print("Circle area:", round(circle.area(), 2))
