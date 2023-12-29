from typing import List, Tuple


def near_number(n: int, n_home: List[int]) -> List[int]:
    result = [float('inf')] * n
    dist = float('inf')

    for i in range(n):
        if n_home[i] == 0:
            dist = 0
        else:
            dist += 1
        result[i] = dist

    for i in range(n-1, -1, -1):
        if n_home[i] == 0:
            dist = 0
        else:
            dist += 1
        result[i] = min(result[i], dist)

    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    n_home = list(map(int, input().strip().split()))
    return n, n_home


def main():
    n, n_home = read_input()
    print(' '.join(map(str, near_number(n, n_home))))


if __name__ == '__main__':
    main()
