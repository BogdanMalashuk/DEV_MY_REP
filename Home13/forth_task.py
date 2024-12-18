"""
Паттерн «Фабричный метод»
● Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
● Создайте классы Dog и Cat, которые наследуют от Animal
и реализуют метод speak.
● Создайте класс AnimalFactory, который использует
паттерн «Фабричный метод» для создания экземпляра
Animal. Этот класс должен иметь метод create_animal,
который принимает строку («dog» или «cat») и возвращает
соответствующий объект (Dog или Cat).
"""


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Woof woof!")


class Cat(Animal):
    def speak(self):
        print("Meow meow!")


class AnimalFactory:
    @staticmethod
    def create_animal(string):
        if string.lower() == "cat":
            return Cat()
        elif string.lower() == "dog":
            return Dog()
        else:
            raise ValueError


factory = AnimalFactory()
cat = AnimalFactory.create_animal("cat")
dog = AnimalFactory.create_animal("dog")
cat.speak()
dog.speak()
