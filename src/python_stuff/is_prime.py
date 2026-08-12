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

    # Only 6k±1 need checking.
    #
    # n = a×b (1<a≤b)
    # a^2 ≤ ab
    # a ≤ √n
    # A composite number always has a factor ≤ √n, so checking up to i*i ≤ n is sufficient.
    #
    # For n < 25 this loop doesn't run: the numbers surviving the checks above
    # (5, 7, 11, 13, 17, 19, 23) are all prime, and 25 = 5×5 is the first
    # composite not divisible by 2 or 3, exactly where the loop kicks in.
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
