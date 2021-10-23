class Node:
    def __init__(self, code = None, price = None):
        if not isinstance(code, int) or not isinstance(price, float):
            raise TypeError("Wrong type of variables")
        elif code < 0 or price <= 0:
            raise ValueError("Not correct data")
        self.code = code
        self.price = price
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, code, price):
        if not self.root:
            self.root = Node(code, price)
        else:
            self._insert(code, price, self.root)

    def _insert(self, code, price, cur_node):
        if code < cur_node.code:
            if not cur_node.left_child:
                cur_node.left_child = Node(code, price)
            else:
                return self._insert(code, price, cur_node.left_child)
        elif code > cur_node.code:
            if not cur_node.right_child:
                cur_node.right_child = Node(code, price)
            else:
                return self._insert(code, price, cur_node.right_child)

    def search(self, code, count):
        if not isinstance(code, int) or not isinstance(count, int):
            raise TypeError("Wrong type of variables")
        elif code < 0 or count <= 0:
            raise ValueError("Not correct data")

        if self.root:
            return self._search(code, count, self.root)
        else:
            return 0

    def _search(self, code, count, cur_node):
        if code == cur_node.code:
            return cur_node.price * count
        elif code < cur_node.code and cur_node.left_child:
            return self._search(code, count, cur_node.left_child)
        elif code > cur_node.code and cur_node.right_child:
            return self._search(code, count, cur_node.right_child)
        else:
            return 0

if __name__ == "__main__":
    try:
        tree = Tree()

        tree.insert(12, 50.5)
        tree.insert(89, 3.5)
        tree.insert(3, 5.5)
        tree.insert(13, 0.5)
        tree.insert(77, 16.5)
        tree.insert(8, 9.5)

        for i in range(0, 5):
            code = int(input("Code: "))
            count = int(input("Number of products: "))
            print(tree.search(code, count))
    except Exception as ex:
        print(ex)