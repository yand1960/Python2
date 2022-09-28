# Найти все семейства слов-анаграм в русском языке ("пост-стоп" и т.д.)

with open("data/RusDictionary.txt", encoding = "utf-8") as f:
    text = f.read()

words = text.split("\n")
# print(words[0:100])

# w1 = "пост"
# w2 = "стоп"
#
# print(str.join("", sorted(w1)))

def sorted_string(word):
    return str.join("", sorted(word))


# for w1 in words:
#     for w2 in words:
#         if  w1 != w2 and  sorted_string(w1) == sorted_string(w2):
#             print(w1, w2)

hashes = []
# for w in words:
#     hashes.append([sorted_string(w), w])
#
# sorted_hashes = sorted(hashes, key= lambda h: h[0])
# #print(sorted_hashes[0:100])
#
# for i in range(1, len(sorted_hashes)):
#     if sorted_hashes[i][0] == sorted_hashes[i - 1][0]:
#         print(sorted_hashes[i -1][1],sorted_hashes[i][1] )

# самое большое (=длинное) семейство анаграмм
hashes = {}
for w in words:
    hashes[sorted_string(w)] = []

for w in words:
    hashes[sorted_string(w)].append(w)

for key in hashes:
    if len(hashes[key]) > 1:
        print(hashes[key])

print("Самые длинные семейства:")
max_len = len(max(hashes.values(), key = lambda anagrams: len(anagrams)))
for anagrams in hashes.values():
    if len(anagrams) >= max_len -1:
        print(anagrams)




