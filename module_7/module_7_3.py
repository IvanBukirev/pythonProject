class WordsFinder:
    def __init__(self,* file_names):
        self.file_names=file_names

    def get_all_words(self):
        all_words={}
        for file_names in self.file_names:
            with open(file_names, encoding='utf-8') as file:
                read=file.read().lower()
                for symbol in ['.', '=', '!', '?', ';', ':', ' - ']:
                    read = read.replace(symbol, '')
                words = read.split()
            all_words[file_names] = words
        return all_words


    def find(self, word):
        word_find = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                word_find[file_name] = words.index(word) + 1
        return word_find




    def count(self, word):
        count_word = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                count_word[file_name] = words.count(word)
        return count_word

# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))