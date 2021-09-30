class Rectangle:
    def __init__(self):
        self.__length, self.__width = 1, 1
    def setLength(self, item):
        try:
            if item <= 0.0 or item > 20.0:
                print("Value must be in range (0.0, 20.0]")
            elif not isinstance(item, float):
                print("Type must be 'float'")
            else:
                self.__length = item
        except:
            print("Error value")

    def getLength(self):
        return self.__length

    def setWidth(self, item):
        try:
            if item <= 0.0 or item > 20.0:
                print("Value must be in range (0.0, 20.0]")
            elif not isinstance(item, float):
                print("Type must be 'float'")
            else:
                self.__width = item
        except:
            print("Value error")

    def getWidth(self):
        return self.__width

    def perimetr(self):
        return self.getLength() * 2 + self.getWidth() * 2

    def area(self):
        return self.getWidth() * self.getLength()

rec = Rectangle()
rec.setLength(10.0)
rec.setWidth(20.0)
print(rec.getLength(), rec.getWidth(), rec.perimetr(), rec.area()) #10.0 20.0 60.0 200.0