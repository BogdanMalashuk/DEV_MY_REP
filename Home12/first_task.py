"""
Класс «Товар» содержит следующие закрытые поля:
● название товара
● название магазина, в котором подаётся товар
● стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● вывод информации о товаре со склада по индексу
● вывод информации о товаре со склада по имени товара
● сортировка товаров по названию, по магазину и по цене
● перегруженная операция сложения товаров по цене

"""


class Product:
    counter = 0
    instances = []

    def __init__(self, name, shop, cost):
        self.__name = name
        self.__shop = shop
        self.__cost = cost
        self.id_product = Product.counter
        Product.counter += 1
        self.__class__.instances.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def shop(self):
        return self.__shop

    @property
    def cost(self):
        return self.__cost

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__cost + other.__cost
        raise TypeError("invalid type")


class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def info_by_id(self, pr_id):
        for product in self.__products:
            if product.id_product == pr_id:
                print(f"name: {product.name}")
                print(f"shop: {product.shop}")
                print(f"cost: {product.cost}")
                print(f"id: {product.id_product}")
                return
        print(f"there is no product with id: {pr_id}")

    def info_by_name(self, name):
        for product in self.__products:
            if product.name == name:
                print(f"name: {product.name}")
                print(f"shop: {product.shop}")
                print(f"cost: {product.cost}")
                print(f"id: {product.id_product}")
                return
        print(f"there is no product with name: {name}")

    def sort_by_name(self):
        return sorted(self.__products, key=lambda product: product.name)

    def sort_by_cost(self):
        return sorted(self.__products, key=lambda product: product.cost)

    def sort_by_shop(self):
        return sorted(self.__products, key=lambda product: product.shop)


product1 = Product("Bread", "Euroopt", 150)
product2 = Product("Coca-Cola", "Gippo", 350)
product3 = Product("Snickers", "Sosedi", 200)

store1 = Store()
store1.add_product(product1)
store1.add_product(product2)
store1.add_product(product3)

print(store1.__dict__)

store1.info_by_id(2)

store1.info_by_name("Bread")

print(product1 + product3)
