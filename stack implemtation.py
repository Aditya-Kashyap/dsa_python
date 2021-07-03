from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False

    def length(self):
        return len(self.container)


if __name__ == '__main__':
    stack = Stack()
    stack.push("Hello")
    stack.push("this")
    stack.push("is")
    stack.push("stack")
    stack.push("implementation")

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.length())
    print(stack.pop())
    print(stack.is_empty())
