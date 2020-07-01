class Stack:
    """
    >>> x = Stack()
    >>> x.is_empty()
    True
    >>> x.top()
    Traceback (most recent call last):
          File "<doctest itai8.Stack[2]>", line 1, in <module>
    IndexError: The Stack is empty
    >>> x.push(5)
    >>> x.top()
    5
    >>> x.is_empty()
    False
    >>> x.push("yay")
    >>> x.top()
    'yay'
    >>> y = Stack()
    >>> z = Stack()
    >>> z == y
    True
    >>> x == y
    False
    >>> y.push(5)
    >>> y.push("yay")
    >>> #y.push(3)
    >>> x == y
    True
    >>> z = x + y
    >>> print(z)
    [5, 'yay', 5, 'yay']
    >>> z.pop()
    'yay'
    >>> z.top()
    5
    >>> x.pop()
    'yay'
    >>> print(x)
    [5]
    >>> y = Stack()
    >>> z = x + y
    >>> print(z)
    [5]
    >>> z = y + x
    >>> print(z)
    [5]
    >>> x.top()
    5
    >>> x.pop()
    5
    >>> x.pop()
    Traceback (most recent call last):
          File "<doctest itai8.Stack[2]>", line 1, in <module>
    IndexError: The Stack is empty
    >>> print(x)
    []
    >>> x.push(1)
    >>> x.push(2)
    >>> y.push(3)
    >>> z = x + y
    >>> print(z)
    [1, 2, 3]
    >>> g = y + x
    >>> print(g)
    [3, 1, 2]
    >>> z == g
    False
    """
    def __init__(self):
        """
        Create a new and empty list to be used
        """
        self.__stack = []

    def push(self, x):
        """
        | Add new item to the top of the stack
        :param x: The item to be added
        """
        self.__stack.append(x)

    def pop(self):
        """
        | Remove and return the last item when there is one
        :return: The last item in the stack if there is one
        """
        # make sure the stack is not empty
        if not self.is_empty():
            __temp = self.__stack.pop()
            return __temp
        else:
            # if its empty cant pop() and raise an error
            raise IndexError("The Stack is empty")

    def top(self):
        """
        | Return the item at the top of the stack
        :return: The last item in the stack
        """
        # make sure the stack is not empty
        if not self.is_empty():
            __x = (len(self.__stack) - 1)
            __temp = self.__stack[__x]
            return __temp
        else:
            # if its empty cant top() and raise an error
            raise IndexError("The Stack is empty")

    def is_empty(self):
        """
        | Check if the stack is empty
        :return: True when empty, False when not empty
        """
        return self.__stack == []

    def __add__(self, other):
        """
        | Add 2 list to a new one, one list at the end of the first list
        :param other: The list to add in the end
        :return: The new and combined list
        """
        __new = Stack()
        # go over and ad each item of the 1st stack
        for i in self.__stack:
            __new.push(i)
        # go over and ad each item of the 2nd stack
        for i in other.__stack:
            __new.push(i)
        return __new

    def __eq__(self, other):
        """
        | Check if the given stack are the same
        :param other: The stack to compare against
        :return: True when the stacks are the same, False if not
        """
        # check if only one of the stack is empty
        if self.is_empty() != other.is_empty():
            return False
        # check if the stacks length is not the same
        if len(self.__stack) != len(other.__stack):
            return False
        # go one by one to compare the items in the stack
        j = 0
        for i in self.__stack:
            if i != other.__stack[j]:
                return False
            j += 1
        # when every other check pass return True
        return True
        # return self.__stack == other.__stack (simple why using list build in)

    def __str__(self):
        return format(self.__stack)


def correct_brackets(this, other):
    """
    | Check if the brackets have the correct open and closed ones
    :param this: open brackets to check
    :param other: close brackets to check
    :return: True when the open and close brackets are correct. False when not
    """
    if this == "(" and other == ")":
        return True
    elif this == "{" and other == "}":
        return True
    elif this == "[" and other == "]":
        return True
    # when no brackets are a mach return False
    return False


def closer_bracket(closer, s):
    """
    | checks to run when a closer brackets where found
    :param closer: the found closer to check
    :param s: the stack of open brackets
    """
    opener_in_stack = s.top()
    # compare the opener in the stack to the found closer
    if correct_brackets(opener_in_stack, closer):
        # pop() the opener that was used already
        s.pop()
    else:
        raise IndexError


def end_expr(stack, brackets):
    """
    | At the end of the argument check ths status of the stack and if there where brackets used
    :param stack: the brackets stack
    :param brackets: bool. True if there where brackets in the expression.
    :return: string representing the expression status.
    """
    valid = True
    # check if any brackets where used
    if not brackets:
        print("Valid expression (There where no brackets in the expression)")
    # make sure the stack is empty for it to be valid
    elif not stack.is_empty():
        print("Not a valid expression")
        valid = False
    else:
        print("Valid expression")
    return valid


def validate_expr(expr):
    """
    | go over the given argument to make sure there is a valid use of brackets in it
    :rtype: object
    :param expr: the argument to be checked
    :return: print if Valid or not

    >>> validate_expr("(1+1)")
    Valid expression
    True
    >>> validate_expr("[1+1]")
    Valid expression
    True
    >>> validate_expr("{1+1}")
    Valid expression
    True
    >>> validate_expr("({[1+1]})")
    Valid expression
    True
    >>> validate_expr("(){}[]")
    Valid expression
    True
    >>> validate_expr("(1+1))")
    Not a valid expression
    False
    >>> validate_expr("(1+1)+[1+1)")
    Not a valid expression
    False
    >>> validate_expr("(1+1)+[1+1{")
    Not a valid expression
    False
    >>> validate_expr("()(()){}[])")
    Not a valid expression
    False
    >>> validate_expr("123456")
    Valid expression (There where no brackets in the expression)
    True
    >>> validate_expr("hello")
    Valid expression (There where no brackets in the expression)
    True
    >>> validate_expr("")
    Valid expression (empty expression)
    True
    """
    s = Stack()
    i = 0
    brackets = False
    if expr == "":
        print("Valid expression (empty expression)")
        return True
    # go over the expression one by one
    while i < (len(expr)):
        temp_char = (expr[slice(i, (i + 1))])
        # look for opener bracket
        if temp_char == "(" or temp_char == "{" or temp_char == "[":
            # add to the stack if its an opener bracket
            s.push(temp_char)
            brackets = True
        # look for closer bracket
        elif temp_char == ")" or temp_char == "}" or temp_char == "]":
            try:
                closer_bracket(temp_char, s)
            except IndexError:
                print("Not a valid expression")
                return False
                break
        # go in the if only at the end of the expression
        if i+1 == len(expr):
            # at the end of the expression do final checks and print
            valid = (end_expr(s, brackets))
            return valid
            break
        i += 1


if __name__ == "__main__":
    while True:
        expr = input("enter some expression with () [] {} etc.\n")
        validate_expr(expr)
        break
