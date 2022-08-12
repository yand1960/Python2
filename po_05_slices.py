s = "Hello, world!"

print(s[2:5]) # llo
print(s[2: ]) #llo, world!
print(s[:5]) # Hello
print(s[0:7:2]) # Hlo
print(s[::2]) # Hlo ol!
print(s[-2:]) # d!
print(s[::-1]) # !dlrow ,olleH

#https://github.com/yand1960/python2

#  Найти все слова, которые заканчиваются цо

with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()

words = text.split("\n")
#print(words[0:100])
for w in words:
    if w[-2:] == "цо":
        print(w)

# Найти все слова взаимные полиндромы: зал-лаз (асимтотика лучше, чем O(n2))
# for w1 in words:
#     for w2 in words:
#         if w1 == w2[::-1]:
#             print(w1, w2)

# reversed = []
# for w in words:
#     reversed.append(w[::-1])

# reversed = [w[::-1]  for w in words]
# print(reversed[0:100])
#
# print(set(words).intersection(set(reversed)))

print(set(words).intersection(set([w[::-1] for w in words])))

