from math import gcd

class Rational:
    """ Class for working with rational numbers """
    def __init__(self, numerator = 1, denumerator = 2):
        if not denumerator:
            raise ZeroDivisionError("Error: denumerator == 0")
        if not isinstance(numerator, int) or not isinstance(denumerator, int):
            raise TypeError("Wrong type of arguments")
        n = gcd(numerator, denumerator)
        self.__numerator = numerator // n
        self.__denumerator = denumerator // n

    @property
    def numerator(self):
        """ getter for the numerator """
        return self.__numerator
    
    @property
    def denumerator(self):
        """ getter for the denumerator """
        return self.__denumerator



    def __add__(self, item):
        """ adding two rational numbers and adding an integer to a rational one """
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)

        self.__numerator *= item.denumerator
        self.__numerator += self.__denumerator * item.numerator
        self.__denumerator *= item.denumerator
        return Rational(self.__numerator, self.__denumerator)

    def __sub__(self, item):
        """ the difference of two rational numbers and the difference of an integer to a rational one """
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)
        
        self.__numerator *= item.denumerator
        self.__numerator -= self.__denumerator * item.numerator
        self.__denumerator *= item.denumerator
        return Rational(self.__numerator, self.__denumerator)

    def __mul__(self, item):
        """ multiplication of two rational numbers and multiplication of an integer to a rational one """
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)

        return Rational(self.__numerator * item.numerator, self.__denumerator * item.denumerator) 

    def __truediv__(self, item):
        """division of two rational numbers and division of an integer to a rational one"""
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)
        
        return Rational(self.__numerator * item.denumerator, self.__denumerator * item.numerator)

    def __eq__(self, item):
        """ checking the equality of two rational numbers """
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)

        firts_value = self.numerator / self.denumerator
        second_value = item.numerator / item.denumerator
        return firts_value == second_value

    def __ne__(self, item):
        """ checking the inequality of two rational numbers """
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)

        firts_value = self.numerator / self.denumerator
        second_value = item.numerator / item.denumerator
        return firts_value != second_value

    def __lt__(self, item):
        """ checks whether the first fraction is less than the second """
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)

        firts_value = self.numerator / self.denumerator
        second_value = item.numerator / item.denumerator
        return firts_value < second_value

    def __le__(self, item):
        """ checks whether the first fraction is less than or equal to the second """
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)

        firts_value = self.numerator / self.denumerator
        second_value = item.numerator / item.denumerator
        return firts_value <= second_value

    def __gt__(self, item):
        """ checks whether the first fraction is more than the second """
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)

        firts_value = self.numerator / self.denumerator
        second_value = item.numerator / item.denumerator
        return firts_value > second_value

    def __ge__(self, item):
        """ checks whether the first fraction is more than or equal to the second """
        if not isinstance(item, Rational) and not isinstance(item, int):
            raise TypeError("Wrong type")

        if isinstance(item, int):
            item = Rational(item, 1)

        firts_value = self.numerator / self.denumerator
        second_value = item.numerator / item.denumerator
        return firts_value >= second_value

    def __str__(self):
        if self.denumerator != 1 and self.numerator:
            return f'{self.numerator}/{self.denumerator}'
        return f'{self.numerator}'



if __name__ == "__main__":
    try:
        r1 = Rational(1, 5)
        r2 = Rational(110, 220)

        print(r2) # 1/2
        r1 = r1 + r2
        print(r1) # 7/10
        print(r1 > r2) #  true
        print(r1 == r2)#  false
    except Exception as ex:
        print(ex)