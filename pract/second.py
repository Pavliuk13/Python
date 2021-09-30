class Rational:
    def __init__(self, numerator = 1, denumerator = 2):
        try:
            if not denumerator:
                self.__nummerator, self.__denumerator = 1, 2
                raise ValueError
            self.__nummerator = int(numerator / self.__gcd(numerator, denumerator))
            self.__denumerator = int(denumerator / self.__gcd(numerator, denumerator))
        except:
            print("Zero division")

    def __gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def showData(self):
        print(str(self.__nummerator) + "/" + str(self.__denumerator))
    
    def showPoint(self):
        print(self.__nummerator / self.__denumerator)


rational = Rational(9, 45)
rational.showData() # 1/5
rational.showPoint() # 0.2

zero = Rational(9, 0) # Zero division
zero.showData() # 1/2
zero.showPoint() # 0.5

test = Rational(5, 55)
test.showData() # 1/11
test.showPoint() # 0.090909090909