# Класс, который инкапсулирует
# 1. извлечение списка слов из файла словаря
# 2. получение статистики частот по буквам
# 3. получение сатистики по длинам слов

class Vocabulary:

    def __init__(self, path: str, encoding: str = "utf-8", separator: str = "\n"):
        with open(path, encoding=encoding) as f:
            text = f.read()
        self.words = text.split(separator)

    def statistics_letters(self):
        text = str().join(self.words)
        letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        results = {}
        for letter in letters:
            results[letter] = text.count(letter)
        return results

    def statistics_length(self):
        results = {}
        for i in range(0, 30):
            results[i] = 0
        for w in self.words:
            results[len(w)] += 1
        return results


vocab1 = Vocabulary("data/RusDictionary.txt")
words1 = vocab1.words
print(words1[0: 100])
print(vocab1.statistics_letters())
print(vocab1.statistics_length())