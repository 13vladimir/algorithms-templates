# A. Поиск в сломанном массиве
# ID посылки: 107046150

from typing import List, Tuple


def broken_search(nums: list, target: int, array_len: int) -> int:
    start_index = 0
    end_index = array_len - 1

    while start_index <= end_index:
        mid_index = start_index + ((end_index - start_index) >> 1)

        if nums[mid_index] == target:
            return mid_index

        if nums[start_index] <= nums[mid_index]:
            if nums[start_index] <= target < nums[mid_index]:
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1
        else:
            if nums[mid_index] < target <= nums[end_index]:
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1
    return -1


def read_input() -> Tuple[int, int, List[int]]:
    array_len = int(input())
    target = int(input())
    array = list(map(int, input().strip().split()))
    return array_len, target, array


def main():
    array_len, target, array = read_input()
    print(broken_search(array, target, array_len))


if __name__ == '__main__':
    main()
