"""
ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● eat(meal, value) – может принимать в meal только ”nectar”
или “grass”. Если съедает нектар, то value вычитается из
части слона, пчеле добавляется. Иначе – наоборот. Не
может увеличиваться больше 100 и уменьшаться меньше 0.

"""


class ElBee:
    def __init__(self, el_num, bee_num):
        self.el_num = el_num
        self.bee_num = bee_num

    def fly(self):
        return self.bee_num >= self.el_num

    def trumpet(self):
        if self.el_num >= self.bee_num:
            return "tu-tu-doo-doo"
        return "wzzzz"

    def eat(self, meal, value):
        if meal not in ["nectar", "grass"]:
            print("invalid 'meal' value")
            return

        if meal == "nectar":
            self.el_num = max(0, self.el_num - value)
            self.bee_num = min(100, self.bee_num + value)
        elif meal == "grass":
            self.bee_num = max(0, self.bee_num - value)
            self.el_num = min(100, self.el_num + value)
