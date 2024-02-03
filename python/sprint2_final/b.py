# B. Калькулятор
# ID посылки: 106395512

from typing import List, Tuple
import operator

OPERATORS = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
        }


class NoItemsError(Exception):
    def __init__(self):
        raise IndexError('Stack is empty')


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise NoItemsError
        return self.items.pop()


def read_input() -> Tuple[List[int]]:
    expression = list(map(str, input().split()))
    return expression


def main():
    expression = read_input()
    stack = Stack()

    for operators in expression:
        if operators in OPERATORS:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.push(OPERATORS[operators](num1, num2))
        else:
            stack.push(int(operators))
    print(stack.pop())


if __name__ == '__main__':
    main()
