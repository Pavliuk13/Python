class Rational:
    def __init__(self, numerator = 1, denumerator = 2):
        try:
            if not denumerator:
                raise ZeroDivisionError
            self.__nummerator = int(numerator / self.__gcd(numerator, denumerator))
            self.__denumerator = int(denumerator / self.__gcd(numerator, denumerator))
        except:
            self.__nummerator, self.__denumerator = 1, 2
            return None

    def __add__(self, item):
        self.__nummerator *= item.getDen()
        num = self.__denumerator * item.getNum()
        self.__nummerator += num
        self.__denumerator *= item.getDen()
        return Rational(self.__nummerator, self.__denumerator)

    def __sub__(self, item):
        self.__nummerator *= item.getDen()
        num = self.__denumerator * item.getNum()
        self.__nummerator -= num
        self.__denumerator *= item.getDen()
        return Rational(self.__nummerator, self.__denumerator)

    def __mul__(self, item):
        return Rational(self.__nummerator * item.getNum(), self.__denumerator * item.getDen()) 

    def __truediv__(self, item):
        return Rational(self.__nummerator * item.getDen(), self.__denumerator * item.getNum())

    def __gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def showData(self):
        return str(self.__nummerator) + "/" + str(self.__denumerator)
    
    def showPoint(self):
        return self.__nummerator / self.__denumerator
    
    def getNum(self):
        return self.__nummerator
    
    def getDen(self):
        return self.__denumerator


rational = Rational(9, 45)
print(rational.showData()) # 1/5
print(rational.showPoint()) # 0.2

zero = Rational(9, 0) # Zero division
print(zero.showData()) # 1/2
print(zero.showPoint()) # 0.5

test = Rational(5, 55)
print(test.showData()) # 1/11
print(test.showPoint()) # 0.090909090909

obj = rational + test
print(obj.showData()) # 16/55

obj /= zero
print(obj.showData()) # 32/55