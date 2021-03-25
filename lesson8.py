from form import figure
import math


class unfigure(figure):
    def area_tr(self):
        a = float(input('Введите сторону а\n'))
        b = float(input('Введите сторону b\n'))
        c = float(input('Введите сторону с\n'))
        p = (a+b+c)/2
        area = math.sqrt(p * (p-a) * (p-b) * (p-c))
        print(f"Площадь треугольника равна = {area:.2f}")

SELECTOR = {
    '1': unfigure.area_qa,
    '2': unfigure.area_ri,
    '3': unfigure.area_tr,
    '4': unfigure.per_qa,
    '5': unfigure.per_ri,
    '6': unfigure.per_tr,
    '7': unfigure.volume_ri
    }


def is_int(string):
    return string.isdigit()

def actions(figure):
    while True:
        string = input("""
        Что делаем?
        1: Площадь четырехугольника,
        2: Площадь круга,
        3: Площадь треугольника,
        4: Периметр четырехугольника,
        5: Периметр круга,
        6: Периметр треугольника,
        7: ОБъем шара
        """)
        if string and SELECTOR.get(string):
                SELECTOR.get(string)(figure)
        elif string:
            print('Не знаю такой команды')
        else:
            print('Пока')
            break

my_figure = figure()
actions(my_figure)
