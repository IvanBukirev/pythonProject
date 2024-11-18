
class Person():
    '''
    Класс Person.
    '''
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_person(self):
        print (f'Hi, my name is {self.name} and my age is {self.age} and my gender is {self.gender}')


Petya= Person('Petya', 20, 'male')


def introspection_info(obj):

    return {
            'type': type(obj).__name__,
            'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")],
            'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
            'module': getattr(obj, "__module__", None),
            'class': obj.__class__.__name__,
            'doc': obj.__doc__,
    }




obj_info=introspection_info(Petya)
print(obj_info)

number_info = introspection_info(42)
print(number_info)