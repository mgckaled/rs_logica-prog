import random


def show_intro() -> None:
    """
    Exibe a introdução do jogo.
    """
    print("=" * 60)
    print("🎯 Welcome to the Secret Number Challenge!")
    print("Try to guess the secret number before attempts run out!")
    print("=" * 60)


def choose_difficulty() -> int:
    """
    Permite que o jogador escolha o modo de dificuldade.
    Retorna o maior número possível do intervalo.
    """
    print("\nChoose a difficulty level:")
    print("1 - Easy   (1 to 10)")
    print("2 - Medium (1 to 50)")
    print("3 - Hard   (1 to 100)")

    while True:
        choice = input("Select (1/2/3): ").strip()
        match choice:
            case "1":
                return 10
            case "2":
                return 50
            case "3":
                return 100
            case _:
                print("⚠️ Invalid option. Choose 1, 2 or 3.")


def get_player_guess(min_val: int, max_val: int) -> int:
    """
    Solicita um palpite dentro do intervalo válido.
    """
    while True:
        guess = input(
            f"🔢 Enter a number between {min_val} and {max_val}: ").strip()
        if guess.isdigit():
            guess_num = int(guess)
            if min_val <= guess_num <= max_val:
                return guess_num
        print("⚠️ Invalid input. Try again.")


def play_game(secret_number: int, max_val: int, max_attempts: int = 6) -> int:
    """
    Executa o jogo principal, limitando tentativas.
    """
    attempts = 0
    print(f"\n🕹️ You have {max_attempts} attempts. Good luck!")

    while attempts < max_attempts:
        guess = get_player_guess(1, max_val)
        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! The secret number was {secret_number}.")
            return attempts
        elif guess < secret_number:
            print("📈 Too low.")
        else:
            print("📉 Too high.")

        print(f"⏳ Attempts remaining: {max_attempts - attempts}")

    print(f"\n💥 You've run out of attempts. The number was {secret_number}.")
    return -1  # código especial para "não acertou"


def show_result(attempts: int) -> None:
    """
    Mostra resultado final do jogador.
    """
    print("\n" + "=" * 60)
    if attempts == -1:
        print("😵 Better luck next time!")
    else:
        print(f"🏆 You guessed it in {attempts} attempt(s)!")
        if attempts == 1:
            print("💥 First try! Incredible!")
        elif attempts <= 3:
            print("🔥 Excellent performance!")
        elif attempts <= 6:
            print("👍 Well done under pressure!")
    print("=" * 60)


def main() -> None:
    show_intro()
    max_val = choose_difficulty()
    secret_number = random.randint(1, max_val)
    attempts = play_game(secret_number, max_val)
    show_result(attempts)


if __name__ == "__main__":
    main()
