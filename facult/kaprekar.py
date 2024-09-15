def kaprekar_check(n):
    if not n % 100:
        return False
    elif len(set(str(n))) == 1:
        return False
    return len(str(n)) in [3, 4, 6]


def numerics(n):
    return list(map(int, str(n)[::-1]))


def kaprekar_step(L):
    s1 = "".join(map(str, sorted(L)))
    s2 = ''.join(map(str, sorted(L)[::-1]))
    return int(s2) - int(s1)


def kaprekar_loop(n):
    if not kaprekar_check(n):
        print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')
    else:
        set_et = [495, 6174, 549945, 631764]
        se = [n]
        print(n)
        while n  not in set_et:
            n = kaprekar_step(numerics(n))
            if n in se:
                print(f'Следующее число - {n}, кажется процесс зациклился...')
                break
            else:
                print(n)
                se.append(n)

kaprekar_loop(103303)
