# H. Большое число
# ID посылки: 106669526

from typing import List, Tuple


def comparator(number1: str, number2: str) -> bool:
    if int(number1 + number2) > int(number2 + number1):
        return True
    return False


def big_number(amount_numbers, numbers):
    for i in range(1, amount_numbers):
        item_to_insert = numbers[i]
        j = i
        while j > 0 and comparator(item_to_insert, numbers[j-1]):
            numbers[j] = numbers[j-1]
            j -= 1
        numbers[j] = item_to_insert


def read_input() -> Tuple[int, List[int]]:
    amount_numbers = int(input())
    numbers = input().strip().split()
    return amount_numbers, numbers


def main():
    amount_numbers, numbers = read_input()
    big_number(amount_numbers, numbers)
    print(*numbers, sep='')


if __name__ == '__main__':
    main()
