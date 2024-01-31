# A. Дек
# ID посылки: 106319745

from typing import List, Tuple


class NoItemsError(Exception):
    def __init__(self):
        pass


class StackOverflowError(Exception):
    def __init__(self):
        pass


class Queue:
    def __init__(self, max_size_deque: int):
        self.__queue = [None] * max_size_deque
        self.__max_size = max_size_deque
        self.__head = 0
        self.__tail = -1
        self.__size = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def is_full(self) -> bool:
        return self.__size == self.__max_size

    def calculation(self, operation: str):
        if operation == 'push_front':
            self.__head = (self.__head - 1) % self.__max_size
        elif operation == 'push_back':
            self.__tail = (self.__tail + 1) % self.__max_size
        elif operation == 'pop_front':
            self.__head = (self.__head + 1) % self.__max_size
        elif operation == 'pop_back':
            self.__tail = (self.__tail - 1) % self.__max_size
        else:
            raise ValueError('Invalid operation')

    def push_front(self, value: int) -> None:
        if self.is_full():
            raise StackOverflowError
        self.calculation('push_front')
        self.__queue[self.__head] = value
        self.__size += 1

    def push_back(self, value: int) -> None:
        if self.is_full():
            raise StackOverflowError
        self.calculation('push_back')
        self.__queue[self.__tail] = value
        self.__size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise NoItemsError
        value = self.__queue[self.__head]
        self.calculation('pop_front')
        self.__size -= 1
        return value

    def pop_back(self) -> int:
        if self.is_empty():
            raise NoItemsError
        value = self.__queue[self.__tail]
        self.calculation('pop_back')
        self.__size -= 1
        return value


def read_input() -> Tuple[int, int, List[int]]:
    amount_commands = int(input())
    max_size_deque = int(input())
    commands = [list(map(str, input().split()))
                for _ in range(amount_commands)]
    return max_size_deque, commands


def main():
    max_size_deque, commands = read_input()
    queue = Queue(max_size_deque)
    for command in commands:
        try:
            [print(getattr(queue, command[0])())
             if len(command) == 1 else getattr(queue, command[0])(command[1])]
        except (NoItemsError, StackOverflowError):
            print('error')


if __name__ == '__main__':
    main()
