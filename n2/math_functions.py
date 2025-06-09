"""
Módulo de Demonstração de Funções Lineares e Quadráticas.

Define funções para avaliar expressões lineares (f(x) = a·x + b) e
quadráticas (g(x) = a·x² + b·x + c), além de exemplos de uso.
"""

from __future__ import annotations

from typing import Callable


def linear(a: float, b: float) -> Callable[[float], float]:
    """
    Retorna uma função linear f(x) = a·x + b.

    :param a: coeficiente angular
    :param b: coeficiente linear (intercepto)
    :return: função que recebe x e devolve a·x + b
    """
    def f(x: float) -> float:
        return a * x + b
    return f


def quadratic(a: float, b: float, c: float) -> Callable[[float], float]:
    """
    Retorna uma função quadrática g(x) = a·x² + b·x + c.

    :param a: coeficiente de x²
    :param b: coeficiente de x
    :param c: termo constante (intercepto)
    :return: função que recebe x e devolve a·x² + b·x + c
    """
    def g(x: float) -> float:
        return a * x**2 + b * x + c
    return g


def evaluate_function(func: Callable[[float], float], inputs: list[float]) -> list[tuple[float, float]]:
    """
    Avalia uma função em múltiplos pontos.

    :param func: função numérica de um argumento
    :param inputs: lista de valores de x para avaliação
    :return: lista de tuplas (x, func(x))
    """
    return [(x, func(x)) for x in inputs]


def main() -> None:
    """
    Exemplo de uso das funções linear e quadrática.
    """
    # Definição de uma função linear f(x) = 2·x + 1
    f = linear(a=2.0, b=1.0)
    # Definição de uma função quadrática g(x) = x² - 3·x + 2
    g = quadratic(a=1.0, b=-3.0, c=2.0)

    # Pontos de avaliação
    pontos: list[float] = [-2.0, -1.0, 0.0, 1.0, 2.0]

    # Avaliar f e g nos mesmos pontos
    resultados_f = evaluate_function(f, pontos)
    resultados_g = evaluate_function(g, pontos)

    print("Avaliação da função linear f(x) = 2x + 1:")
    for x, y in resultados_f:
        print(f"f({x}) = {y:.2f}")

    print("\nAvaliação da função quadrática g(x) = x² - 3x + 2:")
    for x, y in resultados_g:
        print(f"g({x}) = {y:.2f}")


if __name__ == "__main__":
    main()
