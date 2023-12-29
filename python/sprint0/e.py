from typing import List, Tuple, Optional


def twosum_with_sort(arr: List[int], target_sum: int, n: int) -> Optional[
    Tuple[int, int]
]:
    arr.sort()
    left = 0
    right = n - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return arr[left], arr[right]
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1


# def twosum_extra_ds(arr: List[int], target_sum: int) -> Optional[
#     Tuple[int, int]
# ]:
#     previous = set()
#    for A in arr:
#        Y = target_sum - A
#        if Y in previous:
#            return A, Y
#        else:
#           previous.add(A)


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
print_result(twosum_with_sort(arr, target_sum, n))
# print_result(twosum_extra_ds(arr, target_sum))
