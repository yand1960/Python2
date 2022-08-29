# Это типичный класс. Для него можно создавать объекты.
class MyGeometry:

    # Это называется "конструктор класса"
    def __init__(self, non_euqluid = 1.0):
        # Это называется "поле класса". Не совсем точно, "свойство класса"
        # Синтаксис self указывает, что это поле может быть разным у разных экземляров
        self.non_euqluid = non_euqluid

    # Это называется "метод класса", относящийся не к классу в целом,
    #  а к объекту этого класса
    def hypot(self, a, b):
        return ((a * a + b * b) ** 0.5) * self.non_euqluid

    def square(self, a, b):
        return a * b / 2 * self.non_euqluid


# Создание экзепляров класса
geometry1 = MyGeometry()
geometry2 = MyGeometry(non_euqluid=0.9)
# geometry2.non_euqluid = 0.9
geometry3 = MyGeometry(1.1)
# geometry3.non_euqluid = 1.1

# Эвклидова геометрия
print(geometry1.hypot(3, 4), geometry1.square(3, 4))

#  Геометрия Лобачевского
print(geometry2.hypot(3, 4), geometry2.square(3, 4))

#  Геометрия Гаусса
print(geometry3.hypot(3, 4), geometry3.square(3, 4))

# https://github.com/yand1960/Python3