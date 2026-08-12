def runway_number(angle: int | str) -> str:
    """
    Convert a magnetic heading angle to a standard runway number.

    >>> runway_number(0)
    "36"
    >>> runway_number(45)
    "05"
    >>> runway_number("270°")
    "27"
    """

    if isinstance(angle, str):
        angle = int(angle.rstrip("°"))

    result = (angle % 360 + 5) // 10

    return f"{result:02d}" if result != 0 else "36"


def main() -> None:
    angle = input("\nAngle: ")
    print(f"\nRunway number: {runway_number(angle)}")


if __name__ == "__main__":
    main()
