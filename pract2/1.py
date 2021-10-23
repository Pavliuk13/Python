class Product:
    def __init__(self, price, desc, dimension):
        if not isinstance(price, float) or not isinstance(desc, str) or not isinstance(dimension, list):
            raise TypeError("Wrong type of variables")
        elif price <= 0 or not len(desc) or len(dimension) < 3 or len(dimension) > 3 or not all(isinstance(x, float) and x > 0 for x in dimension):
            raise ValueError("Not correct data")
        self.__price = price
        self.__desc = desc
        self.__dimention = dimension

    def getPrice(self):
        return self.__price

    def getInfo(self):
        return f'Priсe: {self.__price}$, Description: {self.__desc}, Height: {self.__dimention[0]}mm, Width: {self.__dimention[1]}mm, Length: {self.__dimention[2]}mm'



class Client:
    def __init__(self, surname, name, patronymic, phone, age):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(patronymic, str) or not isinstance(phone, str) or not isinstance(age, int):
            raise TypeError("Wrong type of variables")
        elif not len(name) or not len(surname) or not len(patronymic) or not len(phone) or age < 18:
            raise ValueError("Not correct data")
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__phone = phone
        self.__age = age
    def getFullName(self):
        return f'{self.__surname} {self.__name} {self.__patronymic}'

    def getInfo(self):
        return f'Client {self.getFullName()}\nAge: {self.__age}, Phone: {self.__phone}'
        

class Order:
    def __init__(self):
        self.__data = {}
    
    def newClient(self, client):
        if not isinstance(client, Client):
            raise TypeError("Wrong type of variables")
        self.__data[client] = []
        
    def addProduct(self, client, product):
        if not isinstance(client, Client) or not isinstance(product, Product):
            raise TypeError("Wrong type of variables")
        self.__data[client].append(product)

    def DataBase(self):
        data = ""
        for key in self.__data:
            array = self.__data.get(key)
            data += key.getInfo() + '\n'

            for value in array:
                data += value.getInfo() + '\n'
        return data

    def fullPriceOfOrder(self, client):
        sum = 0
        array = self.__data[client]
        for i in array:
            sum += i.getPrice()
        return f'{client.getFullName()}: {round(sum, 2)}$'
    



if __name__ == "__main__":     
    try:
        client1 = Client("Plisiuk", "Nazar", "Valentinovich", "986254563", 20)
        client2 = Client("Karpiuk", "Alina", "Olexandrivna", "986254563", 24)
        client3 = Client("Subitskiy", "Pavlo", "Romanovich", "986254563", 18)
        
        prod1 = Product(1.1, "Product 1", [1.0, 1.1, 1.2])
        prod2 = Product(2.2, "Product 2", [2.1, 2.2, 2.3])
        prod3 = Product(3.3, "Product 3", [3.1, 3.2, 3.3])
        prod4 = Product(4.4, "Product 4", [4.1, 4.2, 4.3])
        prod5 = Product(5.6, "Product 5", [5.1, 5.2, 5.3])

        order = Order()
        # initialize new customers in the order
        order.newClient(client1)
        order.newClient(client2)
        order.newClient(client3)
        # first customer order
        order.addProduct(client1, prod1)
        order.addProduct(client1, prod5)
        # second customer order
        order.addProduct(client2, prod2)
        order.addProduct(client2, prod4)
        # third customer order
        order.addProduct(client3, prod3)
        # full price of the order of the first customer
        print(order.fullPriceOfOrder(client1) + '\n') # Plisiuk Nazar Valentinovich: 6.7$
        print(order.fullPriceOfOrder(client2) + '\n') # Karpiuk Alina Olexandrivna: 6.6$
        print(order.fullPriceOfOrder(client3) + '\n') # Subitskiy Pavlo Romanovich: 3.3$
        # show all orders
        print(order.DataBase())
                                # Client Plisiuk Nazar Valentinovich
                                # Age: 20, Phone: 986254563
                                # Priсe: 1.1$, Description: Product 1, Height: 1.0mm, Width: 1.1mm, Length: 1.2mm
                                # Priсe: 5.6$, Description: Product 5, Height: 5.1mm, Width: 5.2mm, Length: 5.3mm
                                # Client Karpiuk Alina Olexandrivna
                                # Age: 24, Phone: 986254563
                                # Priсe: 2.2$, Description: Product 2, Height: 2.1mm, Width: 2.2mm, Length: 2.3mm
                                # Priсe: 4.4$, Description: Product 4, Height: 4.1mm, Width: 4.2mm, Length: 4.3mm
                                # Client Subitskiy Pavlo Romanovich
                                # Age: 18, Phone: 986254563
                                # Priсe: 3.3$, Description: Product 3, Height: 3.1mm, Width: 3.2mm, Length: 3.3mm
    except Exception as ex:
        print(ex) 