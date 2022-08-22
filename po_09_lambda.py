from typing import Callable

def f1(x):
    return x * 2

print(f1(1))

# Функции можно присваивать и передавать в другие функции
f2 = f1
print(f2(2))
f3 = f2
print(f3(3))

# Обобщенная функция - ей могут передаваться как аргументы другие функции
def f4(x: int, f: Callable[ [int], int]) -> int:
    x += 1
    result = f(x)
    return result

print(f4(4, f2))

# Задача о трансформации списка
data = [1, 2, 3, 4]
# results = []
# for x in data:
#     results.append(x * x)
# results = [x * x for x in data]

def transform(data, convert_one):
    results = []
    for x in data:
        results.append(convert_one(x))
    return results


print(transform(data, f1))

def to_square(x):
    return x * x
print(transform(data, to_square))

# Это полный эквивалент трех верхних строк
print(transform(data, lambda x: x * x))
print(transform(data, lambda x: x * x * x))
print(transform(data, lambda x: 2 * x))

#Задача о фильтрации списка
data = [1, 2, 55, 3, 4, 66]
def select(data, predicate):
    results =[]
    for x in data:
        if predicate(x):
            results.append(x)
    return results

print(select(data, lambda x: x > 10))
print(select(data, lambda x: x < 10))


# Применение стандартных функций Питона для трансформации, фильтрации и сортировки
data = [1, 2, 55, 3, 4, 66]
results = list(map(lambda x: x * x, data))
print(results)
print(list(map(lambda x: x * x * x, data)))

results = list(filter(lambda x: x > 10, data))
print(results)

data1 = [(1, 1), (2, 2),  (4, 4), (5, 55), (3, 33)]
# Одной строкой получить спискок кортежей из data1, у которых второй член больше 10 (20:14)
results = list(filter(lambda x: x[1] > 10, data1))
print(results)

results = sorted(data1, key=lambda x: x[1])
print(results)

people = [
    {
        "firstName": "Yuri",
        "lastName": "Andrienko",
        "salary": 123456
    },
    {
        "firstName": "Vasya",
        "lastName": "Pupkin",
        "salary": 77777,
        "children": [
            {"name": "Kola", "gender": "m"},
            {"name": "Lena", "gender": "f"},
        ]
    },
    {
        "firstName": "Masha",
        "lastName": "Mashkina",
        "salary": 300000
    },
]

# 1. Отсортировать список людей в порядке возрастания зарплаты
# 2. Одной строкой кода вывести фамилию. самого высокооплачиваемого сотрудника
# 20:40

print(sorted(people, key=lambda p: p['salary']))
print(sorted(people, key=lambda p: -p['salary'])[0]['lastName'])

# Найти среднюю зарплату в одну строку кода
# data = [1, 2, 55, 3, 4, 66]
# print(sum(data))
print(sum(list(map(lambda p: p['salary'], people))) / len(people))
