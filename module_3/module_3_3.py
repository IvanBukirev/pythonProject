# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params("sds",False,36)
print_params()
print_params(3)
print_params(c=8, a='fmksldfklsdf')
print_params('sdsd',True,{'f':17})
print_params(b=25)
print_params(c=[1, 2, 3])
#print_params(2,4,'trrt','56')  - возникнет ошибка. передано параметров больше чем принимает функция

#2.Распаковка параметров:
print()
values_list=('string', 58, True)
values_dict={'a': False, 'b': 35, 'c': 'trtrtrt'}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
print()
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)