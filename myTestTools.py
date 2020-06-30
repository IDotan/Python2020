import sys
from io import StringIO
"""
A collection of test tools for easy test-code creation
"""


class Test:
    """
    class to use for tests
    """

    def __init__(self, function, var):
        """
        create a Test item to be tested upon
        :param function: the function to run
        :param var: args to send to the function
        """
        self.__function = function
        self.__var = var

    def test_print(self):
        """
        | Call the function and making sure var is unpacked when needed
        """
        self.__function(*self.__var)


def print_test(*data):
    """
    | Tool to get a print as a value to be tested against.
    | the function is only the name with out the brackets:
    | function -- not function()
    | to send multi args to the function:
    | print_test(function, (a, b, c...) )


    :param data: (function, (*args)) function to test. (optional- *args to send)
    :return: string of the print.
    """
    function, *var = data
    stdout_ = sys.stdout  # Keep track of the previous value.
    stream = StringIO()
    sys.stdout = stream
    # create Test item to be called
    t = Test(function, var)
    # line to get the print of
    t.test_print()
    sys.stdout = stdout_  # restore the previous stdout.
    print_output = (stream.getvalue()).strip()  # This will get the string inside the variable and strip it
    return print_output
