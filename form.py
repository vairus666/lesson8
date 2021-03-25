import math

class figure:

    def area_tr(self):
        a = float(input('Введите сторону а\n'))
        b = float(input('Введите сторону b\n'))
        c = float(input('Введите сторону с\n'))
        p = (a+b+c)/2
        area = math.sqrt(p * (p-a) * (p-b) * (p-c))
        print(f"Площадь треугольника равна = {area:.2f}")

    def area_qa(self):
        a = float(input('Введите диагональ а\n'))
        b = float(input('Введите диагональ b\n'))
        c = float(input('Введите угол между диагоналями\n'))
        area = (a*b)/2*math.sin(math.radians(c))
        print(f"Площадь четыреугольника равна = {area:.2f}")

    def area_ri(self):
        r = float(input('Введите радиус\n'))
        area = math.pi*(r**2)
        print(f"Площадь круга равна = {area:.2f}")

    def per_tr(self):
        a = float(input('Введите сторону а\n'))
        b = float(input('Введите сторону b\n'))
        c = float(input('Введите сторону с\n'))
        per = (a+b+c)
        print(f"Площадь треугольника равна = {per:.2f}")

    def per_qa(self):
        a = float(input('Введите сторону а\n'))
        b = float(input('Введите сторону b\n'))
        c = float(input('Введите сторону с\n'))
        d = float(input('Введите сторону d\n'))
        per = (a+b+c+d)
        print(f"Площадь четырехугольника равна = {per:.2f}")    

    def per_ri(self):
        r = float(input('Введите радиус\n'))
        per = 2*math.pi*r
        print(f"Площадь круга равна = {per:.2f}")       

    def volume_ri(self):
        r = float(input('Введите радиус\n'))
        vol = (4*math.pi*r**3)/3
        print(f"Объем шара равен = {vol:.2f}")


