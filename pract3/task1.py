from datetime import datetime
import re
import json
import itertools
import time


class ITEvent:
    """A class that describes an event"""
    def __init__(self, date, desc, price):
        if not isinstance(date, str) or not ITEvent.check_date(date) or not isinstance(desc, str) or not isinstance(price, int):
            raise TypeError("Wrong type of variables")
        if not desc or price <= 0:
            raise ValueError("Wrong data")

        self._date = date
        self._desc = desc
        self._price = price
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("Wrong type of variables")
        if not ITEvent.check_date(date):
            raise ValueError("Wrong data")

        self._date = date

    @property
    def desc(self):
        return self._desc
    
    @desc.setter
    def desc(self, desc):
        if not isinstance(desc, str):
            raise TypeError("Wrong type of variable")
        if not desc:
            raise ValueError("Description can't be empty")
        self._desc = desc

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError
        if price <= 0:
            raise ValueError("Price must be more then 0")
        self._price = price

    def __str__(self):
        return f'Event: {self._desc}. Date of event: {self._date}'

    @staticmethod
    def check_date(date):
        if not isinstance(date, str):
            raise TypeError("Wrong type")
        try:
            valid_date = time.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            return False



class Regular:
    """Class for a regular ticket"""
    newid = itertools.count()
    def __init__(self, event: ITEvent, date, type = "regular"):
        if not isinstance(event, ITEvent) or not isinstance(date, str) or not isinstance(type, str):
            raise TypeError("Wrong type of variables")
        if not ITEvent.check_date(date) or not type in ["regular", "advance", "student", "late"]:
            raise ValueError("Wrong data")

        self._ticket_price = event.price
        self._type = type
        self._id = next(self.newid)
        self._event = event.__dict__
        self._date = date
    
    @property
    def ticket_price(self):
        return self._ticket_price

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id
    
    @property
    def date(self):
        return self._date

    def __str__(self):
        return f'Event: {self._event["_desc"]}\nDate of event: {self._event["_date"]}\nOrder date: {self._date}\nType of ticket: {self._type}\nPrice: {self._ticket_price}$'

    @staticmethod
    def get_price(event: ITEvent):
        if not isinstance(event, ITEvent):
            raise TypeError("Wrong type of variable")
        return event.price



class Advance(Regular):
    """Class for a advance ticket"""
    def __init__(self, event: ITEvent, date):
        super().__init__(event, date, "advance")
        self._ticket_price *= 0.6

    @staticmethod
    def get_price(event: ITEvent):
        if not isinstance(event, ITEvent):
            raise TypeError("Wrong type of variable")
        return event.price * 0.6



class Student(Regular):
    """Class for a student ticket"""
    def __init__(self, event: ITEvent, date):
        super().__init__(event, date, "student")
        self._ticket_price *= 0.5

    @staticmethod
    def get_price(event: ITEvent):
        if not isinstance(event, ITEvent):
            raise TypeError("Wrong type of variable")
        return event.price * 0.5



class Late(Regular):
    """Class for a late ticket"""
    def __init__(self, event: ITEvent, date):
        super().__init__(event, date, "late")
        self._ticket_price *= 1.1

    @staticmethod
    def get_price(event: ITEvent):
        if not isinstance(event, ITEvent):
            raise TypeError("Wrong type of argument")
        return event.price * 1.1
        


class Customer:
    def __init__(self, name, surname, phone, is_student):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(phone, str) or not isinstance(is_student, bool):
            raise TypeError("Wrong type")
        if not name or not surname or not re.match(r'380[0-9]{9}', phone):
            raise ValueError("Wrong value of argument")
        self._name = name
        self._surname = surname
        self._phone = phone
        self._is_student = is_student

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong type")
        if not name:
            raise ValueError("Wrong value of argument")
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Wrong type")
        if not surname:
            raise ValueError("Wrong value of argument")
        self._surname = surname

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Wrong type")
        if re.match(r'380[0-9]{9}', phone):
            raise ValueError("Wrong value of argument")
        self._phone = phone

    @property
    def is_student(self):
        return self._is_student

    @is_student.setter
    def is_student(self, is_student):
        if not isinstance(is_student, bool):
            raise TypeError("Wrong type")
        self._is_student = is_student

    def __str__(self) -> str:
        return f'{self._name} {self._surname} {self._phone}'



def order(event: ITEvent, customer: Customer, date):
    if not isinstance(customer, Customer) or not isinstance(event, ITEvent) or not isinstance(date, str):
        raise TypeError("Wrong type of variables")
    if not ITEvent.check_date(date):
        raise ValueError("Wrong date")
    
    ticket = None

    if customer.is_student:
            ticket = Student(event, date)

    else:
        date_order = datetime.strptime(date, "%d/%m/%Y")
        date_event = datetime.strptime(event.date, "%d/%m/%Y")
        t_days = (date_event - date_order).days

        if t_days >= 60:
            ticket = Advance(event, date)

        elif 0 <= t_days < 10:
            ticket = Late(event, date)

        elif t_days < 0:
            raise ValueError("Event is over")

        else:
            ticket = Regular(event, date)

    with open("data.json", "r") as file:
        dictionary = json.load(file)

    to_json1 = vars(ticket)
    to_json2 = vars(customer)
    dictionary[ticket.id] = to_json1
    dictionary[ticket.id]["_customer"] = to_json2

    with open("data.json", "w") as file:
        json.dump(dictionary, file, indent = 4)

    return ticket.__str__()


def find(id):
    if not isinstance(id, str):
        raise TypeError("Wrong type")
    with open("data.json", "r") as file:
        dictionary = json.load(file)
        if not id in dictionary.keys():
            raise ValueError("Ticket not found")
        else:
            customer = Customer(dictionary[id]["_customer"]["_name"], dictionary[id]["_customer"]["_surname"], dictionary[id]["_customer"]["_phone"], dictionary[id]["_customer"]["_is_student"])
            event = ITEvent(dictionary[id]["_event"]["_date"], dictionary[id]["_event"]["_desc"], dictionary[id]["_event"]["_price"])

            if dictionary[id]["_type"] == "regular":
                ticket = Regular(event, dictionary[id]["_date"])

            elif dictionary[id]["_type"] == "student":
                ticket = Student(event, dictionary[id]["_date"])

            elif dictionary[id]["_type"] == "advance":
                ticket = Advance(event, dictionary[id]["_date"])

            else:
                ticket = Late(event, dictionary[id]["_date"])

    return f'Customer: {customer.__str__()}\n{ticket.__str__()}'



def main():
    event = ITEvent("31/12/2021", "KPI-Open", 350)

    customer1 = Customer("Vasiliy", "Pavliuk", "380639746908", True)
    customer2 = Customer("Diana", "Nechyporuk", "380639746909", True)
    customer3 = Customer("Irina", "Kozhuhovska", "380639746902", False)

    ticket1 = order(event, customer1, "5/9/2021")
    ticket2 = order(event, customer2, "5/12/2021")
    ticket3 = order(event, customer3, "30/12/2021")
    ticket4 = order(event, customer3, "5/11/2021")
    
    ticket5 = find("0")
    print(ticket5)
                                # Customer: Vasiliy Pavliuk 380639746908
                                # Event: KPI-Open
                                # Date of event: 31/12/2021
                                # Order date: 5/9/2021
                                # Type of ticket: student
                                # Price: 175.0$

main()