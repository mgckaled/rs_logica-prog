import random
import time


def display_intro() -> None:
    """
    Displays the introductory message for the magic trick.
    """
    print("=" * 50)
    print("🎩 Welcome to the Amazing Mind Reader!")
    print("Think of a number between 1 and 20 in your mind...")
    print("Don't tell me, just think about it...")
    print("=" * 50)
    time.sleep(3)


def perform_magic_trick() -> None:
    """
    Simulates the magic trick by pretending to guess the number.
    """
    print("\nLet me concentrate... 🔮")
    time.sleep(2)
    print("Reading your thoughts...")
    time.sleep(3)

    guessed_number = random.randint(1, 20)
    print(f"\n✨ I got it! You're thinking of the number **{guessed_number}**!")
    print("Am I right? Of course I am... It's magic! 🧙‍♂️")


def main() -> None:
    """
    Entry point of the program.
    """
    display_intro()
    input("When you're ready, press ENTER and I will read your mind... ")
    perform_magic_trick()


if __name__ == "__main__":
    main()
