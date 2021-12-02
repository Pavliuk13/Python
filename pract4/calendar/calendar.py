from const import DAYS_IN_MONTHS, START_YEAR, LAST_MONTH, FIRST_MONTH, REGULAR_YEAR, NUMBER_OF_MONTHS, STARTS_OF_MONTHS


class AddValues:
    """ A class that stores the value you want to add to the date """
    def __init__(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("Wrong type of variable")
        if value < 0:
            raise ValueError("Wrong value of variable")
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value


class Day(AddValues):
    """ A class that describes the number of days """
    def __init__(self, value = 0) -> None:
        super().__init__(value = value)


class Month(AddValues):
    """ A class that describes the number of months """
    def __init__(self, value = 0) -> None:
        super().__init__(value = value)


class Year(AddValues):
    """ A class that describes the number of years """
    def __init__(self, value = 0) -> None:
        super().__init__(value = value)


class Calendar:
    """ Class calendar that stores the date """
    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    @property
    def day(self) -> int:
        """ getter for the day """
        return self.__day

    @day.setter
    def day(self, day):
        """ setter for the day """
        if not isinstance(day, int):
            raise TypeError("Wrong type of 'day' variable")

        max_day = DAYS_IN_MONTHS[self.month - 1]
        if self.month == 2 and self.__is_leap():
            max_day += 1

        if not 0 < day <= max_day:
            raise ValueError("Wrong day")

        self.__day = day


    def __is_leap(self) -> bool:
        """ a function that determines whether a year is leap """
        return not self.year % 4 and self.year % 100 or not self.year % 400
            
    @property
    def month(self) -> int:
        """ getter for the month """
        return self.__month

    @month.setter
    def month(self, month):
        """ setter for the month """
        if not isinstance(month, int):
            raise TypeError("Wrong type of 'month' variable")
        if not FIRST_MONTH <= month <= LAST_MONTH:
            raise ValueError("Wrong month")
        self.__month = month

    @property
    def year(self) -> int:
        """ getter for the year """
        return self.__year

    @year.setter
    def year(self, year):
        """ setter for the year """
        if not isinstance(year, int):
            raise TypeError("Wrong type of 'year' variable")
        if year < START_YEAR:
            raise ValueError("Wrong year")
        self.__year = year

    def __str__(self) -> str:
        return f'{self.day}-{self.month}-{self.year}'

    def __iadd__(self, count):
        """ adds to the date: days, months, years """
        if isinstance(count, Day):
            curr_day = STARTS_OF_MONTHS[self.month - 1] + self.day
            curr_day += count.value

            if self.__is_leap():
                leap = 1
            else:
                leap = 0

            while curr_day > REGULAR_YEAR:
                curr_day -= REGULAR_YEAR
                self.year += 1
                if self.__is_leap():
                    leap += 1
                    
            curr_day -= leap

            i = 0
            for m in STARTS_OF_MONTHS:
                if m > curr_day:
                    break
                i += 1

            self.day = curr_day - STARTS_OF_MONTHS[i - 1]
            self.month = i
        elif isinstance(count, Month):

            if not count.value % NUMBER_OF_MONTHS:
                self.year += count.value // NUMBER_OF_MONTHS
            else:
                month = (self.month + count.value) // NUMBER_OF_MONTHS
                self.year += month
                self.month += count.value - NUMBER_OF_MONTHS * month
                if self.day > DAYS_IN_MONTHS[self.month - 1]:
                    self.day = DAYS_IN_MONTHS[self.month - 1]
        elif isinstance(count, Year):
            self.year += count.value
        else:
            raise TypeError("Wrong type")

        return Calendar(self.day, self.month, self.year)

    
    def __isub__(self, count):
        """ subtracts from the date: days, months, years """
        if isinstance(count, Day):
            curr_day = STARTS_OF_MONTHS[self.month - 1] + self.day
            curr_day = abs(curr_day - count.value)
            
            if self.__is_leap():
                leap = 1
            else:
                leap = 0

            while curr_day > REGULAR_YEAR:
                curr_day -= REGULAR_YEAR
                self.year -= 1
                if self.__is_leap():
                    leap += 1
                    
            self.year -= 1
            curr_day = REGULAR_YEAR - curr_day + leap

            i = 0
            for m in STARTS_OF_MONTHS:
                if m > curr_day:
                    break
                i += 1

            self.day = curr_day - STARTS_OF_MONTHS[i - 1]
            self.month = i
        elif isinstance(count, Month):

            if not count.value % NUMBER_OF_MONTHS:
                self.year -= count.value // NUMBER_OF_MONTHS
            else:
                month = abs(self.month + count.value) // NUMBER_OF_MONTHS
                self.year -= month
                self.month -= abs(count.value - NUMBER_OF_MONTHS * month)
                if self.day > DAYS_IN_MONTHS[self.month - 1]:
                    self.day = DAYS_IN_MONTHS[self.month - 1]
        elif isinstance(count, Year):
            self.year += count.value
        else:
            raise TypeError("Wrong type")

        return Calendar(self.day, self.month, self.year)

    def __gt__(self, date):
        """ compare dates '>' """
        if not isinstance(date, Calendar):
            raise TypeError("Wrong type")
        if self.year > date.year:
            return True
        elif self.year == date.year:
            if self.month > date.month:
                return True
            elif self.month == date.month:
                if self.day > date.day:
                    return True
        return False

    def __ge__(self, date):
        """ compare dates '>=' """
        if not isinstance(date, Calendar):
            raise TypeError("Wrong type")
        if self.year > date.year:
            return True
        elif self.year == date.year:
            if self.month > date.month:
                return True
            elif self.month == date.month:
                if self.day >= date.day:
                    return True
        return False

    def __lt__(self, date):
        """ compare dates '<' """
        if not isinstance(date, Calendar):
            raise TypeError("Wrong type")
        if self.year < date.year:
            return True
        elif self.year == date.year:
            if self.month < date.month:
                return True
            elif self.month < date.month:
                if self.day < date.day:
                    return True
        return False

    def __le__(self, date):
        """ compare dates '<=' """
        if not isinstance(date, Calendar):
            raise TypeError("Wrong type")
        if self.year < date.year:
            return True
        elif self.year == date.year:
            if self.month < date.month:
                return True
            elif self.month < date.month:
                if self.day <= date.day:
                    return True
        return False

    def __eq__(self, date) -> bool:
        """ compare dates '==' """
        if not isinstance(date, Calendar):
            raise TypeError("Wrong type")
        if self.year == date.year and self.month == date.month and self.day == date.day:
            return True
        return False

    def __ne__(self, date) -> bool:
        """ compare dates '!=' """
        if not isinstance(date, Calendar):
            raise TypeError("Wrong type")
        if self.year == date.year and self.month == date.month and self.day == date.day:
            return False
        return True



if __name__ == "__main__":
    c1 = Calendar(1, 12, 2021)
    print(c1) # 1-12-2021
    c1 += Day(111)
    print(c1) # 22-3-2022
    c1 -= Month(13)
    print(c1) # 22-2-2021
    c1 += Year(12)
    print(c1) # 22-2-2033