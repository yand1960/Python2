# Это не совсем типичный класс. Для него бессмысленно понятие "объект".
# В других платформах это называется "статический класс".
class MyGeometry:

    # Это называется "поле класса". Не точно, "свойство класса"
    non_eugluid = 1.0

    # Это называется "метод класса"
    def hypot(a, b):
        return ((a * a + b * b) ** 0.5) * MyGeometry.non_eugluid

    def square(a, b):
        return a * b / 2 * MyGeometry.non_eugluid

# Эвклидова геометрия
print(MyGeometry.non_eugluid)
print(MyGeometry.hypot(3, 4), MyGeometry.square(3, 4))

#  Геометрия Лобачевского
MyGeometry.non_eugluid = 0.9
print(MyGeometry.hypot(3, 4), MyGeometry.square(3, 4))

#  Геометрия Гаусса
MyGeometry.non_eugluid = 1.1
print(MyGeometry.hypot(3, 4), MyGeometry.square(3, 4))

# https://github.com/yand1960/Python3