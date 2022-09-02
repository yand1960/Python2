# Создать класс - наследник списка, в котором можно контролировать
# критерий, которому должен соответствовать каждый элемент списка


class ControlledList(list):

    def __init__(self, data, criteria):
        self._criteria = criteria
        for x in data:
            if not criteria(x):
                raise ValueError("Предоставленные данные не соответствуют критерию")
        super().__init__(data)

    def append(self, x):
        if self.criteria(x):
            super().append(x)
        else:
            raise ValueError("Предоставленные данные не соответствуют критерию")

    def __setitem__(self, key, value):
        if self.criteria(value):
            super().__setitem__(key, value)
        else:
            raise ValueError("Предоставленные данные не соответствуют критерию")

    def __add__(self, other):
        raise NotImplementedError("Операция + не определена для объектов этого типа")

    def __iadd__(self, other):
        raise NotImplementedError("Операция + не определена для объектов этого типа")

    @property
    def criteria(self):
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        for x in self:
            if not criteria(x):
                raise ValueError("Существующие данные не соответствуют критерию")


list1 = ControlledList([11, 221, 2221], lambda x: x > 10)
list1.append(12)
list1.criteria = lambda x: x > -10
# list1 += [22, 222]
print(list1)
