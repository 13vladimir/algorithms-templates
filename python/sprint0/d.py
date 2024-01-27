# D. Две фишки
# ID посылки: 103694247

from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int, n: int) -> Optional[
    Tuple[int, int]
]:
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target_sum:
                return arr[i], arr[j]


def read_input() -> Tuple[int, List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return n, arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(' '.join(map(str, result)))


n, arr, target_sum = read_input()
print_result(two_sum(arr, target_sum, n))
