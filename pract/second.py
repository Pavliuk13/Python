from math import gcd

class Rational:
    def __init__(self, numerator = 1, denumerator = 2):
        if not denumerator:
            raise ZeroDivisionError("Error: denumerator == 0")
        if not isinstance(numerator, int) or not isinstance(denumerator, int):
            raise TypeError("Wrong type of arguments")
        n = gcd(numerator, denumerator)
        self.__nummerator = numerator // n
        self.__denumerator =denumerator // n

    def __add__(self, item):
        self.__nummerator *= item.denumerator
        num = self.__denumerator * item.numerator
        self.__nummerator += num
        self.__denumerator *= item.denumerator
        return Rational(self.__nummerator, self.__denumerator)

    def __sub__(self, item):
        self.__nummerator *= item.denumerator
        num = self.__denumerator * item.numerator
        self.__nummerator -= num
        self.__denumerator *= item.denumerator
        return Rational(self.__nummerator, self.__denumerator)

    def __mul__(self, item):
        return Rational(self.__nummerator * item.numerator, self.__denumerator * item.denumerator) 

    def __truediv__(self, item):
        return Rational(self.__nummerator * item.denumerator, self.__denumerator * item.numerator)

    def show_data(self):
        return f'{self.__nummerator}/{self.__denumerator}'
    
    def show_point(self):
        return self.__nummerator / self.__denumerator
    
    @property
    def numerator(self):
        return self.__nummerator
    
    @property
    def denumerator(self):
        return self.__denumerator



if __name__ == "__main__":
    try:
        rational = Rational(9, 45)
        print(rational.show_data()) # 1/5
        print(rational.show_point()) # 0.2

        test = Rational(5, 55)
        print(test.show_data()) # 1/11
        print(test.show_point()) # 0.090909090909

        obj = rational + test
        print(obj.show_data()) # 16/55

    except Exception as ex:
        print(ex)