class Rectangle:
    def __init__(self, length = 1.0, width = 1.0):
        if not isinstance(length, float) or not isinstance(width, float):
            raise TypeError("Wrong type of variables")
        elif length <= 0.0 or width <= 0.0 or length > 20.0 or width > 20.0:
           raise ValueError("Wrong data") 
        self.__length, self.__width = length, width

    def setLength(self, length):
        if not isinstance(length, float):
            raise TypeError("Wrong type of variables")
        elif length <= 0.0 or length > 20.0:
           raise ValueError("Wrong data") 
        self.__length = length

    def setWidth(self, width):
        if not isinstance(width, float):
            raise TypeError("Wrong type of variables")
        elif width <= 0.0 or width > 20.0:
           raise ValueError("Wrong data") 
        self.__width = width

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

    def perimetr(self):
        return self.getLength() * 2 + self.getWidth() * 2

    def area(self):
        return self.getWidth() * self.getLength()


if __name__ == "__main__":
    try:
        rec = Rectangle(15.0, 20.0)
        print(rec.getLength(), rec.getWidth(), rec.perimetr(), rec.area()) #15.0 20.0 70.0 300.0
    except Exception as ex:
        print(ex)
