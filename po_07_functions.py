def plus(x: int, y: int, tax: float = 0) -> float:
    result = (x + y) * (1 - tax)
    return result


print(plus(x=1, y=2, tax=0.1))
z = plus(2, 3)
print(z)

# print(plus("a", "b", ))

def summa(x, y, *args):
    result = x + y
    for a in args:
        result += a
    return result

print(summa(1, 2, 33, 44, 55))

def dummy(x, y, *args, **kwargs):
    for key in kwargs:
        print(key, kwargs[key])

dummy(1, 2, a=12, b=34, c=56)

def plus_minus(x: int, y:int) -> (int, int):
    result1 = x + y
    result2 = x - y
    return result1, result2

a, b = plus_minus(1, 2)
print(a)
print(b)

def get_people_from_file(
            path: str,
            encoding: str = "utf-8",
            itemseparator: str = "\n",
            attributeseparator=";"
        ) -> list[dict[str, any] ]:
    with open(path, encoding=encoding) as f:
            text = f.read()
    lines = text.split(itemseparator)

    people = []
    for line in lines:
        splitted = line.split(attributeseparator)
        people.append(
            {'firstName': splitted[0], 'lastName': splitted[1], 'salary': float(splitted[2])}
        )
    return people

print(get_people_from_file("data/people.csv"))
