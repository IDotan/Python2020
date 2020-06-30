"""
This is a binary tree for the INT collage test.
A binary tree is a data collection handler. The tree have a root, left branch and a right branch.
The root is the stating position of the given data node.
The left branch is the data smaller then the given root.
The right branch is the data bigger then the given root.
---
binary search use the fact the tree is already split in half and go over only the half we need.
the half we need is picked if the value to search is smaller then the root we go left other wise we go right.
"""

temp_string = ""


class Node:
    """
    | class of of the binary tree
    """
    def __init__(self, data):
        """
        | initialize new data root in the tree
        :param data: the data to create a root for
        """
        self.root = data
        self.left = None
        self.right = None

    def get_data(self):
        """
        | get the value of the root
        :return: the root value
        """
        return self.root

    def printTree(self):
        """
        | print the binary tree in multiple lines
        """
        if self.left:
            self.left.printTree()
        print(self.root)
        if self.right:
            self.right.printTree()

    def print_tree(self, first=True):
        """
        | print the tree in order in one line
        :param first: bool to see if this is the first call to the function. default True
        :return: string of the tree
        """
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

    def insert(self, data, is_exist=False):
        """
        | add new data to the binary tree
        :param data: the data to be added to the tree
        :param is_exist: bool if the data was checked to already been in the tree. default False
        """
        if is_exist is False and self.is_exist(data):
            return print(f"Can't add the value {data}, as its already in the tree.")
        is_exist = True
        if data < self.get_data():
            if not self.left:
                self.left = Node(data)
                return
            else:
                self.left.insert(data, is_exist)
        elif data > self.get_data():
            if not self.right:
                self.right = Node(data)
                return
            else:
                self.right.insert(data, is_exist)
        else:
            return False

    def is_exist(self, val):
        """
        | check if the given value is already in the tree
        :param val: the value to be checked in the tree
        :return: True when the value was already in the tree
        """
        if self.get_data() == val:
            return True
        if val < self.get_data():
            if self.left is not None:
                return self.left.is_exist(val)
        else:
            if self.right is not None:
                return self.right.is_exist(val)
        return False


def test_binary_tree():
    root = Node(10)
    assert root.is_exist(10)
    root.insert(4)
    assert root.is_exist(4)
    root.insert(11)
    assert root.is_exist(11)
    root.insert(3)
    assert root.is_exist(3)
    root.insert(770)
    assert root.is_exist(770)
    root.insert(523)
    assert root.is_exist(523)
    root.insert(43)
    assert root.is_exist(43)


def test_disabling_capturing(capsys):
    root2 = Node(10)
    root2.insert(10)
    captured = capsys.readouterr()
    assert captured.out == "Can't add the value 10, as its already in the tree.\n"
    root2.insert(30)
    root2.insert(20)
    root2.insert(20)
    captured = capsys.readouterr()
    assert captured.out == "Can't add the value 20, as its already in the tree.\n"
    print(root2)
    captured = capsys.readouterr()
    assert captured.out == "10,20,30\n"
    root2.printTree()
    captured = capsys.readouterr()
    assert captured.out == "10\n20\n30\n"
