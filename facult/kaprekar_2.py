def kaprekar(n):
    n2 = n ** 2
    str_n2 = str(n2)
    for i in range(1, len(str_n2)):
        if (int(str_n2[:i]) + int(str_n2[i:])) == n:
            return ((f'True\n'
                     f'{n}**2 = {n2}\n'
                     f'{str_n2[:i]} + {str_n2[i:]} = {int(str_n2[:i]) + int(str_n2[i:])}'))
            break
        else:
            return False


print(kaprekar(45))

# (f'True\n'
# f'{n}**2 = {n2}\n'
# f'{str_n2[:i]} + {str_n2[i:]} = {int(str_n2[:i]) + int(str_n2[i:])}')
