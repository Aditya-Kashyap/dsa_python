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

    def peek_left(self):
        return self.container[0]

    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False

    def length(self):
        return len(self.container)


def reverse(string):

    if len(string) < 2:
        return string

    char = Stack()
    for i in range(len(string)):
        char.push(string[i])

    print(char.peek_left())

    rev_str = ''
    for ch in range(char.length()):
        rev_str += char.pop()

    return rev_str


if __name__ == '__main__':
    reverse_str = reverse("I am the King")
    print(reverse_str)
