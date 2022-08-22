a = 123

def dummy(x: int) -> int:
    global a
    a = 777
    result = x * a
    return result

print(dummy(1))
# print(result)
print(a)

a = None

if a is None:
    print("a is none")

x1 = 1
x2 = 1.0
print(x1 == x2)
print(x1 is x2)


