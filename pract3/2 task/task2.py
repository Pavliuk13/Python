import json
import uuid
from constants import DAYS, ADDITIONAL_INGREDIENTS

class Pizza:
    """The main class that describes pizza"""
    def __init__(self, name, add_ingredients):
        if not isinstance(add_ingredients, list):
            raise TypeError("Wrong type of additional ingredients")
        if not all(i in ADDITIONAL_INGREDIENTS for i in add_ingredients):
            raise ValueError("Wrong ingredient")
        self._name = name
        with open("pizzas.json", "r") as file:
            data = json.load(file)
        self._price = data[name]["price"]
        self._ingredients = data[name]["ingredients"]
        self._add_ingredients = add_ingredients
    
    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def ingredients(self):
        return self._ingredients

    def __str__(self) -> str:
        return f'Pizza: {self.name}\nPrice: {self.price}\nIngredients: {", ".join(self.ingredients + self._add_ingredients)}.'

class Monday(Pizza):
    """Pizza class on Monday"""
    def __init__(self, add_ingredients = []):
        super().__init__("Margherita", add_ingredients)
        self._day = "Monday"

class Tuesday(Pizza):
    """Pizza class on Tuesday"""
    def __init__(self, add_ingredients = []):
        super().__init__("Cheese", add_ingredients)
        self._day = "Tuesday"

class Wednesday(Pizza):
    """Pizza class on Wednesday"""
    def __init__(self, add_ingredients = []):
        super().__init__("Veggie", add_ingredients)
        self._day = "Wednesday"

class Thursaday(Pizza):
    """Pizza class on Thursaday"""
    def __init__(self, add_ingredients = []):
        super().__init__("Pepperoni", add_ingredients)
        self._day = "Thursday"

class Friday(Pizza):
    """Pizza class on Friday"""
    def __init__(self, add_ingredients = []):
        super().__init__("Meat", add_ingredients)
        self._day = "Friday"

class Saturday(Pizza):
    """Pizza class on Saturday"""
    def __init__(self, add_ingredients = []):
        super().__init__("Hawaiian", add_ingredients)
        self._day = "Saturday"

class Sunday(Pizza):
    """Pizza class on Sunday"""
    def __init__(self, add_ingredients = []):
        super().__init__("Buffalo", add_ingredients)
        self._day = "Sunday"
    


def order(day, count, add_ingredients):
    """The function that places an order"""
    if not isinstance(day, str) or not isinstance(count, int):
        raise TypeError("Wrong type of variables")
    if not (day in DAYS) or count <= 0:
        raise ValueError("Wrong value")
    
    index = DAYS.index(day)

    pizza = create_obj(index, add_ingredients)
    
    with open("order.json", "r") as file:
        data = json.load(file)

    id_of_order = str(uuid.uuid1())
    dictionary = vars(pizza)
    data[id_of_order] = dictionary
    data[id_of_order]["count"] = count
    data[id_of_order]["price"] = pizza.price * count

    with open("order.json", "w") as file:
        json.dump(data, file, indent = 4)

    return f'Id of order: {id_of_order}:\n{pizza.__str__()}\nCount: {count}\nTotal price: {pizza.price * count}'

def find(id_of_order):
    """Function that finds the order by id"""
    if not isinstance(id_of_order, str):
        raise TypeError("Wrong type of id")
    
    with open("order.json", "r") as file:
        data = json.load(file)

    if not data.get(id_of_order):
        raise KeyError("Wrong id of order")
    
    dictionary = data[id_of_order]
    index = DAYS.index(dictionary["_day"])

    pizza = create_obj(index, dictionary["_add_ingredients"])
    
    return f'Id of order: {id_of_order}:\n{pizza.__str__()}\nCount: {dictionary["count"]}\nTotal price: {pizza.price * dictionary["count"]}'


def create_obj(index, add_ingredients):
    """A function that creates a class object depending on the day of the week"""
    if not isinstance(index, int):
        raise TypeError("Wrong type of index")
    if not 0 <= index <= 6:
        raise ValueError("Wrong index")

    pizza = None
    match index:
        case 0:
            pizza = Monday(add_ingredients)
        case 1:
            pizza = Tuesday(add_ingredients)
        case 2:
            pizza = Wednesday(add_ingredients)
        case 3:
            pizza = Thursaday(add_ingredients)
        case 4:
            pizza = Friday(add_ingredients)
        case 5:
            pizza = Saturday(add_ingredients)
        case 6:
            pizza = Sunday(add_ingredients)

    return pizza



def main():
    add_ingredients = {1: "pineapple",
                       2: "turkey", 
                       3: "olives", 
                       4: "chili pepper", 
                       5: "mushrooms", 
                       6: "corn"}

    order1 = order("Monday", 5, [add_ingredients[1], add_ingredients[6]])
    print(order1)

    print()

    order2 = order("Sunday", 21, [add_ingredients[5], add_ingredients[4], add_ingredients[3]])
    print(order2)

                    # Id of order: 8ebca47e-47bf-11ec-bed9-74d02b736a48:
                    # Pizza: Margherita
                    # Price: 100
                    # Ingredients: tomatoes, cheese, basil, pineapple, corn.
                    # Count: 5
                    # Total price: 500

                    # Id of order: 8ebe77bb-47bf-11ec-a3be-74d02b736a48:
                    # Pizza: Buffalo
                    # Price: 199
                    # Ingredients: hot sauce, garlic powder, chicken, mozzarella, blue cheese, red onion, green onions, mushrooms, chili pepper, olives.
                    # Count: 21
                    # Total price: 4179

    order2 = find("8ebca47e-47bf-11ec-bed9-74d02b736a48")
    print(order2)

                    # Id of order: 8ebca47e-47bf-11ec-bed9-74d02b736a48:
                    # Pizza: Margherita
                    # Price: 100
                    # Ingredients: tomatoes, cheese, basil, pineapple, corn.
                    # Count: 5
                    # Total price: 500

main()