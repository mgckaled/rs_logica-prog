import random
from typing import Literal

GridSymbol = Literal[" ", "X", "💎"]
Board = list[list[GridSymbol]]

# Configurações do jogo
BOARD_SIZE = 4
MAX_ATTEMPTS = 6


def create_board() -> Board:
    """
    Cria o tabuleiro com espaços vazios.
    """
    return [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def generate_random_position() -> tuple[int, int]:
    """
    Gera uma posição aleatória para o tesouro.
    """
    row = random.randint(0, BOARD_SIZE - 1)
    col = random.randint(0, BOARD_SIZE - 1)
    return row, col


def print_board(board: Board) -> None:
    """
    Exibe o tabuleiro com coordenadas.
    """
    print("\n   " + "   ".join(str(i) for i in range(BOARD_SIZE)))
    print("  +" + "---+" * BOARD_SIZE)
    for i, row in enumerate(board):
        row_display = " | ".join(row)
        print(f"{i} | {row_display} |")
        print("  +" + "---+" * BOARD_SIZE)


def get_coordinates() -> tuple[int, int] | None:
    """
    Solicita linha e coluna ao jogador. Retorna None em erro.
    """
    try:
        raw = input("🔭 Enter row and column (e.g., 2 3): ").strip()
        row_str, col_str = raw.split()
        row, col = int(row_str), int(col_str)
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            return row, col
        else:
            print(
                f"❌ Invalid position. Values must be between 0 and {BOARD_SIZE - 1}.")
            return None
    except ValueError:
        print("⚠️  Please enter two numbers separated by a space.")
        return None


def play_turn(board: Board, row: int, col: int, treasure: tuple[int, int]) -> Literal["hit", "miss", "repeat"]:
    """
    Executa uma jogada. Atualiza o tabuleiro e retorna o resultado.
    """
    if board[row][col] in {"X", "💎"}:
        return "repeat"

    if (row, col) == treasure:
        board[row][col] = "💎"
        return "hit"

    board[row][col] = "X"
    return "miss"


def main() -> None:
    board = create_board()
    treasure = generate_random_position()
    attempts = 0

    print("=" * 60)
    print("🚀 Welcome to the Intergalactic Treasure Hunt 4x4!")
    print(
        f"A mysterious planet hides a treasure in a {BOARD_SIZE}x{BOARD_SIZE} grid.")
    print(f"You have {MAX_ATTEMPTS} scans to locate it. Good luck, explorer!")
    print("=" * 60)

    while attempts < MAX_ATTEMPTS:
        print_board(board)
        print(f"\n🧭 Attempt {attempts + 1} of {MAX_ATTEMPTS}")
        coords = get_coordinates()

        if coords is None:
            continue

        row, col = coords
        result = play_turn(board, row, col, treasure)

        match result:
            case "hit":
                print_board(board)
                print("\n💎 You found the treasure! Stellar work, captain!")
                break
            case "miss":
                print("🌌 Empty space... keep searching.")
                attempts += 1
            case "repeat":
                print("🔁 You've already scanned this position!")

    else:
        print("\n💥 Mission failed. You've used all your scans.")
        print(f"The treasure was at row {treasure[0]}, column {treasure[1]}.")
        # Revela o tesouro no tabuleiro final
        tr, tc = treasure
        if board[tr][tc] == " ":
            board[tr][tc] = "💎"
        print_board(board)

    print("\n👋 Mission complete. See you in the next galaxy!")


if __name__ == "__main__":
    main()
