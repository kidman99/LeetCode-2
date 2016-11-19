class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        temp_queue = [x]
        while len(self.stack) > 0:
            temp_queue.insert(0, self.stack.pop())
        while len(temp_queue) > 0:
            self.stack.insert(0, temp_queue.pop())
            

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0