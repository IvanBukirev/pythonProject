def rotor(symbol, n, reverse=False):

    ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
              4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
              5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
              6: 'JPGVOUMFYQBENHZRDKASXLICTW',
              7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
              8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
              'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
              'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
              }
    i = 0
    if reverse:
        i, n = n, 0
    ch = ROTORS[n][ROTORS[i].index(symbol)]
    return ch


def reflector(symbol, n):
    REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
                  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
                  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
                  }
    ch = REFLECTORS[n][REFLECTORS[0].index(symbol)]
    return ch


def enigma(text, ref, rot1, rot2, rot3):
    text = text.upper()
    message_ = ''
    for ch in text:
        if ch.isalpha():
            ch = rotor(ch, rot3, reverse=False)
            ch = rotor(ch, rot2, reverse=False)
            ch = rotor(ch, rot1, reverse=False)
            ch = reflector(ch, ref)
            ch = rotor(ch, rot1, reverse=True)
            ch = rotor(ch, rot2, reverse=True)
            ch = rotor(ch, rot3, reverse=True)
            message_ += ch
    return message_


print(enigma('LDRBBKJMWGFBOFBYF', 1, 1, 2, 3))
