"""
Класс «Автобус». Класс содержит свойства:
● скорость
● максимальное количество посадочных мест
● максимальная скорость
● список фамилий пассажиров
● флаг наличия свободных мест
● словарь мест в автобусе
Методы:
● посадка и высадка одного или нескольких пассажиров
● увеличение и уменьшение скорости на заданное значение
● операции in, += и -= (посадка и высадка пассажира по
фамилии)
"""


class Bus:
    def __init__(self, speed, seats_count, max_speed, is_seats=True):
        self.speed = speed
        self.seats_count = seats_count
        self.max_speed = max_speed
        self.surnames = []
        self.is_seats = is_seats
        self.seats_dict = {}

    def add_passengers(self, *args):
        for arg in args:
            self.surnames.append(arg)

    def del_passengers(self, *args):
        for arg in args:
            if arg in self.surnames:
                self.surnames.remove(arg)

    def edit_speed(self, speed):
        self.speed += speed

    def __iadd__(self, surname):
        if surname not in self.surnames:
            self.surnames.append(surname)
        return self

    def __isub__(self, surname):
        if surname in self.surnames:
            self.surnames.remove(surname)
        return self

    def __contains__(self, surname):
        return surname in self.surnames


bus1 = Bus(35, 10, 100, is_seats=True)

bus1.add_passengers("Fam1", "Fam2", "Fam3", "Fam4", "Fam5", "Fam6")
print(bus1.__dict__)
bus1.edit_speed(-10)

bus1.del_passengers("Fam4", "Fam5")
print(bus1.__dict__)

bus1 += "Fam10"
bus1 -= "Fam2"

print(bus1.__dict__)
