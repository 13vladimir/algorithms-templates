# G. Стек - MaxEffective
# ID посылки:

from typing import List, Tuple


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(item)
        if len(self.max_items) == 0:
            return self.max_items.append(item)
        if item > self.max_items[-1]:
            max_item = item
        else:
            max_item = self.max_items[-1]
        self.max_items.append(max_item)

    def pop(self):
        if self.items:
            self.items.pop()
            self.max_items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(self.max_items[-1])
        else:
            print('None')


def commands(command):
    stack = StackMaxEffective()
    for i in command:
        if i[0] == 'push':
            stack.push(int(i[1]))
        if i[0] == 'pop':
            stack.pop()
        if i[0] == 'get_max':
            stack.get_max()


def read_input() -> Tuple[List[str], int]:
    amount_command = int(input())
    command = [list(map(str, input().split())) for _ in range(amount_command)]
    return command


def main():
    command = read_input()
    commands(command)


if __name__ == '__main__':
    main()
