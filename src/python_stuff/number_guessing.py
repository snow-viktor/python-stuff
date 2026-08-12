from random import randint


def number_guessing():
    min = int(input("\nLower limit: "))
    max = int(input("Upper limit: "))
    print()

    answer = randint(min, max)
    record = 0

    while True:
        user = int(input(f"[{min}, {max}]: "))
        record += 1

        if user == answer:
            print("\nCORRECT!")
            print(f"You guessed {record} times.")
            break
        elif user < answer:
            min = user
        else:
            max = user

    play_again = input("\nContinue to the next round? (Y/n): ").strip().lower()
    if play_again in ["y", ""]:
        number_guessing()


def main() -> None:
    number_guessing()


if __name__ == "__main__":
    main()
