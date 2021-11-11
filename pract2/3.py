class Student:
    def __init__(self, name, surname, number, evaluation):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(number, int) or not isinstance(evaluation, list):
            raise TypeError("Wrong type of variables")
        if not len(name) or not len(surname) or number < 0 or not all(isinstance(x, int) for x in evaluation) or not all(x > 0 and x <= 5 for x in evaluation) or not (0 < len(evaluation) <= 5):
            raise ValueError("Not correct data")
        self.__name = name
        self.__surname = surname
        self.__number = number
        self.__evaluation = evaluation

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong type")
        if not len(name):
            raise ValueError("Name can't be empty")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Wrong type")
        elif not len(surname):
            raise ValueError("Surname can't be empty")
        self.__surname = surname

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if isinstance(number, int):
            raise TypeError("Wrong type")
        if number < 0:
            raise ValueError("Wrong number of record book")
        self.__number = number

    @property
    def evaluation(self):
        return self.__evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        if not isinstance(evaluation, list):
            raise TypeError("Wrong type")
        if not all(isinstance(x, int) for x in evaluation) or not all(x > 0 and x <= 5 for x in evaluation) or not (0 < len(evaluation) < 5):
            raise ValueError("Wrong data")
        self.__evaluation = evaluation

    def average_score(self):
        return round(sum(self.__evaluation) / len(self.__evaluation))

MAX_STUDENTS = 20

class Group:
    def __init__(self):
        self.__group = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Wrong type of variable")
        if len(self.__group) == MAX_STUDENTS:
            raise IndexError("Maximum number of students")

        for st in self.__group:
            if st.name == student.name:
                raise ValueError("Such a student already exists")
            if st.number == student.number:
                raise ValueError("Record book number already exists")
        self.__group.append(student)
        self.__group = sorted(self.__group, key =  lambda st : st.average_score() , reverse = True)

    def best_five(self):
        return self.__group[:5]


if __name__ == "__main__":
    try:
        student1 = Student("Junior", "Moraes", 1, [3, 2, 3, 3, 5])
        student2 = Student("Mykola", "Matvienko", 2, [5, 5, 5, 5, 5])
        student3 = Student("Marcos", "Antonio", 3, [4, 5, 4, 2, 5])
        student4 = Student("Anatoliy", "Trubin", 4, [5, 2, 5, 3, 5])
        student5 = Student("Taras", "Stepanenko", 5, [4, 1, 5, 3, 5])
        student6 = Student("Mykhailo", "Mudryk", 6, [5, 5, 5, 3, 5])
        student7 = Student("Alan", "Patrick", 7, [5, 5, 5, 5, 5])

        ti01 = Group()
        ti01.add_student(student1)
        ti01.add_student(student2)
        ti01.add_student(student3)
        ti01.add_student(student4)
        ti01.add_student(student5)
        ti01.add_student(student6)
        ti01.add_student(student7)

        best = ti01.best_five()
        for i in best:
            print(i.name, i.surname, i.average_score())
                                                        # Mykola Matvienko 5
                                                        # Mykhailo Mudryk 5
                                                        # Alan Patrick 5
                                                        # Marcos Antonio 4
                                                        # Anatoliy Trubin 4
    except Exception as ex:
        print(ex)