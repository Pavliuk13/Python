import re

class Statistic:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name should be a string")
        if not len(name):
            raise ValueError("Not correct data")
        if not open(name, "r"):
            raise FileNotFoundError("File not found")
        self.__name = name

    def __readFile(self):
        with open(self.__name, 'r') as f:
            self.__text = f.read()

    def countSymbol(self):
        self.__readFile()
        return len(self.__text)

    def countSentences(self):
        self.__readFile()
        return len(re.split(r'[.?!]+', self.__text)) - 1
    
    def countWords(self):
        self.__readFile()
        return len(re.split(r'[\'\-\w]+', self.__text)) - 1


if __name__ == "__main__":
    try:
        fileName = r'E:\prog works\python\test\pract2\lorem.txt'
        stats = Statistic(fileName)
        print("Symbols: ", stats.countSymbol()) # Symbols: 28
        print("Words: ", stats.countWords()) # Words: 5
        print("Sentences: ", stats.countSentences()) # Sentences: 5
    except Exception as ex:
        print(ex)
