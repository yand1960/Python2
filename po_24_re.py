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
pattern = "^\d{2} \d{2} \d{6}$"
result = re.match(pattern, passport)
print(not (result is None))
result = re.match(pattern, passport1)
print(not (result is None))
