"""
Jogo da Velha Inteligente.

Implementa um jogo da velha (tic-tac-toe) em que o usuário joga contra
a máquina. A máquina utiliza o algoritmo Minimax para escolher a melhor
jogada. A lógica está organizada em classes e funções, com tipagem nativa
do Python 3.11 e seguindo padrões de codibilidade (PEP 8, docstrings e
nomenclaturas descritivas).
"""

from __future__ import annotations

import math
from typing import Optional

# Representação do tabuleiro como lista de listas de strings
Board = list[list[str]]


class TicTacToe:
    """
    Classe que gerencia o estado do jogo, operações no tabuleiro e lógica
    do Minimax para a inteligência artificial.
    """

    def __init__(self) -> None:
        """
        Inicializa o tabuleiro vazio e define o jogador inicial (X).
        """
        self._board: Board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player: str = 'X'  # 'X' é o humano, 'O' é a máquina

    def display_board(self) -> None:
        """
        Exibe o tabuleiro no console.
        """
        print()
        for i, row in enumerate(self._board):
            print(' | '.join(row))
            if i < 2:
                print('-' * 9)
        print()

    def make_move(self, row: int, col: int, player: str) -> bool:
        """
        Tenta fazer uma jogada na posição (row, col) para o jogador dado.
        Retorna True se a jogada for válida e executada, ou False caso contrário.
        """
        if not (0 <= row <= 2 and 0 <= col <= 2):
            return False
        if self._board[row][col] != ' ':
            return False

        self._board[row][col] = player
        return True

    def check_winner(self) -> Optional[str]:
        """
        Verifica se há um vencedor. Retorna 'X' ou 'O' se houver vencedor,
        ou None caso contrário.
        """
        lines = []

        # Linhas e colunas
        for i in range(3):
            lines.append(self._board[i])                     # linha i
            lines.append([self._board[0][i], self._board[1][i],
                          self._board[2][i]])                # coluna i

        # Diagonais
        lines.append([self._board[0][0], self._board[1][1],
                      self._board[2][2]])
        lines.append([self._board[0][2], self._board[1][1],
                      self._board[2][0]])

        for line in lines:
            if line[0] != ' ' and line[0] == line[1] == line[2]:
                return line[0]

        return None

    def check_draw(self) -> bool:
        """
        Retorna True se todas as casas estiverem preenchidas e não houver vencedor.
        """
        if self.check_winner() is not None:
            return False
        return all(cell != ' ' for row in self._board for cell in row)

    def switch_player(self) -> None:
        """
        Alterna o jogador atual entre 'X' e 'O'.
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_human_move(self) -> tuple[int, int]:
        """
        Solicita ao usuário as coordenadas da jogada (linha e coluna).
        Retorna uma tupla (row, col). Lida com exceções de entrada inválida.
        """
        while True:
            try:
                row = int(input('Digite a linha (0, 1 ou 2): ').strip())
                col = int(input('Digite a coluna (0, 1 ou 2): ').strip())
            except ValueError:
                print('Entrada inválida. Digite números inteiros entre 0 e 2.')
                continue

            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col

            print('Coordenadas fora do intervalo. Tente novamente.')

    def minimax(self, is_maximizing: bool) -> int:
        """
        Implementação recursiva do algoritmo Minimax.
        - is_maximizing: True quando for a vez da máquina ('O'),
          False quando for a vez do humano ('X').
        Retorna o valor de pontuação do estado atual do tabuleiro.
        """
        winner = self.check_winner()
        if winner == 'O':
            return 1
        if winner == 'X':
            return -1
        if self.check_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if self._board[i][j] == ' ':
                        self._board[i][j] = 'O'
                        score = self.minimax(is_maximizing=False)
                        self._board[i][j] = ' '
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if self._board[i][j] == ' ':
                        self._board[i][j] = 'X'
                        score = self.minimax(is_maximizing=True)
                        self._board[i][j] = ' '
                        best_score = min(best_score, score)
            return best_score

    def get_best_move(self) -> tuple[int, int]:
        """
        Determina a melhor jogada para a máquina ('O') usando Minimax.
        Retorna a tupla (linha, coluna) da jogada escolhida.
        """
        best_score = -math.inf
        best_move: tuple[int, int] = (0, 0)

        for i in range(3):
            for j in range(3):
                if self._board[i][j] == ' ':
                    self._board[i][j] = 'O'
                    score = self.minimax(is_maximizing=False)
                    self._board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

    def play(self) -> None:
        """
        Loop principal do jogo, alternando entre humano e máquina até
        que haja um vencedor ou empate.
        """
        print('Bem-vindo ao Jogo da Velha!')
        print('Você é X e a máquina é O.\n')
        self.display_board()

        while True:
            if self.current_player == 'X':
                row, col = self.get_human_move()
                if not self.make_move(row, col, 'X'):
                    print('Jogada inválida! Tente novamente.')
                    continue
            else:
                print('Vez da máquina (O)...')
                row, col = self.get_best_move()
                self.make_move(row, col, 'O')

            self.display_board()

            winner = self.check_winner()
            if winner is not None:
                print(f'Jogador {winner} venceu!')
                break

            if self.check_draw():
                print('Fim de jogo: empate!')
                break

            self.switch_player()


def main() -> None:
    """
    Inicializa e inicia o jogo.
    """
    game = TicTacToe()
    game.play()


if __name__ == '__main__':
    main()
