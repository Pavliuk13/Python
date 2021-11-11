class Rectangle:
    def __init__(self, length = 1.0, width = 1.0):
        if not isinstance(length, float) or not isinstance(width, float):
            raise TypeError("Wrong type of variables")
        if not (0.0 < length <= 20.0) or not (0.0 < width <= 20.0):
           raise ValueError("Wrong data") 
        self.__length, self.__width = length, width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if not isinstance(length, float):
            raise TypeError("Wrong type of variables")
        if not (0.0 < length <= 20.0):
           raise ValueError("Wrong data") 
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError("Wrong type of variables")
        if not (0.0 < width <= 20.0):
           raise ValueError("Wrong data") 
        self.__width = width

    def perimetr(self):
        return self.length * 2 + self.width * 2

    def area(self):
        return self.width * self.length


if __name__ == "__main__":
    try:
        rec = Rectangle(15.0, 20.0)
        print(rec.length, rec.width, rec.perimetr(), rec.area()) #15.0 20.0 70.0 300.0
    except Exception as ex:
        print(ex)
