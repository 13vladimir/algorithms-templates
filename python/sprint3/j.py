# J. Пузырек
# ID посылки: 106654881

from typing import List, Tuple


def bubble_sort(array_len: int, array: List[int]):
    printed = True
    for i in range(1, array_len):
        sorted = False
        for j in range(array_len-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                sorted = True
        if sorted:
            print(' '.join(map(str, array)))
            printed = False
    if printed:
        print(' '.join(map(str, array)))


def read_input() -> Tuple[int, List[int]]:
    array_len = int(input())
    array = list(map(int, input().strip().split()))
    return array_len, array


def main() -> None:
    array_len, array = read_input()
    bubble_sort(array_len, array)


if __name__ == '__main__':
    main()
