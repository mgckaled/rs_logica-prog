#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exemplos de manipulação de arrays em Python:
- Listas nativas (unidimensionais e multidimensionais)
- Arrays com NumPy (operações vetorizadas, reshape e indexação avançada)
"""

from __future__ import annotations

import numpy as np


def exemplos_listas() -> None:
    """
    Demonstra operações básicas com listas nativas do Python.
    """
    # Criação de uma lista unidimensional
    lista: list[int] = [1, 2, 3, 4, 5]
    print("Lista original:", lista)

    # Acesso por índice
    primeiro: int = lista[0]
    ultimo: int = lista[-1]
    print("Primeiro elemento:", primeiro)
    print("Último elemento:", ultimo)

    # Slicing (fatia)
    sublista: list[int] = lista[1:4]  # elementos 2, 3 e 4
    print("Sublista [1:4]:", sublista)

    # Adicionar e remover elementos
    lista.append(6)
    lista.remove(3)
    print("Após append(6) e remove(3):", lista)

    # Compreensão de lista (list comprehension)
    quadrados: list[int] = [x**2 for x in lista]
    print("Lista de quadrados:", quadrados)

    # Lista multidimensional (matriz 3×3)
    matriz: list[list[int]] = [
        [i + j*3 + 1 for i in range(3)] for j in range(3)]
    print("Matriz 3×3:")
    for linha in matriz:
        print(linha)


def exemplos_numpy() -> None:
    """
    Demonstra operações com arrays do NumPy.
    """
    # Criação de arrays
    a: np.ndarray = np.array([1, 2, 3, 4, 5])
    b: np.ndarray = np.arange(1, 10, 2)       # [1, 3, 5, 7, 9]
    c: np.ndarray = np.zeros((2, 3))          # matriz 2×3 preenchida com zeros
    d: np.ndarray = np.ones((3, 2), dtype=int)  # matriz 3×2 de uns (inteiros)

    print("\nArray a:", a)
    print("Array b:", b)
    print("Array c (zeros):\n", c)
    print("Array d (ones):\n", d)

    # Forma e reshape
    print("a.shape:", a.shape)
    a_reshaped: np.ndarray = a.reshape((5, 1))
    print("a reshaped para (5,1):\n", a_reshaped)

    # Operações vetorizadas
    soma: np.ndarray = a + b[:5]   # soma elemento a elemento
    prod: np.ndarray = a * 2       # multiplica todos os elementos por 2
    print("a + b[:5]:", soma)
    print("a * 2:", prod)

    # Indexação avançada e boolean
    pares: np.ndarray = a[a % 2 == 0]  # seleciona apenas elementos pares
    print("Elementos pares em a:", pares)

    # Operações agregadas
    print("Soma de a:", a.sum())
    print("Média de a:", a.mean())
    print("Valor máximo de a:", a.max())
    print("Valor mínimo de a:", a.min())


def main() -> None:
    """
    Roda todos os exemplos de manipulação de arrays.
    """
    print("=== Exemplos com Listas ===")
    exemplos_listas()

    print("\n=== Exemplos com NumPy ===")
    exemplos_numpy()


if __name__ == "__main__":
    main()
