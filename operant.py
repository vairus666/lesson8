
class Home:
    """
    Изменение оперантов +, -, *, / на противоположные
    """
    def __init__(self, test:int):
        self.__test = test 

    def getFormatTest(self):
        s = self.__test      
        return f"{Home.__getForm(s)}"

    def __getForm(x):
        return str(x)

    def getTest(self):
        return self.__test

    def __sub__(self, other): 
        return Home(self.__test + other.getTest())
        
    def __mul__(self, other):
        return Home(self.__test / other.getTest())

    def __truediv__(self, other):
        return Home(self.__test * other.getTest())

    def __add__(self, other):
        return Home(self.__test - other.getTest())

test1 = Home(10)
test2 = Home(5)
test3 = test1 + test2
print(test3.getFormatTest())
test3 = test1 - test2
print(test3.getFormatTest())
test3 = test1 * test2
print(test3.getFormatTest())
test3 = test1 / test2
print(test3.getFormatTest())



