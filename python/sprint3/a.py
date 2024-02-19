# A. Генератор скобок
# ID посылки: 106641789

LEFT_PARENTHESIS = '('
RIGHT_PARENTHESIS = ')'


def gen_binary(amount_psp: int,
               open_br: int = 0,
               close_br: int = 0,
               prefix: str = ''
               ) -> None:
    if amount_psp * 2 == len(prefix):
        print(prefix)
        return
    if open_br < amount_psp:
        gen_binary(amount_psp,
                   open_br + 1,
                   close_br,
                   prefix + LEFT_PARENTHESIS
                   )
    if close_br < open_br:
        gen_binary(amount_psp,
                   open_br,
                   close_br + 1,
                   prefix + RIGHT_PARENTHESIS
                   )


def read_input() -> int:
    amount_psp = int(input())
    return amount_psp


def main():
    amount_psp = read_input()
    gen_binary(amount_psp)


if __name__ == '__main__':
    main()
