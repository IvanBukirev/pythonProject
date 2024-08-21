calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    s = (len(string), string.upper(), string.lower())
    count_calls()
    return s


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    return any(item in string for item in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(string_info('аБРкАДАбра'))
print(is_contains('Студент', ['СТУдень', 'СтУДент', 'СТУДЕНТЫ']))
print(calls)
