# A. Ближайший ноль
# ID посылки: 104360899

from typing import List, Tuple


def calculate_distance(dist: int, house_number: int) -> int:
    return 0 if house_number == 0 else dist + 1


def near_number(street_length: int, house_number: List[int]) -> List[int]:
    result = [float('inf')] * street_length
    dist = float('inf')

    for i in range(street_length):
        dist = calculate_distance(dist, house_number[i])
        result[i] = dist

    for i in range(street_length-1, -1, -1):
        dist = calculate_distance(dist, house_number[i])
        result[i] = min(result[i], dist)

    return result


def read_input() -> Tuple[List[int], int]:
    street_length = int(input())
    house_number = list(map(int, input().strip().split()))
    return street_length, house_number


def main():
    street_length, house_number = read_input()
    print(*near_number(street_length, house_number), sep=' ')


if __name__ == '__main__':
    main()
