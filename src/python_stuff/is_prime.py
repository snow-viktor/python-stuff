def is_prime(n: int) -> bool:
    """
    Check if a positive integer is prime.
    """

    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    # Only 6k±1 can be prime; a composite always has a factor <= √n.
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def main() -> None:
    num = int(input("\nPrime? "))
    print(is_prime(num))


if __name__ == "__main__":
    main()
