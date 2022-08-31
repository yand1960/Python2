# 1. "Приватный доступ" к полю класс
# 2. Понятие "свойство класса"

# "Явский стиль" инкапсуляции доступ к приватному полю класса
# class Product:
#
#     __slots__ = "_name", "price"
#
#     def __init__(self, name: str, price: float):
#         self.set_name(name)
#         self.price = price
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if len(name) >= 4:
#             self._name = name
#         else:
#             raise ValueError("Длина имени должна быть больше 4")
#
#     def __str__(self):
#         return f"{self._name} - {self.price}"

# # Явная реализация у класса свойства c помощью функции property
# class Product:
#
#     def __init__(self, name: str, price: float):
#         self._name = None
#         self.set_name(name)
#         self.price = price
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if len(name) >= 4:
#             self._name = name
#         else:
#             raise ValueError("Длина имени должна быть больше 4")
#
#     name = property(fget=get_name, fset=set_name)

# Явная реализация у класса свойства c помощью декортора property
class Product:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) >= 4:
            self._name = name
        else:
            raise ValueError("Длина имени должна быть больше 4")

    def __str__(self):
        return f"{self._name} - {self.price}"


product1 = Product("Kepka", 123)
print(product1)

product2 = Product("Kepka", 123)
#product2._name = "Kep" #конвенция - не обращзаться к челнам класс _lala в клиенстком
print(product2.name)
# product2.set_name("Sha")
product2.name = "Shapka"
print(product2)



