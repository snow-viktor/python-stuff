from random import sample


def password(length: int) -> str:
    """
    The password is ASCII characters and the maximum length of the password is 95 characters.
    """

    PASSWORD = sample(
        " !'\"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
        95,
    )
    return "".join(PASSWORD[:length])


def main() -> None:
    length = int(input("\nLength: "))
    print(f"Password:\n{password(length)}")


if __name__ == "__main__":
    main()
