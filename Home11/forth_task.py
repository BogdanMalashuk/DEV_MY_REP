"""
Программа с классом Sphere для представления сферы
в трёхмерном пространстве. Реализовать методы:
● конструктор, принимающий 4 числа: радиус и координаты
центра сферы x, y, z. Если конструктор вызывается без
аргументов, создать объект сферы с единичным радиусом
и центром в начале координат. Если конструктор
вызывается только с радиусом, создать объект с
соответствующим радиусом и центром в начале
координат
● метод get_volume(), возвращающий число – объем шара,
ограниченного текущей сферой
● метод get_square(), возвращающий число – площадь
внешней поверхности сферы
● метод get_radius(), возвращающий число – радиус текущей
сферы
● метод get_center(), возвращающий кортеж с координатами
центра сферы
● метод set_radius(radius), который принимает новое
значение радиуса, меняет радиус текущей сферы и ничего
не возвращает
● метод set_center(x, y, z), который принимает новые
значения для координат центра радиуса, меняет
координаты текущей сферы и ничего не возвращает
● метод is_point_inside(x, y, z), который принимает
координаты некой точки в трёхмерном пространстве и
возвращает True или False в зависимо
находится ли точка внутри сферы
"""
import math


class Sphere:
    def __init__(self, x=0, y=0, z=0, r=1):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def get_volume(self):
        return 4/3 * math.pi * self.r ** 3

    def get_square(self):
        return 4 * math.pi * self.r ** 2

    def get_radius(self):
        return self.r

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_radius(self, radius):
        self.r = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        length = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2)
        return length < self.r


sphere = Sphere(3, 4, 5, 10)

print(f"sphere: {sphere.__dict__}")
print(f"volume: {sphere.get_volume():.2f}")
print(f"area: {sphere.get_square():.2f}")
print(f"radius: {sphere.get_radius()}")
print(f"center: {sphere.get_center()}")

print(sphere.set_radius(7))
print(f"sphere: {sphere.__dict__}")

print(sphere.set_center(3, 2, 9))
print(f"sphere: {sphere.__dict__}")

is_inside = sphere.is_point_inside(2, 5, 10)
print(f"is point inside sphere: {is_inside}")
