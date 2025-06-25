def show_welcome() -> None:
    """
    Exibe uma introdução ao assistente.
    """
    print("=" * 60)
    print("🤖 Welcome to the Oracle of Programming")
    print("Ask about programming topics, and I shall enlighten you!")
    print("Examples: variables, functions, oop, recursion, decorators...")
    print("=" * 60)


def ask_user() -> str:
    """
    Solicita ao usuário um tema de programação.
    """
    return input("🔎 Ask me about a programming topic: ").strip().lower()


def respond_to_topic(topic: str) -> None:
    """
    Fornece uma resposta baseada no tema usando match-case.
    """
    print("\n📘 Oracle's Response:")

    match topic:
        case "variables":
            print("Variables store data values. In Python, no need to declare types explicitly. Example: `x = 42`.")
        case "functions":
            print("Functions are reusable blocks of code. Define them using `def`. They promote modularity and clarity.")
        case "oop" | "object-oriented programming":
            print("OOP is a paradigm using objects and classes. Core principles: encapsulation, inheritance, and polymorphism.")
        case "recursion":
            print("Recursion is when a function calls itself. It requires a base case and is powerful for tree-like structures.")
        case "decorators":
            print("Decorators wrap functions to extend behavior. They use the `@decorator_name` syntax above function defs.")
        case "lambda":
            print(
                "Lambdas are anonymous functions defined with `lambda` keyword. Example: `lambda x: x * 2`.")
        case "async":
            print("Async allows concurrent code with coroutines. Use `async def`, `await`, and event loops for I/O efficiency.")
        case "typing":
            print("Typing adds type hints to Python. Helps tooling and readability. Use `def add(x: int) -> int:` for example.")
        case _:
            print(
                "Hmm... I'm still learning about that topic. Try asking something else!")


def ask_continue() -> bool:
    """
    Pergunta ao usuário se ele quer continuar.
    """
    response = input(
        "\n🔁 Would you like to ask another question? (yes/no): ").strip().lower()
    return response in {"yes", "y", "sim", "s"}


def main() -> None:
    """
    Loop principal do programa.
    """
    show_welcome()

    while True:
        topic = ask_user()
        respond_to_topic(topic)

        if not ask_continue():
            print("\n👋 Farewell, curious mind. May your code be bug-free!")
            break


if __name__ == "__main__":
    main()
