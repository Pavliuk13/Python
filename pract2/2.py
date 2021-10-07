import re

class Statistic:
    def __init__(self, name):
        if not open(name, "r"):
            raise FileNotFoundError
        self.__file = open(name, "r")
        self.__text = self.__file.read()

    def countSymbol(self):
        return len(self.__text)
    
    def countSentences(self):
        return len(re.split(r'[.?!]+', self.__text)) - 1
    
    def countWords(self):
        return len(self.__text.split())


if __name__ == "__main__":
    try:
        fileName = "lorem.txt"
        stats = Statistic(fileName)
        print("Symbols: ", stats.countSymbol()) # Symbols: 28
        print("Words: ", stats.countWords()) # Words: 5
        print("Sentences: ", stats.countSentences()) # Sentences: 5
    except:
        print("Error! File not found")


