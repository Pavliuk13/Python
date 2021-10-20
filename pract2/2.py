import re

class Statistic:
    def __init__(self, name):
        if not len(name):
            return ValueError
        elif not open(name, "r"):
            raise FileNotFoundError
        self.__name = name

    def countSymbol(self):
        text = ""
        with open(self.__name, 'r') as f:
            text = f.read()
        return len(text)
    
    def countSentences(self):
        text = ""
        with open(self.__name, 'r') as f:
            text = f.read()
        return len(re.split(r'[.?!]+', text)) - 1
    
    def countWords(self):
        text = ""
        with open(self.__name, 'r') as f:
            text = f.read()
        return len(text.split())


if __name__ == "__main__":
    try:
        fileName = r'E:\prog works\python\test\pract2\lorem.txt'
        stats = Statistic(fileName)
        print("Symbols: ", stats.countSymbol()) # Symbols: 28
        print("Words: ", stats.countWords()) # Words: 5
        print("Sentences: ", stats.countSentences()) # Sentences: 5
    except:
        print("Error! File not found")
