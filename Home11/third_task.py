"""
Программа с классом Car. При инициализации объекта
ему должны задаваться атрибуты color, type и year.
Реализовать пять методов. Запуск автомобиля – выводит
строку «Автомобиль заведён». Отключение автомобиля –
выводит строку «Автомобиль заглушен». Методы для
присвоения автомобилю года выпуска, типа и цвета.
"""


class Car:
    def __init__(self, color=None, type=None, year=None):
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
        print("engine is started")

    def stop_engine(self):
        print("engine is stopped")

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year


Mercedes = Car()

Mercedes.set_color("gray")
print(Mercedes.__dict__)

Mercedes.set_type("sedan")
print(Mercedes.__dict__)

Mercedes.set_year(2018)
print(Mercedes.__dict__)

Mercedes.start_engine()
Mercedes.stop_engine()
