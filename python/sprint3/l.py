# L. Два велосипеда
# ID посылки: 106581352

from typing import Tuple, List


def binarySearch(money, bike_cost, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if money[mid] >= bike_cost > money[mid - 1] or mid == 0:
        return mid + 1
    elif money[mid] >= bike_cost:
        return binarySearch(money, bike_cost, left, mid)
    else:
        return binarySearch(money, bike_cost, mid + 1, right)


def read_input() -> Tuple[int, List[int], int]:
    number_days = int(input())
    money = list(map(int, input().strip().split()))
    bike_cost = int(input())
    return number_days, money, bike_cost


def main():
    number_days, money, bike_cost = read_input()
    print(binarySearch(
        money, bike_cost, left=0, right=number_days), end=' '
    )
    print(binarySearch(
        money, bike_cost * 2, left=0, right=number_days), end=' '
    )


if __name__ == '__main__':
    main()
