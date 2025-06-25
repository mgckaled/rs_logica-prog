import random
import time

# Predefined color options with emojis and hex codes
COLOR_OPTIONS = [
    ("Red", "🔴", "#F00F0F"),
    ("Green", "🟢", "#217321"),
    ("Blue", "🔵", "#0000FF"),
    ("Yellow", "🟡", "#FFFF00"),
    ("Purple", "🟣", "#6006AF"),
    ("Orange", "🟠", "#E16506EC"),
    ("White", "⚪", "#FFFFFF"),
    ("Black", "⚫", "#000000"),
    ("Brown", "🟤", "#A52A2A"),
]


def display_intro() -> None:
    """
    Displays the introductory message for the color mind trick.
    """
    print("=" * 50)
    print("🎨 Welcome to the Amazing Color Mind Reader!")
    print("Think of a color in your mind... but don't tell me!")
    print("Make it something vivid... something bright...")
    print("=" * 50)
    input("Once you've picked a color, press ENTER to continue... ")


def build_suspense() -> None:
    """
    Creates a fun suspenseful sequence.
    """
    print("\nLet me focus on your aura...")
    time.sleep(2)
    input("Now imagine your color glowing in front of you... Press ENTER again...")
    print("Visualizing the wavelengths...")
    time.sleep(2)
    print("Analyzing chromatic energy...")
    time.sleep(2)


def reveal_color() -> None:
    """
    Randomly selects a color and displays it as the magical 'guess'.
    """
    name, emoji, hex_code = random.choice(COLOR_OPTIONS)
    print("\n✨ I've seen it clearly in my crystal ball!")
    time.sleep(1.5)
    print(f"You were thinking of... {emoji} **{name.upper()}** ({hex_code})!")
    print("Incredible, right? I *told* you it's magic! 🧙‍♂️")


def main() -> None:
    """
    Entry point for the program.
    """
    display_intro()
    build_suspense()
    reveal_color()


if __name__ == "__main__":
    main()
