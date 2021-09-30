class Rectangle:
    def __init__(self):
        self.__length, self.__width = 1, 1
    
    def setLength(self, item):
        try:
            if item <= 0.0 or item > 20.0 or not isinstance(item, float):
                raise ValueError             
            else:
                self.__length = item
                return True
        except:
            return False

    def getLength(self):
        return self.__length

    def setWidth(self, item):
        try:
            if item <= 0.0 or item > 20.0 or not isinstance(item, float):
                raise ValueError
            else:
                self.__width = item
                return True
        except:
            return False

    def getWidth(self):
        return self.__width

    def perimetr(self):
        return self.getLength() * 2 + self.getWidth() * 2

    def area(self):
        return self.getWidth() * self.getLength()



rec = Rectangle()
print("Try to set length:", rec.setLength(11.1)) # True
print("Try to set width:", rec.setWidth(20.0))   # True
print(rec.getLength(), rec.getWidth(), rec.perimetr(), rec.area()) #10.0 20.0 60.0 200.0