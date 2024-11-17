import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


# numpy
class Numpy:
    arr = np.arange(10)  # create array
    squared_arr = np.square(arr)  # square array
    average_value = np.mean(arr)  # average value
    standard_deviation = np.std(arr)  # standard deviation
    flip_arr = np.flip(arr)  # flip
    print(f"Исходный массив: {arr}")
    print(f"Возведение в квадрат: {squared_arr}")
    print(f"Среднее значение: {average_value}")
    print(f"Стандартное отклонение: {standard_deviation}")
    print(f"Переворот массива: {flip_arr}")


# matplotlib
class Matplotlib:
    x = [5, 4, 3, 2, 1]  # Задаем данные по осям
    y = [10, 20, 15, 25, 30]
    plt.plot(x, y)  # Построение линейного графика
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.title('Пример линейного графика')
    plt.savefig('plot.jpg')
    plt.show()

    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 12, 67, 34]
    plt.xlabel('наименование')
    plt.ylabel('значения')
    plt.bar(categories, values)
    plt.title('Пример столбчатой диаграммы')
    plt.savefig('bar.jpg')
    plt.show()

    x = np.linspace(-5, 5, 100)  # X от -5 до 5
    y = x ** 2
    plt.plot(x, y)
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.title('График функции y=x**2')
    plt.savefig('function.jpg')
    plt.show()



# PIL
class Pillow:
    image = Image.open(r'C:\Users\ivan\PycharmProjects\pythonProject\module_11\image.jpg')
    resized_image = image.resize((800, 800))  # изменение размера на 800 x 800 пикселей
    resized_image.save('resized_image.jpg')

    # image = Image.open(r'C:\Users\ivan\PycharmProjects\pythonProject\module_11\image.jpg')
    blurred_image = image.filter(ImageFilter.GaussianBlur(10))  # применить эффекты
    blurred_image.save('blurred_image.jpg')

    # сохранить в другой формат
    # image = Image.open(r'C:\Users\ivan\PycharmProjects\pythonProject\module_11\image.jpg')
    image.save('converted_image.png')  # конвертация в формат PNG
    image.save('converted_image.gif')  # конвертация в формат GIF

    # переворачивает изображение слева направо, в результате чего получается зеркальное отображение
    # image = Image.open(r'C:\Users\ivan\PycharmProjects\pythonProject\module_11\image.jpg')
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)  # зеркальное отображение
    flipped_image.save('flipped_image.jpg')
