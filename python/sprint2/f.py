# F. Стек - Max
# ID посылки: 105145572

from typing import List, Tuple


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        print('error')

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print('None')


def commands(command):
    stack = StackMax()
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
