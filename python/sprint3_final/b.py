# B. Эффективная быстрая сортировка
# ID посылки: 107630650

from typing import List


def quicksort(username: list, start: int, end: int) -> list:
    if start >= end:
        return username
    i, j = start, end
    pivot = username[(start + end) // 2]
    while i <= j:
        while username[i] < pivot:
            i += 1
        while username[j] > pivot:
            j -= 1
        if i <= j:
            username[i], username[j] = username[j], username[i]
            i, j = i + 1, j - 1
    quicksort(username, start, j)
    quicksort(username, i, end)
    return username


def info_participants_sort(login: str, score_task: int, penalty: int) -> tuple:
    return -int(score_task), int(penalty), str(login)


def read_input() -> List[str]:
    number_participants = int(input())
    info_participants = (list(info_participants_sort(*input().split())
                              for _ in range(number_participants)))
    return info_participants


def main():
    info_participants = read_input()
    quicksort(info_participants, 0, len(info_participants) - 1)
    print(*(login for _, _, login in info_participants), sep='\n')


if __name__ == '__main__':
    main()
