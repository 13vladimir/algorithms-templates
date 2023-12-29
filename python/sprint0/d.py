from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int, n: int) -> Optional[
    Tuple[int, int]
]:
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target_sum:
                return arr[i], arr[j]


def read_input() -> Tuple[int, List[int], int]:
    n = 6
    arr = [-1, -1, -9, -7, 3, -6]
    target_sum = 2
    return n, arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(' '.join(map(str, result)))


n, arr, target_sum = read_input()
print_result(two_sum(arr, target_sum, n))
