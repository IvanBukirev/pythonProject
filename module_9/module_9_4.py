import random

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

letter_comparison_list = list(map(lambda x, y: x == y, first, second))
print(letter_comparison_list)


# Замыкание:
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_set:
                file.write("%s\n" % item)
                # print(item, file=file) или так

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())