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

del(a)
print(a)