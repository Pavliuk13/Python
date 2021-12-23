from abc import abstractmethod, ABC


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
    def teachers(self): pass

    @teachers.setter
    @abstractmethod
    def teachers(self, teachers): pass

    @property
    @abstractmethod
    def themes(self): pass

    @themes.setter
    @abstractmethod
    def themes(self, themes): pass

    @abstractmethod
    def add_teacher(self, teacher_name): pass

    @abstractmethod
    def __iter__(self): pass


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

    @abstractmethod
    def add_course(self, course_name): pass

    @abstractmethod
    def __iter__(self): pass


class ICourseFactory(ABC):
    """Interface for courses factory"""
    @abstractmethod
    def create_course(self, type_course, name, themes): pass

    @abstractmethod
    def create_teacher(self, full_name): pass

    @abstractmethod
    def organization(self, course, teachers): pass
