"""
Simulação de Remoção de Bolas Brancas e Pretas — Regras Condicionais

Descrição:
-----------
Este programa simula um jogo baseado em regras condicionais de remoção e devolução de bolas 
de uma caixa. As bolas podem ser **pretas** ou **brancas**, e o comportamento depende da 
combinação sorteada de duas bolas por vez.

O objetivo do programa é simular esse processo repetidamente até que reste **apenas uma bola** na caixa, 
exibindo passo a passo cada movimentação.

Regras do jogo:
----------------
A cada rodada, duas bolas são retiradas da caixa ao acaso. As ações dependem da combinação retirada:

1. **Duas pretas (⚫, ⚫)**:
    - Remove **uma** bola preta.
    - Devolve a **outra** preta à caixa.

2. **Duas brancas (⚪, ⚪)**:
    - Remove **ambas** as bolas brancas.
    - Devolve **uma** bola preta à caixa.

3. **Uma branca e uma preta (⚫, ⚪ ou ⚪, ⚫)**:
    - Remove a **bola preta**.
    - Devolve a **bola branca** à caixa.

Estratégia de simulação:
-------------------------
- O conteúdo da caixa é representado por uma lista de strings (`"black"`, `"white"`).
- A cada iteração:
    - Duas bolas são embaralhadas e retiradas.
    - A regra apropriada é aplicada.
    - O estado da caixa é atualizado e impresso.
- O processo continua até sobrar **uma única bola**.

Complexidade:
--------------
- O número de iterações depende da quantidade inicial de bolas e das regras aplicadas.
- O processo é estocástico (aleatório), mas termina sempre com exatamente uma bola remanescente.

Uso neste módulo:
-------------------
O script permite definir a composição inicial da caixa (quantas bolas pretas e brancas).
A cada etapa, o console exibe:
- As bolas sorteadas
- A ação aplicada
- O novo estado da caixa

Ideal para fins didáticos, análise de algoritmos condicionais e simulações probabilísticas.
"""

from collections import Counter
from random import shuffle

BLACK_BALL = "black"
WHITE_BALL = "white"


def apply_rules(ball1: str, ball2: str) -> str | None:
    """
    Apply the rules of the game to two drawn balls.
    Return the ball to be returned to the box, or None if none.
    """
    if ball1 == BLACK_BALL and ball2 == BLACK_BALL:
        print(
            f"Drawn: ({ball1}, {ball2}) ➜ Remove one {BLACK_BALL}, return one {BLACK_BALL}")
        return BLACK_BALL
    elif ball1 == WHITE_BALL and ball2 == WHITE_BALL:
        print(
            f"Drawn: ({ball1}, {ball2}) ➜ Remove both {WHITE_BALL}, return one {BLACK_BALL}")
        return BLACK_BALL
    else:
        print(
            f"Drawn: ({ball1}, {ball2}) ➜ Remove one {BLACK_BALL}, return one {WHITE_BALL}")
        return WHITE_BALL


def draw_two_balls(box: list[str]) -> tuple[str, str] | None:
    """
    Randomly draw two balls from the box.
    Return a tuple of two balls or None if fewer than two balls are available.
    """
    if len(box) < 2:
        return None

    shuffle(box)
    return box.pop(), box.pop()


def simulate_ball_game(initial_box: list[str]) -> str:
    """
    Simulate the ball game step by step until one ball remains.
    Return the color of the last remaining ball.
    """
    box = initial_box.copy()
    step = 1

    while len(box) > 1:
        print(f"\nStep {step}:")
        print(f"Current box: {count_balls(box)}")

        drawn = draw_two_balls(box)
        if drawn is None:
            break

        ball1, ball2 = drawn
        returned_ball = apply_rules(ball1, ball2)

        if returned_ball:
            box.append(returned_ball)

        print(f"Box after step {step}: {count_balls(box)}")
        step += 1

    print(f"\nFinal box: {count_balls(box)}")
    return box[0] if box else "empty"


def count_balls(box: list[str]) -> dict[str, int]:
    """
    Count the number of black and white balls in the box.
    """
    return dict(Counter(box))


def main() -> None:
    """
    Entry point of the simulation.
    """
    initial_box = (
        [BLACK_BALL] * 4 +
        [WHITE_BALL] * 4
    )

    print("Initial box composition:", count_balls(initial_box))
    result = simulate_ball_game(initial_box)
    print("\nFinal remaining ball:", result)


if __name__ == "__main__":
    main()
