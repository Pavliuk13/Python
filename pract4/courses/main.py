from interfaces import *
from uuid import uuid4
from pymongo import MongoClient
from config import host, db, teachers_collection, courses_collection


class Course(ICourse):
    """Class for courses"""
    def __init__(self, name, teachers, themes):
        self.name = name
        self.teachers = teachers
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
    def teachers(self):
        """getter for teachers of course"""
        return self._teachers

    @teachers.setter
    def teachers(self, teachers):
        """setter for teachers of course"""
        if not isinstance(teachers, list):
            raise TypeError("Wrong type of 'teacher' variable")
        self._teachers = teachers

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

    def add_teacher(self, teacher_name):
        """add teacher for current course"""
        if not isinstance(teacher_name, str):
            raise TypeError("Wrong type of 'teacher_name' variable")
        if not teacher_name:
            raise ValueError("'teacher_name' can't be empty")
        self._teachers.append(teacher_name)

    def __iter__(self):
        return Iterator(self.teachers)

    def __str__(self):
        return f'Name of course: {self.name}\nTeachers: {",".join(self.teachers)}\nThemes:{",".join(self.themes)}'


class LocalCourse(Course, ILocalCourse):
    """Class for local courses"""
    def __init__(self, name, teachers, themes):
        super().__init__(name, teachers, themes)
        self._type = 'Local'

    @property
    def type(self):
        """getter for course type"""
        return self._type

    def __str__(self):
        return f'{super().__str__()}\nType: {self.type}'


class OffsiteCourse(Course, IOffsiteCourse):
    """Class for offsite courses"""
    def __init__(self, name, teachers, themes):
        super().__init__(name, teachers, themes)
        self._type = 'Offsite'

    @property
    def type(self):
        """getter for course type"""
        return self._type

    def __str__(self):
        return f'{super().__str__()}\nType: {self.type}'


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

    def add_course(self, course_name):
        """add course for teacher"""
        if not isinstance(course_name, str):
            raise TypeError("Wrong value for 'course_name' variable")
        if not course_name:
            raise ValueError("'course_name' can't be empty")
        self._courses.append(course_name)

    def __iter__(self):
        return Iterator(self.courses)

    def __str__(self):
        return f'Full name: {self.full_name}\nCourses: {",".join(self.courses)}'


class Iterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.wrapped):
            raise StopIteration()
        self.index += 1
        return self.wrapped[self.index - 1]


class CourseFactory(ICourseFactory):
    """Class for course factory"""
    def __init__(self):
        self.client = MongoClient(host)
        self.db = self.client[db]
        self.teachers = self.db[teachers_collection]
        self.courses = self.db[courses_collection]

    def create_course(self, type_course, name, themes):
        """a function that creates a course in an academy"""
        if not isinstance(type_course, str):
            raise TypeError("Wrong type for 'type_course' variable")
        if type_course == 'Local':
            course = LocalCourse(name, [], themes)
        elif type_course == 'Offsite':
            course = OffsiteCourse(name, [], themes)
        else:
            raise ValueError("Wrong type of course")

        check = self.courses.find_one({"name": name})
        if check:
            raise ValueError("Course is registered in the system")

        record = {"_id": uuid4().__str__(), "name": name, "teachers": [], "themes": themes, "type": type_course}
        self.courses.insert_one(record)

        return course

    def create_teacher(self, full_name):
        """a function that creates a teacher in an academy"""
        teacher = Teacher(full_name, [])

        check = self.teachers.find_one({"full_name": full_name})
        if check:
            raise ValueError("Teacher is registered in the system")

        record = {"_id": uuid4().__str__(), "full_name": full_name, "courses": []}
        self.teachers.insert_one(record)

        return teacher

    def organization(self, course, teachers):
        """a function that allows you to assign to a teacher's course"""
        if not isinstance(course, Course) or not isinstance(teachers, list) or not all(isinstance(teacher, Teacher) for teacher in teachers):
            raise TypeError("Wrong type of variables")

        for teacher in teachers:
            teacher.add_course(course.name)
            course.add_teacher(teacher.full_name)
            courses = self.teachers.find_one({"full_name": teacher.full_name})["courses"]
            courses.append(course.name)
            self.teachers.update_one({"full_name": teacher.full_name}, {"$set": {"courses": courses}})

        self.courses.update_one({"name": course.name}, {"$set": {"teachers": course.teachers}})

    def all_teachers(self):
        """a function that finds all teachers in a database"""
        teachers = []
        items = self.teachers.find({})
        for item in items:
            teachers.append(Teacher(item["full_name"], item["courses"]))
        return teachers

    def all_courses(self):
        """a function that finds all courses in a database"""
        courses = []
        items = self.courses.find({})
        for item in items:
            if item["type"] == "Local":
                courses.append(LocalCourse(item["name"], item["teachers"], item["themes"]))
            else:
                courses.append(OffsiteCourse(item["name"], item["teachers"], item["themes"]))
        return courses


if __name__ == "__main__":
    factory = CourseFactory()
    teacher1 = factory.create_teacher("Steve Jobs")
    teacher2 = factory.create_teacher("Yurii Adamovich Tarnavskiy")
    course1 = factory.create_course("Local", "Java", ["OOP", "Strings"])
    course2 = factory.create_course("Offsite", "Kotlin", ["OOP"])
    factory.organization(course1, [teacher2])
    factory.organization(course2, [teacher1])
    print(teacher1)






