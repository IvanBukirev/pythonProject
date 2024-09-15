from decimal import *

getcontext().prec = 50


# def  luka(L0, L1, n):
#     for _ in range(n):
#         L0, L1 = L1, L0 + L1
#     return L0

# def fi(L0, L1, n):
#     for i in range(1, n):
#         L0, L1 = L1, L0 + L1
#     return Decimal(L1)/Decimal(L0)


# def fi(L0, L1, n):
#     return Decimal(luka(L0, L1, n)) / Decimal(luka(L0, L1, n - 1))
def super_L(n):
    L0, L1 = 2, 1
    for _ in range(n):
        L0, L1 = L1, L0 + L1
    return L0


print(super_L(180))
