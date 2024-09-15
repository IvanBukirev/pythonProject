from sympy.diffgeom import twoform_to_matrix


def simple_multiplication(x, y):
    return (100 - ((100 - x) + (100 - y))) * 100 + ((100 - x) * (100 - y))


def multiplication_check(x, y):
    return x * y == simple_multiplication(x, y)


def multiplication_check_list_1(start=10, stop=99):
    n = 0
    m = 0
    for i in range(start, stop + 1):
        for j in range(start, stop + 1):
            if multiplication_check(i, j):
                n += 1
            else:
                m += 1
    print(f'Правильных результатов: {n}')
    print(f'Неправильных результатов: {m}')


def wisdom_multiplication(x, y, length_check=True):
    one = 100 - ((100 - x) + (100 - y))
    two = (100 - x) * (100 - y)

    if length_check and two < 10:
        return int(str(one) + '0' + str(two))

    else:
        return int(str(one) + str(two))

def multiplication_check_list(start=10, stop=99, length_check = True):
    n = 0
    m = 0
    for i in range(start, stop + 1):
        for j in range(start, stop + 1):
            if wisdom_multiplication(i, j, length_check)==i*j:
                n += 1
            else:
                m += 1
    print(f'Правильных результатов: {n}')
    print(f'Неправильных результатов: {m}')

multiplication_check_list(98, 99, False)
