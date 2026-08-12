from math import factorial


# f(x) = x! - 2^x
def f(x: int) -> int:
    return factorial(x) - 2**x


# u(x) = f(x) - 10 • ⌊ ⅒ • f(x) ⌋
def u(x: int) -> int:
    return f(x) - 10 * (f(x) // 10)


def main() -> None:
    length = int(input("\nLength: "))
    seq = [str(u(i)) for i in range(7, 7 + length)]
    print("\nRoger says you are " + "".join(seq), end=".\n")


if __name__ == "__main__":
    main()
