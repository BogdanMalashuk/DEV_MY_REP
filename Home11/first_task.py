"""
Создайте класс Soda (газировка). Для инициализации
есть параметр, который определяет вкус газировки. При
инициализации этот параметр можно задавать, а можно и не
задавать. Реализовать метод строковой репрезентации,
который возвращает строку вроде «У вас газировка с
<клубничным> вкусом», если вкус задан. Если вкус не задан,
метод должен возвращать строку «У вас обычная газировка».
"""


class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def display_taste(self):
        if self.taste:
            return f"soda with {self.taste} taste"
        else:
            return f"simple soda without taste"


aqua = Soda()
cola = Soda("vanilla")

print(aqua.display_taste())
print(cola.display_taste())
