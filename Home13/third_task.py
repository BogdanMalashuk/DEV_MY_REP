"""
Паттерн «Строитель»
● Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions,
bacon.
● Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
● Создайте класс PizzaDirector, который принимает
экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza.
"""


class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.bacon = None


class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def get_pizza(self):
        return self._pizza

    def set_size(self, size):
        self._pizza.size = size
        return self

    def set_cheese(self, cheese):
        self._pizza.cheese = cheese
        return self

    def set_pepperoni(self, pepperoni):
        self._pizza.pepperoni = pepperoni
        return self

    def set_mushrooms(self, mushrooms):
        self._pizza.mushrooms = mushrooms
        return self

    def set_onions(self, onions):
        self._pizza.onions = onions
        return self

    def set_bacon(self, bacon):
        self._pizza.bacon = bacon
        return self


class PizzaDirector:
    def __init__(self):
        self.pizza_builder = PizzaBuilder()

    def make_pizza(self):
        return (self.pizza_builder
                .set_size("medium")
                .set_cheese(True)
                .set_pepperoni(True)
                .set_mushrooms(True)
                .set_onions(True)
                .set_bacon(True))


builder = PizzaBuilder()
director = PizzaDirector()
pizza = director.make_pizza()

new_pizza = ((pizza.set_cheese(False)
             .set_bacon(True)
             .set_onions(True)
             .set_pepperoni(True)
             .set_mushrooms(False)
             .set_size("Large"))
             .get_pizza())

print(new_pizza.__dict__)
