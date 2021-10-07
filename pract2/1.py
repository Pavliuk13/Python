class Product:
    def __init__(self, price, desc, dimension):
        if not isinstance(price, float) or not isinstance(desc, str) or not isinstance(dimension, list):
            raise TypeError
        elif price <= 0 or not len(desc) or len(dimension) < 3 or len(dimension) > 3:
            raise ValueError
        else:
            for i in dimension:
                if not isinstance(i, float):
                    raise TypeError
                elif i <= 0:
                    raise ValueError
        self.__price = price
        self.__desc = desc
        self.__dimention = dimension

    def getPrice(self):
        return self.__price

    def getInfo(self):
        return f'Priсe: {self.__price}$, Description: {self.__desc}, Height: {self.__dimention[0]}cm, Width: {self.__dimention[1]}cm, Length: {self.__dimention[2]}cm'



class Client:
    def __init__(self, name, surname, patronymic, phone, age):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(patronymic, str) or not isinstance(phone, str) or not isinstance(age, int):
            raise TypeError
        elif not len(name) or not len(surname) or not len(patronymic) or not len(phone) or age < 18:
            raise ValueError
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
        self.__data[client] = []
        
    def addProduct(self, client, product):
        self.__data[client].append(product)

    def showDataBase(self):
        for key in self.__data:
            array = self.__data.get(key)
            print(key.getInfo())
            for value in array:
                print(value.getInfo())

    def fullPriceOfOrder(self, client):
        sum = 0
        array = self.__data[client]
        for i in array:
            sum += i.getPrice()
        return f'{client.getFullName()}: {sum}$'
    



if __name__ == "__main__":     
    try:
        client1 = Client("Vasyl", "Pavliuk", "Olexandrovich", "0639746908", 18)
        client2 = Client("Volodymyr", "Pavliuk", "Olexandrovich", "0639752563", 24)
        client3 = Client("Olexandr", "Pavliuk", "Mykolayovich", "063649752653", 45)
        
        prod1 = Product(100362.0, "Audi A5", [2920.24, 2004.01, 5609.77])
        prod2 = Product(150362.0, "Mercedes C class", [1920.24, 2500.01, 5679.77])
        prod3 = Product(10362.0, "Daewoo", [920.24, 2030.01, 5689.77])
        prod4 = Product(130362.0, "Tesla", [1920.24, 2000.01, 5699.77])
        prod5 = Product(130362.5, "Wolkswagen", [3920.24, 1000.01, 5679.77])

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
        print(order.fullPriceOfOrder(client1)) # Pavliuk Vasyl Olexandrovich: 230724.5$
        print(order.fullPriceOfOrder(client2)) # Pavliuk Volodymyr Olexandrovich: 280724.0$
        print(order.fullPriceOfOrder(client3)) # Pavliuk Olexandr Mykolayovich: 10362.0$
        # show all orders
        order.showDataBase()
                            # Client Pavliuk Vasyl Olexandrovich
                            # Age: 18, Phone: 0639746908
                            # Prise: 100362.0$, Description: Audi A5, Height: 2920.24cm, Width: 2004.01cm, Length: 5609.77cm
                            # Prise: 130362.5$, Description: Wolkswagen, Height: 3920.24cm, Width: 1000.01cm, Length: 5679.77cm
                            # Client Pavliuk Volodymyr Olexandrovich
                            # Age: 24, Phone: 0639752563
                            # Prise: 150362.0$, Description: Mercedes C class, Height: 1920.24cm, Width: 2500.01cm, Length: 5679.77cm
                            # Prise: 130362.0$, Description: Tesla, Height: 1920.24cm, Width: 2000.01cm, Length: 5699.77cm
                            # Client Pavliuk Olexandr Mykolayovich
                            # Age: 45, Phone: 063649752653
                            # Prise: 10362.0$, Description: Daewoo, Height: 920.24cm, Width: 2030.01cm, Length: 5689.77cm
    except:
        print("Error!") 


    