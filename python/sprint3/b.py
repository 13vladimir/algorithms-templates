# B. Комбинации
# ID посылки: 106644725

LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def gen_binary(numbers: str, combination: str = ''):
    if not numbers:
        print(combination, end=' ')
        return
    for letter in LETTERS[numbers[0]]:
        combination += letter
        gen_binary(numbers[1:], combination)
        combination = combination[:-1]


def read_input() -> str:
    numbers = input()
    return numbers


def main():
    numbers = read_input()
    gen_binary(numbers)


if __name__ == '__main__':
    main()
