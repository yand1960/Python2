# people = [
#     ["Yuri", "Andrienko", 123456],
#     ["Vasya", "Pupkin", 77777],
#     ["Masha", "Mashkina", 300000]
# ]
# for p in people:
#     print(f"{p[0]} {p[1]} has salary {p[2]}")
#
# person1 = {
#     "firstName": "Yuri",
#     "lastName": "Andrienko",
#     "salary": 123456
# }
#
# print(f"{person1['firstName']} {person1['lastName']} has salary {person1['salary']}")

people = [
    {
        "firstName": "Yuri",
        "lastName": "Andrienko",
        "salary": 123456
    },
    {
        "firstName": "Vasya",
        "lastName": "Pupkin",
        "salary": 77777
    },
    {
        "firstName": "Masha",
        "lastName": "Mashkina",
        "salary": 300000
    },
]

for p in people:
    print(f"{p['firstName']} {p['lastName']} has salary {p['salary']}")

# 1. Найти среднюю зарплату
# 2. Вывести фамилию самого выкооплачиваемого сотрудника (19:44)
summa = 0
for p in people:
    summa += p['salary']
    # summa = summa + p['salary']
print(f"Average salary: {summa / len(people)}")

richest = people[0]
for p in people:
    if p['salary'] > richest['salary']:
        richest = p
print(f"Most highly paid person is {richest['lastName']}")

nums = (1, 2, 3)
#nums.append(77)
#nums[0] = 11
print(nums)

set1 = {1, 2, 3}
set2 = {2, 2, 3, 4}
set3 = set(nums)
print(set1, set2, set3)
print(set1.intersection(set2))

print(people[1]['lastName'])

person1 = people[2]

for key in person1:
    print(key, person1[key])

for key, value in people[0].items():
    print(f"{key}: {value}")

for p in people:
    if p['salary'] > 100000:
        print(p['lastName'])
        break

i = 0
while i < len(people):
    print(people[i]['firstName'])
    i += 1

iterator = iter(people)
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))


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

for p in people:
    print(f"{p['lastName']}, {p['firstName']}")
    if 'children' in p.keys():
        print("\tChildren:")
        for c in p['children']:
            print(f"\t\t{c['name']}")