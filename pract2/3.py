class Student:
    def __init__(self, name, surname, number, evaluation):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(number, int) or not isinstance(evaluation, list):
            raise TypeError("Wrong type of variables")
        elif not len(name) or not len(surname) or number < 0 or not all(isinstance(x, int) for x in evaluation) or not all(x > 0 and x <= 5 for x in evaluation) or len(evaluation) < 5 or len(evaluation) > 5:
            raise ValueError("Not correct data")
        self.__name = name
        self.__surname = surname
        self.__number = number
        self.__evaluation = evaluation

    def FullName(self):
        return f'{self.__name} {self.__surname}'

    def setName(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong type")
        elif not len(name):
            raise ValueError("Name can't be empty")
        self.__name = name
    
    def getName(self):
        return self.__name

    def setSurname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Wrong type")
        elif not len(surname):
            raise ValueError("Surname can't be empty")
        self.__surname = surname

    def getSurname(self):
        return self.__surname

    def setNumber(self, number):
        if isinstance(number, int):
            raise TypeError("Wrong type")
        elif number < 0:
            raise ValueError("Wrong number of record book")
        self.__number = number

    def getNumber(self):
        return self.__number

    def setEvaluation(self, evaluation):
        if not isinstance(evaluation, list):
            raise TypeError("Wrong type")
        elif not all(isinstance(x, int) for x in evaluation) or not all(x > 0 and x <= 5 for x in evaluation) or len(evaluation) < 5 or len(evaluation) > 5:
            raise ValueError("Wrong data")
        self.__evaluation = evaluation

    def getEvauation(self):
        return self.__evaluation

    def AverageScore(self):
        return round(sum(self.__evaluation) / len(self.__evaluation))

MAX_STUDENTS = 20

class Group:
    def __init__(self):
        self.__group = []

    def AddStudent(self, student):
        if not isinstance(student, Student):
            raise TypeError("Wrong type of variable")
        elif len(self.__group) == MAX_STUDENTS:
            raise IndexError("Maximum number of students")

        for st in self.__group:
            if st.FullName() == student.FullName():
                raise ValueError("Such a student already exists")
            elif st.getNumber() == student.getNumber():
                raise ValueError("Record book number already exists")
        self.__group.append(student)
        self.__SortGroup()

    def __SortGroup(self):
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
            raise ValueError("Group is empty")
        info = ""
        for i in range(0, len(self.__group)):
            info += f'#{i + 1} {self.__group[i].FullName()}: {self.__group[i].AverageScore()}' + '\n'
        return info


if __name__ == "__main__":
    try:
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
    except Exception as ex:
        print(ex)