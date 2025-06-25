def get_user_info() -> dict:
    """
    Coleta dados do usuário para o crachá.
    """
    print("=" * 50)
    print("🎟️  Welcome to the Tech Conference Badge Generator!")
    print("Fill in your details below:")
    print("=" * 50)

    name = input("🧑 Name: ").strip().title()
    age = input("📅 Age: ").strip()
    language = input("💻 Favorite Programming Language: ").strip().title()
    emoji = input("🌟 Emoji that represents you: ").strip()

    return {
        "name": name or "Anonymous",
        "age": age or "N/A",
        "language": language or "Python",
        "emoji": emoji or "*"
    }


def fixed_field(label: str, value: str, width: int = 36) -> str:
    """
    Formata uma linha com o rótulo e o valor, alinhados e truncados.
    """
    line = f"{label}: {value}"
    return line[:width].ljust(width)


def display_badge(data: dict) -> None:
    """
    Exibe um crachá terminal com alinhamento correto.
    """
    width = 40
    border = "+" + "-" * (width - 2) + "+"

    print("\n" + border)
    print("|" + "💡 TECH CONFERENCE 2025".center(width - 3) + "|")
    print("|" + "Developer Access Badge".center(width - 2) + "|")
    print(border)
    print("| " + fixed_field("Name", data['name']) + " |")
    print("| " + fixed_field("Age", data['age']) + " |")
    print("| " + fixed_field("Language", data['language']) + " |")
    print("| " + fixed_field("Identity", data['emoji']) + " |")
    print(border)
    print("| " + "Access Level: 🟢 Full Pass".ljust(width - 3) + " |")
    print(border)


def main() -> None:
    user_data = get_user_info()
    display_badge(user_data)


if __name__ == "__main__":
    main()
