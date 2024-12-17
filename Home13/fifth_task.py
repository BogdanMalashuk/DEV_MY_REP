"""
Паттерн «Стратегия»
● Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
● Создайте несколько классов, каждый реализует
определенную стратегию математической операции,
например, Addition, Subtraction, Multiplication, Division.
Каждый класс должен содержать метод execute, который
принимает два числа и выполняет соответствующую
операцию.
● Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate,
который выполняет операцию с помощью текущей стратегии.
"""


class Calculator:
    strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, first, second):
        return self.strategy.execute(first, second)


class Addition:
    @staticmethod
    def execute(a, b):
        return a + b


class Subtraction:
    @staticmethod
    def execute(a, b):
        return a - b


class Multiplication:
    @staticmethod
    def execute(a, b):
        return a * b


class Division:
    @staticmethod
    def execute(a, b):
        if b != 0:
            return a / b
        else:
            print("divider mustn't be 0")


calculator = Calculator()
calculator.set_strategy(Multiplication())
print(calculator.calculate(25, 12))
