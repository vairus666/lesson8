from form import figure

SELECTOR = {
    '1': figure.area_qa,
    '2': figure.area_ri,
    '3': figure.area_tr,
    '4': figure.per_qa,
    '5': figure.per_ri,
    '6': figure.per_tr,
    '7': figure.volume_ri
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
            print('Не понял, попробуйте еще раз')
        else:
            print('До встречи')
            break

my_figure = figure()
actions(my_figure)
