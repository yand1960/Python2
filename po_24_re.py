import re

passport = "12 34 567890"
passport1 = "a12 34 567890"

# valid = True
#
# try:
#     if len(passport) != 12:
#         valid = False
#
#     if passport[2] != " " or passport[5] != " ":
#         valid = False
#
#     for i in [0, 1, 3, 4, 6, 7, 8, 9, 10, 11]:
#         if not (passport[i] >= "0" and passport[i] <= "9"):
#             valid = False
# except:
#     valid = False
#
# print(valid)

# \d - цифра, \D - НЕ цифра
# {6} - ровно 6 раз
# ^ - начало текста, $ - конец текста

# \d - цифра \D - Не цифра
#{2} - ровно 2 раза
# ^ - начало текста, $ - конец текста
pattern = "^\d{2} \d{2} \d{6}$"
result = re.match(pattern, passport)
print(not (result is None))
result = re.match(pattern, passport1)
print(not (result is None))

text = """
Волга впадает в Каспийское море.
Тете Глаше 60 лет.
Саша впадает в уныние.
Мама мыла раму.
Оля впадает в восторг.
Пете 5 лет.
Маша впадает в ступор.
Тётя Клава тащит шпалу.
Хохо муму!
Петя впадает в восторг.
"""

# Найти всех, кто впадает в какое-то настроение.
# \S - неробельные символы
# + - в любом количестве
# [а-я] - любой символ от а до я
pattern = "\S+ впадает в [а-я]\S+"
results = re.findall(pattern, text)
print(results)

# Подсчитать статистику настроений
# (...) - группа, которая нас интересует
pattern = "\S+ впадает в ([а-я]+)"
results = re.findall(pattern, text)
# print(results)

statistics = {}
for mood in list(set(results)):
    statistics[mood] = results.count(mood)
print(statistics)

# Как зовут тетю, которая тащит шпалу (19:45)
# [её] - е или ё
pattern = "Т[её]тя (\S+) тащит шпалу"
results = re.findall(pattern, text)
print(results)
