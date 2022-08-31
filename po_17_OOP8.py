#  Полиморфизм и утиная типизация

class Cat:
    def voice(self):
        return "Meaow"

class Dog:
    def voice(self):
        return "Hab"

cat = Cat()
dog = Dog()

print(cat.voice(), dog.voice())

def call(animal):
    print("come to me!")
    print(animal.voice())

call(cat)
call(dog)
# call(123)