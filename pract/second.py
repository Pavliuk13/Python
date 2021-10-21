from math import gcd

class Rational:
    def __init__(self, numerator = 1, denumerator = 2):
        if not denumerator:
            raise ZeroDivisionError("Error: denumerator == 0")
        n = gcd(numerator, denumerator)
        self.__nummerator = int(numerator / n)
        self.__denumerator = int(denumerator / n)

    def __add__(self, item):
        self.__nummerator *= item.getDenumerator()
        num = self.__denumerator * item.getNumerator()
        self.__nummerator += num
        self.__denumerator *= item.getDenumerator()
        return Rational(self.__nummerator, self.__denumerator)

    def __sub__(self, item):
        self.__nummerator *= item.getDenumerator()
        num = self.__denumerator * item.getNumerator()
        self.__nummerator -= num
        self.__denumerator *= item.getDen()
        return Rational(self.__nummerator, self.__denumerator)

    def __mul__(self, item):
        return Rational(self.__nummerator * item.getNum(), self.__denumerator * item.getDen()) 

    def __truediv__(self, item):
        return Rational(self.__nummerator * item.getDen(), self.__denumerator * item.getNum())

    def showData(self):
        return str(self.__nummerator) + "/" + str(self.__denumerator)
    
    def showPoint(self):
        return self.__nummerator / self.__denumerator
    
    def getNumerator(self):
        return self.__nummerator
    
    def getDenumerator(self):
        return self.__denumerator



if __name__ == "__main__":
    try:
        rational = Rational(9, 45)
        print(rational.showData()) # 1/5
        print(rational.showPoint()) # 0.2

        test = Rational(5, 55)
        print(test.showData()) # 1/11
        print(test.showPoint()) # 0.090909090909

        obj = rational + test
        print(obj.showData()) # 16/55

    except Exception as ex:
        print(ex)