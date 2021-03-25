import math

class figure:
    a = b = c = 1
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print('Шалом')
        

    def area(self, a , b, c = 0):
        if self.form == 'triangle':
            p = (a+b+c)/2
            self.area_f = math.sqrt(p * (p-a) * (p-b) * (p-c))
            print(f"Площадь треугольника равна = {self.square_f}")
        elif self.form == 'square':
            self.area_f = a*b
            print(f"Площадь прямоугольника равна = {self.square_f}")
        elif self.form == 'ring':
            self.area_f = math.pi*(a**2)
            print(f"Площадь прямоугольника равна = {self.square_f}")

    def per(self, a, b, c):
        if self.form == 'triangle':
            self.per_f = (a+b+c)
            print(f"Площадь треугольника равна = {self.per_f}")
        elif self.form == 'rectangle':
            self.per_f = (a+b) * 2
            print(f"Площадь прямоугольника равна = {self.per_f}")
        elif self.form == 'ring':
            self.per_f = (math.pi*a)/2
            print(f"Площадь прямоугольника равна = {self.per_f}")

    







