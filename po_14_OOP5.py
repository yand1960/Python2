# Наследование в ООП
from po_12_OOP3 import Person


class Boss(Person):

    # расширение супер-класса
    def scream(self):
        return f"Я {self.first_name} {self.last_name}! Всем работать!!!"

    # перекрытие метода супер-класса
    def __str__(self):
        return f"Boss: {self.first_name} {self.last_name}"


boss = Boss(first_name="Bill", last_name="Gates", salary=1234567)
print(boss.last_name)
print(boss.scream())


class Manager(Person):

    def __init__(self, first_name, last_name, salary, level):
        super().__init__(first_name, last_name, salary)
        self.level = level

    def __str__(self):
        return super().__str__().replace("Person", "Manager")


manager1 = Manager("A", "B", 66666, 12)
print(manager1)

# Сделать класс типа списка, который принимает в себ ятолье нечетные числа
class ListOfUneven(list):

    def append(self, x):
        if x % 2 == 1:
            super().append(x)
        else:
            raise ValueError("Список принимает только нечетные числа")

    def __setitem__(self, key, value):
        if value % 2 == 1:
            super().__setitem__(key, value)
        else:
            raise ValueError("Список принимает только нечетные числа")


list1 = ListOfUneven([200, 200]) #надо бы еще преркрыть конструктор
list1.append(1)
list1.append(3)
print(list1)
#list1.append(2) #error

#list1[0] = 22 #error
list1[0] = 111
print(list1)
