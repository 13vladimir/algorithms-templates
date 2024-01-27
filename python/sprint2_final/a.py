# A. Дек
# ID посылки: 105951624

from typing import List, Tuple


class NoItemsError(Exception):
    def __init__(self):
        pass


class StackOverflowError(Exception):
    def __init__(self):
        pass


class Qeque:
    def __init__(self, max_size_deque: int):
        self.queue = [None] * max_size_deque
        self.max_n = max_size_deque
        self.head = 0
        self.tail = -1
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.max_n

    def push_front(self, x: int) -> None:
        if self.is_full():
            raise StackOverflowError
        self.head = (self.head - 1) % self.max_n
        self.queue[self.head] = x
        self.size += 1

    def push_back(self, x: int) -> None:
        if self.is_full():
            raise StackOverflowError
        self.tail = (self.tail + 1) % self.max_n
        self.queue[self.tail] = x
        self.size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise NoItemsError
        x = self.queue[self.head]
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self) -> int:
        if self.is_empty():
            raise NoItemsError
        x = self.queue[self.tail]
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x


def read_input() -> Tuple[int, int, List[int]]:
    amount_commands = int(input())
    max_size_deque = int(input())
    command = [list(map(str, input().split())) for _ in range(amount_commands)]
    return max_size_deque, command


def main():
    max_size_deque, command = read_input()
    queue = Qeque(max_size_deque)
    for i in command:
        try:
            if i[0] == 'push_front':
                queue.push_front(int(i[1]))
            if i[0] == 'push_back':
                queue.push_back(int(i[1]))
            if i[0] == 'pop_front':
                print(queue.pop_front())
            if i[0] == 'pop_back':
                print(queue.pop_back())

        except (NoItemsError, StackOverflowError):
            print('error')


if __name__ == '__main__':
    main()
