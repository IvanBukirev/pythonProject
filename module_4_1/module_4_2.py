def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

# inner_function() - функция определена внутри функции test_function(), и если раскоментировать эту строку, возникнет
#                    ошибка.
test_function()
