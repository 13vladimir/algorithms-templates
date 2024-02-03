# A. Дек
# ID посылки: 106513262

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

    def calculate(self, value: int, delta: int) -> int:
        return (value + delta) % self.__max_size

    def push_front(self, value: int) -> None:
        if self.is_full():
            raise StackOverflowError
        self.__head = self.calculate(self.__head, -1)
        self.__queue[self.__head] = value
        self.__size += 1

    def push_back(self, value: int) -> None:
        if self.is_full():
            raise StackOverflowError
        self.__tail = self.calculate(self.__tail, 1)
        self.__queue[self.__tail] = value
        self.__size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise NoItemsError
        value = self.__queue[self.__head]
        self.__head = self.calculate(self.__head, 1)
        self.__size -= 1
        return value

    def pop_back(self) -> int:
        if self.is_empty():
            raise NoItemsError
        value = self.__queue[self.__tail]
        self.__tail = self.calculate(self.__tail, -1)
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
    for command, *arg in commands:
        try:
            result = getattr(queue, command)(*arg)
            if result is not None:
                print(result)
        except (NoItemsError, StackOverflowError):
            print('error')


if __name__ == '__main__':
    main()
