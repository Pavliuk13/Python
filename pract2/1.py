import re



class Product:
    def __init__(self, price, desc, dimension):
        if not isinstance(price, float) or not isinstance(desc, str) or not isinstance(dimension, list):
            raise TypeError("Wrong type of variables")
        if price <= 0 or not len(desc) or not (0 < len(dimension) <= 3) or not all(isinstance(x, int) and x > 0 for x in dimension):
            raise ValueError("Not correct data")
        self.__price = price
        self.__desc = desc
        self.__dimension = dimension

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, float):
            raise TypeError("Wrong type of variable")
        if price < 0:
            raise ValueError("Price can't be less then 0")
        self.__price = price

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, desc):
        if not isinstance(desc, str):
            raise TypeError("Wrong type of variable")
        if not len(desc):
            raise ValueError("Description can't be empty")
        self.__desc = desc

    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension):
        if not isinstance(dimension, list):
            raise TypeError("Wrong type of variable")
        if not (0 < len(dimension) <= 3) or not all(isinstance(x, int) and x > 0 for x in dimension):
            raise ValueError("Wrong dimention")



class Client:
    def __init__(self, surname, name, patronymic, phone):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(patronymic, str) or not isinstance(phone, str):
            raise TypeError("Wrong type of variables")
        if not len(name) or not len(surname) or not len(patronymic) or not len(phone) or not re.match(r'380[0-9]{9}', phone):
            raise ValueError("Not correct data")
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__phone = phone

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Wrong type of variable")
        if not len(surname):
            raise ValueError("Surname can't be empty")
        self.__surname = surname

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong type of variable")
        if not len(name):
            raise ValueError("Name can't be empty")
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("Wrong type of variable")
        if not len(patronymic):
            raise ValueError("Patronymic can't be empty")
        self.__patronymic = patronymic

    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Wrong type of variable")
        if not len(phone) or not re.match(r'380[0-9]{9}', phone):
            raise ValueError("Wrong phone number format")
        self.__phone = phone

    def __str__(self):
        return f'Full name: {self.__name} {self.__surname} {self.__patronymic}. Phone: {self.phone}'
        

class Order:
    def __init__(self, client, products):
        if not isinstance(client, Client) or not isinstance(products, list) or not all(isinstance(x, Product) for x in products):
            raise TypeError("Wrong type of arguments")
        if not len(products):
            raise ValueError("List of products can't be empty")
        self.__client = client
        self.__products = products

    def __full_price(self):
        sum = 0
        for prod in self.__products:
            sum += prod.price
        return sum

    def __str__(self):
        return f'{self.__client}. Total price: {round(self.__full_price(), 2)}'




if __name__ == "__main__":     
    try:
        client1 = Client("Pavliuk", "Vasyl", "Olexandrovich", "380639746908")
        client2 = Client("Pavliuk", "Volodymyr", "Olexandrovich", "380639746908")

        product1 = Product(200.1, "Product 1", [12, 10, 15])
        product2 = Product(300.1, "Product 2", [12, 10, 15])
        product3 = Product(400.1, "Product 3", [12, 10, 15])
        product4 = Product(500.1, "Product 4", [12, 10, 15])

        order1 = Order(client1, [product1, product2])
        order2 = Order(client2, [product3, product4])
        print(order1)
        print(order2)
    except Exception as ex:
        print(ex) 