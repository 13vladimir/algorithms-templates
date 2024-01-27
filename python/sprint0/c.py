# C. Скользящее среднее
# ID посылки: 103686579

from typing import List, Tuple


def moving_average(arr: List[int], window_size: int, n: int) -> List[float]:
    result = []
    current_sum = sum(arr[0:window_size])
    result.append(current_sum / window_size)
    for i in range(0, n - window_size):
        current_sum -= arr[i]
        current_sum += arr[i + window_size]
        current_avg = current_sum / window_size
        result.append(current_avg)
    return result


def read_input() -> Tuple[int, List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return n, arr, window_size


n, arr, window_size = read_input()
print(' '.join(map(str, moving_average(arr, window_size, n))))
