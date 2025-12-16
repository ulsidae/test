def print_cat_normal():
    print(" /\\_/\\")
    print("(=^.^=)")


def print_cat_win():
    print(" /\\_/\\")
    print("(=^.^=)!!")


def print_cat_suspicious():
    print(" /\\_/\\")
    print("(=・ω・=)?")


def print_cat_lose():
    print(" /\\_/\\")
    print("(=・_・=)")


def main():
    print_cat_normal()
    print("Fair Binary Search Duel Begins!\n")

    print("Think of a number between 1 and 100. Keep it in your mind; don't change it.\n")
    print("When I guess, just answer with:")
    print('"correct" if my guess matches your number,')
    print('"down"    if your number is smaller,')
    print('"up"      if your number is bigger.\n')

    low = 1
    high = 100
    max_attempts = 10 # <- actually you can't win in this situation. So, if you want "winnable" game, change max_attempts at least 6
    attempts = 0

    while True:
        if low > high:
            print()
            print_cat_suspicious()
            print("Your answers lead to an impossible situation...")
            print("Something doesn't add up, but you win this time.")
            break

        if attempts >= max_attempts:
            print()
            print_cat_lose()
            print("I couldn't find your number in time. You win!")
            break

        attempts += 1
        guess = (low + high) // 2

        print(f"Attempt {attempts} / {max_attempts}")
        print(f"Current range: [{low}, {high}]")
        print(f"My guess: {guess}")

        while True:
            response = input('Type "correct", "down", or "up": ').strip().lower()
            if response in ("correct", "down", "up"):
                break
            print("I only understand: correct / down / up. Try again.")

        if response == "correct":
            print()
            print_cat_win()
            print("I guessed your number in time. I win!")
            break
        elif response == "up":
            low = guess + 1
            print("Okay, higher than that.\n")
        elif response == "down":
            high = guess - 1
            print("Got it, lower than that.\n")


if __name__ == "__main__":
    main()
