#  Полиморфизм и утиная типизация.
#  И каким образом питон обходится без интерфейсов и абстрактных классов

class Animal:

    def __init__(self):
        raise SyntaxError("Это абстрактный класс")

    def voice(self):
        return ""


class Cat(Animal):

    def __init__(self):
        pass

    def voice(self):
        return "Meaow"


class Dog(Animal):

    def __init__(self):
        pass

    def voice(self):
        return "Hab"

cat = Cat()
dog = Dog()
# animal = Animal() # error

print(cat.voice(), dog.voice())

def call(animal: Animal):
    print("come to me!")
    print(animal.voice())

call(cat)
call(dog)
# call(animal)
# call(123)