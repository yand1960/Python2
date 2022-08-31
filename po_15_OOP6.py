# 1.Динамческое расшширение класса и как с ним бороться
# 2. "Перегрузка операций"

class Product:

    __slots__ = "name", "price"

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


product1 = Product(name="Cheese", price=12345)
print(product1)
# product1.mumu = "MUMU!" #error, если у класса указаны __slots__
# print(product1.mumu)

x = 123
# x.mumu = "qwerty" #error

# product1.price = 7777
# print(product1)

product2 = Product(name="Cheese", price=12345)

print(product1 is product2, product1 == product2)
