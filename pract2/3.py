class Student:
    def __init__(self, name, surname, number, evaluation):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(number, int) or not isinstance(evaluation, list):
            raise TypeError
        elif not len(name) or not len(surname) or number < 0 or not all(isinstance(x, int) for x in evaluation) or not all(x > 0 and x <= 5 for x in evaluation):
            raise ValueError
        self.__name = name
        self.__surname = surname
        self.__number = number
        self.__evaluation = evaluation

    def FullName(self):
        return f'{self.__name} {self.__surname}'

    def Evauation(self):
        arr = map(str, self.__evaluation)
        return ", ".join(arr)

    def AverageScore(self):
        res = 0
        for i in self.__evaluation:
            res += i
        res /= len(self.__evaluation)
        return round(res)

    def studentInfo(self):
        return f'Student: {self.FullName()}. Record book number: {self.__number}. Evaluation: {self.Evauation()}. Average score: {self.AverageScore()}'

class Group:
    def __init__(self):
        self.__group = []

    def AddStudent(self, student):
        if not isinstance(student, Student):
            raise TypeError
        elif len(self.__group) == 20:
            raise IndexError
        self.__group.append(student)
        self.SortGroup()

    def SortGroup(self):
        values = []
        for st in self.__group:
            values.append(st.AverageScore())
        
        for i in range(0, len(values) - 1):
            for j in range(0, len(values) - i - 1):
                if values[j] < values[j + 1]:
                    values[j], values[j + 1] = values[j + 1], values[j]
                    self.__group[j], self.__group[j + 1] = self.__group[j + 1], self.__group[j]

    def BestFive(self):
        if len(self.__group) < 5:
            return self.FullList()
        else:
            info = ""
            for i in range(0, 5):
                info += f'#{i + 1} {self.__group[i].FullName()}: {self.__group[i].AverageScore()}' + '\n'
            return info

    def FullList(self):
        if not len(self.__group):
            return None
        info = ""
        for i in range(0, len(self.__group)):
            info += f'#{i + 1} {self.__group[i].FullName()}: {self.__group[i].AverageScore()}' + '\n'
        return info


if __name__ == "__main__":
    student1 = Student("Junior", "Moraes", 1, [3, 2, 3, 3, 5])
    student2 = Student("Mykola", "Matvienko", 2, [5, 5, 5, 5, 5])
    student3 = Student("Marcos", "Antonio", 3, [4, 5, 4, 2, 5])
    student4 = Student("Anatoliy", "Trubin", 4, [5, 2, 5, 3, 5])
    student5 = Student("Taras", "Stepanenko", 5, [4, 1, 5, 3, 5])
    student6 = Student("Mykhailo", "Mudryk", 6, [5, 5, 5, 3, 5])
    student7 = Student("Alan", "Patrick", 7, [1, 1, 1, 3, 5])

    ti01 = Group()
    ti01.AddStudent(student1)
    ti01.AddStudent(student2)
    ti01.AddStudent(student3)
    ti01.AddStudent(student4)
    ti01.AddStudent(student5)
    ti01.AddStudent(student6)
    ti01.AddStudent(student7)

    print(ti01.BestFive() + '\n')
    print(ti01.FullList())