

def calculate_structure_sum(values):
    sum_of_all = 0
    if isinstance(values, (int, float)):
        sum_of_all += values
    elif isinstance(values, str):
        sum_of_all += len(values)
    elif isinstance(values, (list, tuple, set)):
        for element in values:
            sum_of_all += calculate_structure_sum(element)
    elif isinstance(values, dict):
        for key, value in values.items():
            sum_of_all += calculate_structure_sum(value)
            sum_of_all += calculate_structure_sum(key)
    return sum_of_all

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
