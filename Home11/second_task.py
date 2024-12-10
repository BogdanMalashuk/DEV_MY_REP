"""
Напишите программу с классом Math. При
инициализации атрибутов нет. Реализовать методы addition,
subtraction, multiplication и division. При передаче в методы
двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ.
"""


class Math:
    def addition(self, a, b):
        print(f"{a} + {b} = {a + b}")

    def subtraction(self, a, b):
        print(f"{a} - {b} = {a - b}")

    def multiplication(self, a, b):
        print(f"{a} * {b} = {a * b}")

    def division(self, a, b):
        if b == 0:
            print("invalid value")
            return
        print(f"{a} : {b} = {a / b}")


mathematics = Math()
mathematics.addition(5, 8.8)
mathematics.subtraction(14, 23)
mathematics.multiplication(4, 5.3)
mathematics.division(15, 4)
