# Наследование в ООП
from po_12_OOP3 import Person


class Boss(Person):

    # расширение супер-класса
    def scream(self):
        return f"Я  {self.first_name} {self.last_name}! Всем работать!!!"

    # перекрытие метода супер-класса
    def __str__(self):
        return f"Boss: {self.first_name} {self.last_name}"


boss = Boss(first_name="Bill", last_name="Gates", salary=1234567)
print(boss.last_name)
print(boss.scream())