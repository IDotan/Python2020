import pytest


class Node:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None
        self.count = 0

    def get_data(self):
        return self.root

    def balance(self, data):
        if self.left is not None:
            if self.left.get_data() < data < self.get_data():
                temp = Node(data)
                temp.left = self.left
                self.left = None
                temp.right = self
                return temp, True
        if self.right is not None:
            if self.get_data() < data < self.right.get_data():
                temp = Node(data)
                temp.right = self.right
                self.right = None
                temp.left = self
                return temp, True
        return self, False

    def is_exist(self, value):
        if self.get_data() == value:
            return True
        if value < self.get_data():
            if self.left is not None:
                return self.left.is_exist(value)
        else:
            if self.right is not None:
                return self.right.is_exist(value)
        return False

    def add_node(self, data, exist_check=False):
        if exist_check is False and self.is_exist(data):
            return print(f"Cant add the value {data}, as its already in the system")
        exist_check = True
        if data < self.get_data():
            if not self.left:
                self.left = Node(data)
                self.count += 1
                return
            else:
                self.count += 1
                self.left.add_node(data, exist_check)
        elif data > self.get_data():
            if not self.right:
                self.right = Node(data)
                self.count += 1
                return
            else:
                self.count += 1
                self.right.add_node(data, exist_check)
        else:
            return False

    def print_tree(self, first=True):
        global temp_string
        if first:
            temp_string = ""
        if self.left is not None:
            self.left.print_tree(False)
        temp_string += str(self.get_data()) + ","
        if self.right is not None:
            self.right.print_tree(False)
        return temp_string

    def __str__(self):
        return self.print_tree()[slice(-1)]


root = Node(10)
root.add_node(6)
root.add_node(7)
root.add_node(7)
root.add_node(5)
root.add_node(4)
root.add_node(3)
root.add_node(1)
root.add_node(2)
root.add_node(11)
root.add_node(40)
root.add_node(40)
root.add_node(32)
root.add_node(47)
print(root)
print(str(root.get_data()))


def test_print():
    root = Node(10)
    root.add_node(6)
    root.add_node(7)
    root.add_node(7)
    root.add_node(5)
    root.add_node(4)
    root.add_node(3)
    root.add_node(1)
    root.add_node(2)
    root.add_node(11)
    root.add_node(40)
    root.add_node(40)
    root.add_node(32)
    root.add_node(47)
    assert str(root) == '1,2,3,4,5,6,7,10,11,32,40,47'
    assert str(root.get_data()) == '10'
