# 1. Инкапсуляция
class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Возраст не может быть отрицательным")

    def get_age(self):
        return self._age

p = Person()
p.set_age(25)
print("Инкапсуляция:", p.get_age())


# 2. Наследование
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Животные"

class Dog(Animal):
    def speak(self):
        return "вув"

class Cat(Animal):
    def speak(self):
        return "миу"

dog = Dog("Buddy")
cat = Cat("Kitty")
print("Наследование:", dog.name, dog.speak())
print("Наследование:", cat.name, cat.speak())

# 3. Полиморфизм
class Vehicle:
    def move(self):
        return "движется"

class Car(Vehicle):
    def move(self):
        return "машина едит"

class Bicycle(Vehicle):
    def move(self):
        return "велосипед едит"

def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicycle()
print("Полиморфизм:", move(car))
print("Полиморфизм:", move(bike))

# 4. Абстракция не смог