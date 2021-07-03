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

    def peek_left(self):
        return self.container[0]

    def length(self):
        return len(self.container)


def is_balanced(string):
    stack = Stack()

    if len(string) < 2:
        return False

    if string[0] in ['}', ']', ')']:
        return False
    for ch in string:
        # Staking if the Element is Opening Bracket
        if ch in ['{', '[', '(']:
            stack.push(ch)

        # If the character is closing bracket, then Popping if uppermost stacked element is a Opening Bracket
        # And if next item is closing bracket

        if ch == ')' or ch == '}' or ch == ']':
            if stack.is_empty():
                return False

            if stack.peek() == '{' and ch == '}':
                stack.pop()

            elif stack.peek() == '[' and ch == ']':
                stack.pop()

            elif stack.peek() == '(' and ch == ')':
                stack.pop()

    if stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    print('1', is_balanced("))((a+b}{"))
    print('2', is_balanced("({a+b})"))
    print('3', is_balanced("))((a+b}{"))
    print('4', is_balanced("((a+b))"))
    print('5', is_balanced("))"))
    print('6', is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    print('7', is_balanced(''))
    print('8', is_balanced('['))
