from abc import ABC, abstractmethod
import json


class ICourse(ABC):
    """Interface for courses"""
    @property
    @abstractmethod
    def name(self): pass

    @name.setter
    @abstractmethod
    def name(self, name): pass

    @property
    @abstractmethod
    def teacher(self): pass

    @teacher.setter
    @abstractmethod
    def teacher(self): pass

    @property
    @abstractmethod
    def themes(self): pass

    @themes.setter
    @abstractmethod
    def themes(self): pass


class ILocalCourse(ABC):
    """Interface for local courses"""
    @property
    @abstractmethod
    def type(self): pass


class IOffsiteCourse(ABC):
    """Interface for offsite courses"""
    @property
    @abstractmethod
    def type(self): pass


class ITeacher(ABC):
    """Interface for teachers"""
    @property
    @abstractmethod
    def full_name(self): pass

    @full_name.setter
    @abstractmethod
    def full_name(self, full_name): pass

    @property
    @abstractmethod
    def courses(self): pass

    @courses.setter
    @abstractmethod
    def courses(self, courses): pass


class ICourseFactory(ABC):
    """Interface for courses factory"""
    @abstractmethod
    def create_course(self, type_course, name, teacher, themes): pass

    @abstractmethod
    def create_teacher(self, full_name, courses): pass


class Course(ICourse):
    """Class for courses"""
    def __init__(self, name, teacher, themes):
        self.name = name
        self.teacher = teacher
        self.themes = themes

    @property
    def name(self):
        """getter for course name"""
        return self._name

    @name.setter
    def name(self, name):
        """setter for course name"""
        if not isinstance(name, str):
            raise TypeError("Wrong type of 'name' variable")
        if not name:
            raise ValueError("Name can't be empty")
        self._name = name

    @property
    def teacher(self):
        """getter for teacher of course"""
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        """setter for teacher of course"""
        if not isinstance(teacher, Teacher):
            raise TypeError("Wrong type of 'teacher' variable")
        self._teacher = vars(teacher)

    @property
    def themes(self):
        """getter for themes in course"""
        return self._themes

    @themes.setter
    def themes(self, themes):
        """setter for themes in course"""
        if not isinstance(themes, list):
            raise TypeError("Wrong type of 'themes' variable")
        if not themes:
            raise ValueError("Themes list can't be empty")
        self._themes = themes

    def __str__(self):
        return f'Name of course: {self.name}\nTeacher: {self.teacher["_full_name"]}\nThemes:{",".join(self.themes)}'


class Teacher(ITeacher):
    """Interface for teachers"""
    def __init__(self, full_name, courses):
        self.full_name = full_name
        self.courses = courses

    @property
    def full_name(self):
        """getter for full name of teacher"""
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """setter for full name of teacher"""
        if not isinstance(full_name, str):
            raise TypeError("Wrong type of 'full_name' variable")
        if not full_name:
            raise ValueError("Full name can't be empty")
        self._full_name = full_name

    @property
    def courses(self):
        """getter for courses"""
        return self._courses

    @courses.setter
    def courses(self, courses):
        """setter for courses"""
        if not isinstance(courses, list):
            raise TypeError("Wrong type of 'courses' variable")
        self._courses = courses

    def __str__(self):
        return f'Full name: {self.full_name}\nCourses: {",".join(self.courses)}'


class LocalCourse(Course, ILocalCourse):
    """Class for local courses"""
    def __init__(self, name, teacher, themes):
        super().__init__(name, teacher, themes)
        self._type = 'Local'

    @property
    def type(self):
        """getter for course type"""
        return self._type

    def __str__(self):
        return f'{super().__str__()}\nType: {self.type}'


class OffsiteCourse(Course, IOffsiteCourse):
    """Class for offsite courses"""
    def __init__(self, name, teacher, themes):
        super().__init__(name, teacher, themes)
        self._type = 'Offsite'

    @property
    def type(self):
        """getter for course type"""
        return self._type

    def __str__(self):
        return f'{super().__str__()}\nType: {self.type}'


class CourseFactory(ICourseFactory):
    """Class for course factory"""
    def __init__(self, courses_path, teachers_path):
        self.__courses_path = courses_path
        self.__teachers_path = teachers_path

    def create_course(self, type_course, name, teacher, themes):
        """a function that creates a course in an academy"""
        if not isinstance(type_course, str):
            raise TypeError("Wrong type for 'type_course' variable")
        if type_course == 'Local':
            course = LocalCourse(name, teacher, themes)
        elif type_course == 'Offsite':
            course = OffsiteCourse(name, teacher, themes)
        else:
            raise ValueError("Wrong type of courses")

        with open(self.__teachers_path, "r") as file:
            data = json.load(file)

        for item in data:
            if item["_full_name"] == teacher.full_name:
                item["_courses"].append(name)
                teacher.courses = item["_courses"]

        with open(self.__teachers_path, "w") as file:
            json.dump(data, file, indent=4)

        with open(self.__courses_path, "r") as file:
            data = json.load(file)

        to_json = vars(course)
        data.append(to_json)

        with open(self.__courses_path, "w") as file:
            json.dump(data, file, indent=4)

        return course

    def create_teacher(self, full_name):
        """a function that creates a teacher in an academy"""
        teacher = Teacher(full_name, [])

        with open(self.__teachers_path, "r") as file:
            data = json.load(file)

        to_json = vars(teacher)
        data.append(to_json)

        with open(self.__teachers_path, "w") as file:
            json.dump(data, file, indent=4)

        return teacher


def all_teachers(path):
    """A function that displays all teachers of the academy"""
    with open(path, "r") as file:
        data = json.load(file)
    teachers = []
    for item in data:
        teachers.append(Teacher(item["_full_name"], item["_courses"]))
    return teachers


def all_courses(path):
    """A function that displays all courses of the academy"""
    with open(path, "r") as file:
        data = json.load(file)
    courses = []
    for item in data:
        if item["_type"] == "Local":
            courses.append(
                LocalCourse(item["_name"], Teacher(item["_teacher"]["_full_name"], item["_teacher"]["_courses"]),
                            item["_themes"]))
        else:
            courses.append(
                OffsiteCourse(item["_name"], Teacher(item["_teacher"]["_full_name"], item["_teacher"]["_courses"]),
                            item["_themes"]))

    return courses


if __name__ == "__main__":
    factory = CourseFactory("courses.json", "teachers.json")
    teacher1 = factory.create_teacher("Pavel Valeriyovich Durov")
    teacher2 = factory.create_teacher("Yurii Adamovich Tarnavskiy")
    course1 = factory.create_course("Local", "Java", teacher2, ["OOP", "Strings"])
    course2 = factory.create_course("Offsite", "Telegram on Python", teacher1, ["Bot", "OOP"])

    all_c = all_courses("courses.json")
    all_t = all_teachers("teachers.json")
    for item in all_c:
        print(item)
        print()

    for item in all_t:
        print(item)
        print()

