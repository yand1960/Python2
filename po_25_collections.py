from collections import deque, namedtuple

nums = deque([1, 2, 3])
nums.append(777)
nums.appendleft(-777)
print(nums)
x = nums.pop()
print(x)
print(nums)
y = nums.popleft()
print(y)
print(nums)

Person = namedtuple("Person",["first_name", "last_name"])
p1 = Person(first_name="Yuri", last_name= "Andrienko")
print(f"{p1.last_name}, {p1.first_name}")