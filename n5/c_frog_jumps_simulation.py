"""
Problema do Sapo na Lagoa — Contagem de Formas de Atravessar Pulando 1 ou 2 Pedras

Descrição:
-----------
Este programa calcula o número de formas distintas pelas quais um sapo pode atravessar uma lagoa
pulando sobre pedras, podendo avançar de 1 ou 2 pedras a cada salto. O objetivo é determinar quantas
sequências diferentes de saltos levam o sapo da margem inicial (posição 0) até a última pedra (posição n).

Regras do problema:
-------------------
- O sapo inicia na posição 0 (antes da primeira pedra).
- Em cada movimento, o sapo pode saltar para a próxima pedra (salto de 1) ou pular uma pedra e ir para a seguinte (salto de 2).
- O sapo deve alcançar exatamente a última pedra (posição n).

Relação com a Sequência de Fibonacci:
--------------------------------------
A sequência de Fibonacci é uma série numérica definida recursivamente como a soma dos dois termos anteriores:

    F(0) = 0,  F(1) = 1,  F(n) = F(n-1) + F(n-2)  para n ≥ 2

Os primeiros termos são: 0, 1, 1, 2, 3, 5, 8, 13, ...

No problema do sapo na lagoa, o número de formas que o sapo pode alcançar a pedra n corresponde a um termo da sequência de Fibonacci deslocado, pois:

- O número de formas de alcançar a pedra n é a soma das formas de alcançar as pedras (n-1) e (n-2).
- Isso ocorre porque o sapo pode saltar 1 ou 2 pedras.
- A recorrência é:

    ways(n) = ways(n-1) + ways(n-2)

com condições iniciais:

    ways(0) = 1  (uma forma de estar na posição inicial sem saltos)
    ways(1) = 1  (apenas um salto de 1 pedra possível)

Assim,

    ways(n) = F_{n+1}

onde F_{n} é o n-ésimo número da sequência de Fibonacci padrão.

Objetivo do código:
-------------------
- Implementar uma função recursiva pura que explore todas as possibilidades de salto.
- Mostrar, de forma clara e indentada, todas as chamadas recursivas e seus retornos.
- Calcular e exibir o número total de formas distintas para o sapo atravessar a lagoa.

Aplicações:
-----------
Este problema é um exemplo clássico para ilustrar recursão, programação dinâmica, e a ocorrência prática da sequência de Fibonacci em problemas combinatórios.
"""


from typing import Final


def count_frog_jumps(position: int, target: int, depth: int = 0) -> int:
    """
    Recursively counts the number of distinct ways a frog can reach the last stone
    by jumping either 1 or 2 steps at a time.

    Parameters:
    -----------
    position : int
        Current position of the frog.

    target : int
        Index of the final stone.

    depth : int
        Current recursion depth, used for visual indentation of the output.

    Returns:
    --------
    int
        Number of valid paths from current position to the target.
    """
    indent: Final[str] = "    " * depth
    print(f"{indent}Entering position {position}")

    if position > target:
        print(f"{indent}Exceeded target ({position} > {target}) → return 0")
        return 0

    if position == target:
        print(f"{indent}Reached target ({position}) → return 1")
        return 1

    print(f"{indent}Trying jump of 1 from position {position}:")
    paths_one_step = count_frog_jumps(position + 1, target, depth + 1)
    print(f"{indent}{'-'*40}")

    print(f"{indent}Trying jump of 2 from position {position}:")
    paths_two_steps = count_frog_jumps(position + 2, target, depth + 1)
    print(f"{indent}{'-'*40}")

    total_paths = paths_one_step + paths_two_steps
    print(f"{indent}Total paths from position {position}: {total_paths}")

    return total_paths


def main() -> None:
    """
    Entry point for the frog jump simulation.
    """
    total_stones: Final[int] = 5  # Change this value to test with different stone counts
    print(f"\nFROG JUMP SIMULATION — Total stones: {total_stones}\n")
    total_paths = count_frog_jumps(0, total_stones)
    print(
        f"\nTotal distinct paths to cross {total_stones} stones: {total_paths}")


if __name__ == "__main__":
    main()
