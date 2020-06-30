class Queue:
    """
    | class of a queue
    """

    def __init__(self, maxsize):
        """
        | initialize the queue
        :param maxsize: the max size we want for the queue
        """
        self.data = []
        self.maxsize = maxsize

    def setMaxSize(self, value):
        """
        | set the max size of the queue
        :param value: the new max size to set
        """
        if value == self.maxsize:
            print(f"{value} is all ready the max size")
            return
        if len(self.data) > value:
            print("Can't set the max size to be smaller then the queue")
            return
        self.maxsize = value

    def checkCapcity(self):
        """
        | check how mach space is left in the queue
        :return: int of te left space
        """
        return self.maxsize - (len(self.data))

    def push(self, value):
        """
        | add new data to the end of the queue
        """
        if self.checkCapcity() != 0:
            self.data.append(value)
        else:
            print("The queue is full, can't add any more")

    def pop(self, value):
        """
        | pop the given value for the queue
        :param value: the value to pop
        """
        if self.isEmpty():
            print(f"Can't remove {value}, because the queue is empty")
            return

        for i in range(0, len(self.data)):
            if self.data[i] == value:
                self.data.pop(i)
                return
            i += 1
        print(f"The value {value} is not in the queue")

    def Empty(self):
        """
        | empty the queue
        """
        self.data = []

    def isEmpty(self):
        """
        | check if the queue is empty
        :return: True when the list is empty
        """
        if len(self.data) == 0:
            return True
        return False


def test_queue(capsys):
    qu = Queue(10)
    assert qu.isEmpty() is True
    qu.pop(10)
    captured = capsys.readouterr()
    assert captured.out == "Can't remove 10, because the queue is empty\n"
    qu.push(1)
    qu.push(2)
    qu.setMaxSize(1)
    captured = capsys.readouterr()
    assert captured.out == "Can't set the max size to be smaller then the queue\n"
    qu.setMaxSize(2)
    qu.setMaxSize(2)
    captured = capsys.readouterr()
    assert captured.out == "2 is all ready the max size\n"
    qu.push(3)
    captured = capsys.readouterr()
    assert captured.out == "The queue is full, can't add any more\n"
    qu.pop(3)
    captured = capsys.readouterr()
    assert captured.out == "The value 3 is not in the queue\n"
    qu.pop(2)
    qu.pop(2)
    captured = capsys.readouterr()
    assert captured.out == "The value 2 is not in the queue\n"
    assert qu.isEmpty() is False
    qu.Empty()
    assert qu.isEmpty() is True
