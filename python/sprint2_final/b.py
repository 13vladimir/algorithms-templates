# B. Калькулятор
# ID посылки: 105954365

from typing import List, Tuple
import operator


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> int:
        return self.items.pop()


def read_input() -> Tuple[List[int]]:
    expression = list(map(str, input().split()))
    return expression


def main():
    expression = read_input()
    stack = Stack()
    operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
        }

    for i in expression:
        if i in operators:
            y = stack.pop()
            x = stack.pop()
            stack.push(operators[i](x, y))
        else:
            stack.push(int(i))
    print(stack.pop())


if __name__ == '__main__':
    main()
