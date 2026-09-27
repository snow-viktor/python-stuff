from itertools import cycle

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
_ALPHA_INDEX = {c: i for i, c in enumerate(ALPHABET)}


def caesar_cipher(text: str, offset: int) -> str:
    """
    >>> caesar_cipher("Python 3.14.7", 1)
    "Qzuipo 4.25.8"
    """

    OFFSET_MAP = {a: ALPHABET[(i + offset) % 26] for i, a in enumerate(ALPHABET)}
    OFFSET_MAP.update(
        {a.upper(): ALPHABET[(i + offset) % 26].upper() for i, a in enumerate(ALPHABET)}
    )
    OFFSET_MAP.update({d: DIGITS[(int(d) + offset) % 10] for d in DIGITS})

    return "".join(OFFSET_MAP.get(char, char) for char in text)


def vigenere_cipher(text: str, key: str) -> str:
    """
    >>> vigenere_cipher("Python 3.14.7", "key")
    "Pcrrsl 7.18.7"
    """

    def shift(char, offset):
        if char in _ALPHA_INDEX:
            return ALPHABET[(_ALPHA_INDEX[char] + offset) % 26]
        if char in DIGITS:
            return DIGITS[(int(char) + offset) % 10]
        return char

    shifts = (_ALPHA_INDEX[k] for k in cycle(key.lower()))
    return "".join(shift(char, offset) for char, offset in zip(text, shifts))


def main() -> None:
    method = input("\nChoose caesar or vigenere cipher (c/v): ").strip().lower()
    text = input("Enter text to encrypt: ")

    if method == "c":
        offset = int(input("Enter offset: "))
        print(f"\n{caesar_cipher(text, offset)}")
    elif method == "v":
        key = input("Enter key: ")
        print(f"\n{vigenere_cipher(text, key)}")
    else:
        print("Unknown cipher")


if __name__ == "__main__":
    main()
