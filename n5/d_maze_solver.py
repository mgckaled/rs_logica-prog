"""
Simulação de Resolução de Labirinto com Backtracking e Visualização Interativa

Descrição:
-----------
Este programa simula a resolução de um labirinto 2D utilizando o algoritmo de backtracking (retorno) e exibe,
de forma visual no terminal, cada passo da tentativa do algoritmo até encontrar (ou não) o caminho para a saída.

O labirinto é gerado de forma aleatória, com base em uma matriz de dimensão ajustável (por padrão, 20x20),
em que células podem ser livres (0) ou conter paredes (1). A geração é feita utilizando a biblioteca NumPy,
com uma probabilidade definida de inserção de paredes.

Objetivo:
---------
Encontrar um caminho entre a posição inicial (canto superior esquerdo — coordenada (0,0))
e a posição final (canto inferior direito — coordenada (n-1, n-1)), percorrendo apenas células livres.

Elementos Visuais:
-------------------
Durante a execução, o programa imprime o labirinto passo a passo, com moldura e símbolos:
- `S` : posição inicial (start)
- `E` : posição final (exit)
- `█` : parede (obstáculo)
- `.` : célula atualmente explorada
- `X` : célula explorada e abandonada (beco sem saída)
- `*` : parte do caminho correto até a saída

Recursos Técnicos:
-------------------
- Algoritmo recursivo com backtracking (busca exaustiva)
- Geração de labirinto aleatório com NumPy (`np.random.choice`)
- Impressão interativa com atraso (`time.sleep(1)`) para visualização passo a passo
- Moldura decorativa com caracteres Unicode (┌ ┐ └ ┘ ─ │) para clareza
- Tentativas múltiplas (até 50) para garantir que ao menos um labirinto gerado seja solucionável

Parâmetros importantes:
------------------------
- `size`: tamanho do labirinto (ex: 20 → 20x20)
- `wall_prob`: probabilidade de uma célula ser uma parede (padrão: 0.25)
- `max_attempts`: número máximo de tentativas para gerar um labirinto com solução

Aplicações:
-----------
Este código é uma excelente introdução aos conceitos de:
- Recursão e backtracking
- Problemas de busca em grade bidimensional
- Visualização de algoritmos em tempo real
- Lógica de caminhos em grafos implícitos (como labirintos)

Requisitos:
------------
- Python 3.11 ou superior
- NumPy instalado (`pip install numpy`)
"""


import time

import numpy as np

Maze = list[list[int]]
Path = list[list[str]]

FREE = 0
WALL = 1


def print_maze(maze: Maze, path: Path) -> None:
    width = len(maze[0])
    horizontal_border = "─" * (width * 2)

    print("\n" + "┌" + horizontal_border + "┐")

    for i, row in enumerate(path):
        line = "│ "
        for j, cell in enumerate(row):
            if (i, j) == (0, 0):
                line += "S "
            elif (i, j) == (len(maze) - 1, len(maze[0]) - 1):
                line += "E "
            elif maze[i][j] == WALL:
                line += "█ "
            else:
                line += f"{cell} "
        line += "│"
        print(line)

    print("└" + horizontal_border + "┘\n")
    time.sleep(0.5)


def solve_maze(maze: Maze, path: Path, row: int, col: int) -> bool:
    if not is_valid(maze, row, col):
        return False
    if path[row][col] in (".", "X"):
        return False

    path[row][col] = "."
    print_maze(maze, path)

    if (row, col) == (len(maze) - 1, len(maze[0]) - 1):
        path[row][col] = "*"
        print("Reached the exit!")
        print_maze(maze, path)
        return True

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dr, dc in directions:
        if solve_maze(maze, path, row + dr, col + dc):
            path[row][col] = "*"
            return True

    path[row][col] = "X"
    print_maze(maze, path)
    return False


def is_valid(maze: Maze, row: int, col: int) -> bool:
    rows = len(maze)
    cols = len(maze[0])
    return 0 <= row < rows and 0 <= col < cols and maze[row][col] == FREE


def init_path(maze: Maze) -> Path:
    return [[" " for _ in row] for row in maze]


def generate_random_maze(size: int, wall_prob: float = 0.50) -> Maze:
    maze_np = np.random.choice([FREE, WALL], size=(
        size, size), p=[1 - wall_prob, wall_prob])
    maze_np[0, 0] = FREE
    maze_np[size - 1, size - 1] = FREE
    return maze_np.tolist()


def main() -> None:
    size = 20
    max_attempts = 50
    attempt = 0

    while attempt < max_attempts:
        maze: Maze = generate_random_maze(size, wall_prob=0.25)
        path = init_path(maze)

        print(f"\nAttempt {attempt + 1} — Initial {size}x{size} Maze:")
        print_maze(maze, path)

        if solve_maze(maze, path, 0, 0):
            print(f"Solved on attempt {attempt + 1}")
            return

        print("No solution found for this attempt.\n")
        attempt += 1

    print(f"Failed to generate a solvable maze after {max_attempts} attempts.")


if __name__ == "__main__":
    main()
