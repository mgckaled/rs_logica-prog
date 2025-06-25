Question = list[str]


def get_questions() -> list[Question]:
    """
    Retorna a lista de perguntas e respostas.
    """
    return [
        ["What is the keyword to define a function in Python?", "def"],
        ["Which data type is used to store text?", "string"],
        ["What symbol is used to comment a single line in Python?", "#"],
        ["What is the result of 3 ** 2 in Python?", "9"],
        ["What data type is returned by the input() function?", "string"],
        ["Which keyword is used to create a loop that repeats while a condition is true?", "while"],
        ["What is the index of the first element in a Python list?", "0"],
        ["Which built-in function returns the length of a list?", "len"],
        ["What keyword is used to handle exceptions?", "try"],
        ["Which boolean value represents falsehood?", "false"],
    ]


def ask_question(question: str, correct_answer: str) -> bool:
    """
    Exibe uma pergunta e retorna True se o jogador acertar.
    """
    user_answer = input(f"\n❓ {question}\nYour answer: ").strip().lower()
    return user_answer == correct_answer.strip().lower()


def run_quiz(questions: list[Question]) -> int:
    """
    Executa o quiz e retorna a pontuação final.
    """
    score = 0

    print("=" * 60)
    print("🎮 Welcome to the Programming Quiz!")
    print("Answer the questions below. Good luck!")
    print("=" * 60)

    for index, (question, answer) in enumerate(questions, start=1):
        print(f"\nQuestion {index} of {len(questions)}:")
        if ask_question(question, answer):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {answer}")

    return score


def show_final_score(score: int, total: int) -> None:
    """
    Mostra a pontuação final do jogador.
    """
    print("\n" + "=" * 60)
    print(f"🏁 Quiz finished! Your score: {score} out of {total}")
    if score == total:
        print("🎉 Perfect! You're a Python master!")
    elif score >= total * 0.7:
        print("👏 Great job! You know your stuff.")
    elif score >= total * 0.4:
        print("🙂 Not bad, keep practicing!")
    else:
        print("💡 Don't worry! Every expert was once a beginner.")
    print("=" * 60)


def main() -> None:
    questions = get_questions()
    score = run_quiz(questions)
    show_final_score(score, len(questions))


if __name__ == "__main__":
    main()
