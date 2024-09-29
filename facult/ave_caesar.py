'''
Реализуйте функцию caesar(text, key), возвращающую зашифрованный текст, работающую только с латинским алфавитом.

text - исходных текст, который надо зашифровать (или расшифровать)
key - ключ (сдвиг)
Ключ может быть отрицательным или больше 26

Из преобразуемого текста удаляются все пробелы и знаки препинания. Зашифрованный текст пишется в верхнем регистре 1 строкой.

'''


# def caesar(text, key,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     text = text.upper()
#     decrypted_back = ''
#     for i in text:
#         if i in alphabet:
#             decrypted_back += i
#
#     encrypted = ''
#     for i in decrypted_back:
#         index = alphabet.find(i)
#         index += key
#         n=index//len(alphabet)
#         if index > len(alphabet)-1:
#             index -= len(alphabet)*abs(n)
#         elif index < 0:
#             index += len(alphabet)*abs(n)
#         encrypted += alphabet[index]
#     # return encrypted
#     return f'Encrypted: {encrypted}\nDecrypted back: {decrypted_back}'


# def caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     table = dict(zip(alphabet, alphabet[key:] + alphabet[:key]))
#     return ''.join(table[c] for c in text.upper() if c in table)

# print(caesar("Ave caesar",3))
#
# def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     for i in range(-1, -len(alphabet), -1):
#         print(caesar(text, i, alphabet))

# def caesar(text, key, alphabet):
#     text = text.upper()
#     encoded = ''
#     for ch in text:
#         if ch in alphabet:
#             encoded += alphabet[(alphabet.find(ch) + key) % len(alphabet)]
#     return encoded
#

#
# def disc_generator(alphabet):
#     seed(42)
#     alphabet = ''.join(sample(alphabet, len(alphabet)))[::-1]
#     return alphabet
#
# def disc_generator(alphabet):
#     seed(42)
#     alphabet = list(alphabet)
#     shuffle(alphabet)
#     alphabet = ''.join(alphabet)
#     return alphabet
#
# clear_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# n = 36
# text = "Съешь еще этих мягких французских булок. Кстати, в этом тексте пришлось заменить одну букву"
#
# discs=[disc_generator(clear_alphabet) for i in range (n)]
#
# def jefferson_encryption(text, discs, step, reverse=False):
#     if reverse:
#         step *= -1
#     # if reverse: di = alphabet[::-1]
#     text = text.upper()
#     encoded = ''
#     i = 0
#     for ch in text:
#
#         encoded += discs[i][(discs[i].find(ch) + step) % len(discs[i])]
#         i+= 1
#         if i == len(discs):
#             i = 0
#     return encoded
#
#
# print(jefferson_encryption(text, discs, 4, reverse=False))


def kidds_encryption(text, reverse=False):
    text = text.lower()
    liter = "ethosnairfdlmbyguvcp"
    simvl = "8;4‡)*56(1†092:3?¶-."
    encoded = ''
    if reverse: liter, simvl = simvl, liter
    for ch in text:
        if ch in liter:
            encoded += simvl[liter.find(ch)]
    return encoded


print(kidds_encryption('8;4‡)*56(1†092:3?¶-.', reverse=True))
