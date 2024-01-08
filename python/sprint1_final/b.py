# B. Ловкость рук
# ID посылки: 104053878

from typing import List, Tuple


def points(keyboard: List[str], amount_buttons: int) -> int:
    points = 0
    count = [0] * 16
    amount_buttons = amount_buttons * 2

    for number in keyboard:
        if number != '.':
            count[int(number)] += 1

    for number in count:
        if 0 < number <= amount_buttons:
            points += 1

    return points


def read_input() -> Tuple[List[str], int]:
    amount_buttons = int(input())
    keyboard = [i for i in range(4) for i in input().strip()]
    return keyboard, amount_buttons


def main():
    keyboard, amount_buttons = read_input()
    print(points(keyboard, amount_buttons))


if __name__ == '__main__':
    main()
