import datetime as dt

def days_left_till_new_year():
    #  это комментарий
    today = dt.date.today()
    new_year = dt.date(2023,1,1)
    return (new_year - today).days

if __name__ == "__main__":
    print(days_left_till_new_year())

    x = 32
    y = 2
    result = x + y
    print(f"Result: {result}")
    print(f"{x}+{y}={result}")

    first_name = "Yuri"
    last_name = "Andrienko"
    # full_name = first_name + " " + last_name
    full_name = f"{first_name} {last_name}"
    print(full_name)
    name_with_initial = first_name[0:2] + "." + last_name
    print(name_with_initial)

    full_name = "Vasya Pupkin"
    space_position = full_name.find(" ")
    first_name = full_name[0:space_position]
    last_name = full_name[space_position + 1:]
    print(first_name)
    print(last_name)
    official_name = f"{last_name}, {first_name}"
    print(official_name)

    numbers = [1, 2, 3, 55, 4, 66, 7]
    print(numbers[1])
    numbers.append(88)

    for x in numbers:
        if x > 10:
            print(x)

    # for i in range(0, len(numbers)):
    #     print(numbers[i])

    data1 = [1, 2, 3]
    data2 = [2, 3, 4]

    for x1 in data1:
        for x2 in data2:
            if x1 == x2:
                print(x1)

    #Улучшите асимтотику

    # https://github.com/yand1960/python2