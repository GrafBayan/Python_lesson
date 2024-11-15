import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        for item in file_names:
            self.file_names.append(item)


    def get_all_words(self):
        all_words = dict()
        del_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            temp_str = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                    for tchk in del_:
                        line = line.replace(tchk,"")
                    for word in line.split():
                        temp_str.append(word)
            all_words[name] = temp_str
        return all_words

    def find(self, word):
        find_ = {}
        for name, words in self.get_all_words().items():
            a = 0
            for word1 in words:
                a += 1
                if word.lower() == word1:
                    find_[name] = a
        return find_

    def count(self, word):
        count_ = {}
        for name, words in self.get_all_words().items():
            a = 0
            for word1 in words:
                if word.lower() == word1:
                    a += 1
            count_[name] = a
        return count_



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))