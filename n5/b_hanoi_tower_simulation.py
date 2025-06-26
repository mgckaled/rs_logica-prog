"""
Torre de Hanói — Simulação com Visualização em Etapas

Descrição:
-----------
A Torre de Hanói é um clássico problema de lógica e recursão proposto pelo matemático Édouard Lucas em 1883. 
O enunciado consiste em três torres (ou hastes) e um número `n` de discos de tamanhos diferentes empilhados 
na primeira torre, do maior (na base) para o menor (no topo). O objetivo é mover toda a pilha de discos 
para a terceira torre, obedecendo às seguintes regras:

Regras:
--------
1. Apenas um disco pode ser movido por vez.
2. Um disco só pode ser movido do topo de uma pilha.
3. Um disco maior **nunca pode ser colocado sobre um disco menor**.

Estratégia de solução:
-----------------------
O problema é resolvido de forma recursiva. Para mover `n` discos da torre de origem para a torre de destino, usa-se a torre auxiliar como suporte:

1. Mover os `n-1` discos superiores da torre de origem para a torre auxiliar.
2. Mover o maior disco (o `n`-ésimo) diretamente da torre de origem para a torre de destino.
3. Mover os `n-1` discos da torre auxiliar para a torre de destino.

A cada chamada recursiva, o problema é reduzido até que reste apenas 1 disco (caso base), que pode ser movido diretamente.

Complexidade:
--------------
- Número mínimo de movimentos necessários: `2^n - 1`
- Tempo de execução: **O(2^n)** — crescimento exponencial

Uso neste módulo:
-------------------
Este script simula passo a passo o processo da Torre de Hanói, imprimindo a cada etapa:
- qual disco foi movido
- de qual torre para qual torre
- o estado atual de todas as torres

É possível alterar o número de discos modificando a variável `num_disks` na função `main()`.

Recomenda-se manter o número de discos pequeno (por exemplo, 3 a 6) para facilitar a visualização.
"""


def move_disk(
    towers: dict[str, list[int]],
    source: str,
    target: str,
    step: int
) -> None:
    """
    Move the top disk from source to target tower and print the state.
    """
    disk = towers[source].pop()
    towers[target].append(disk)

    print(f"\nStep {step}: Move disk {disk} from {source} ➜ {target}")
    print_towers(towers)


def solve_hanoi(
    n: int,
    source: str,
    target: str,
    auxiliary: str,
    towers: dict[str, list[int]],
    step_counter: list[int]
) -> None:
    """
    Solve the Tower of Hanoi puzzle recursively.
    """
    if n == 1:
        step_counter[0] += 1
        move_disk(towers, source, target, step_counter[0])
    else:
        solve_hanoi(n - 1, source, auxiliary, target, towers, step_counter)
        step_counter[0] += 1
        move_disk(towers, source, target, step_counter[0])
        solve_hanoi(n - 1, auxiliary, target, source, towers, step_counter)


def print_towers(towers: dict[str, list[int]]) -> None:
    """
    Print the current state of all towers.
    """
    for name in ["A", "B", "C"]:
        print(f"Tower {name}: {towers[name]}")


def initialize_towers(num_disks: int) -> dict[str, list[int]]:
    """
    Initialize towers with all disks on source tower (A).
    """
    return {
        "A": list(reversed(range(1, num_disks + 1))),
        "B": [],
        "C": [],
    }


def main() -> None:
    """
    Entry point for the Tower of Hanoi simulation.
    """
    num_disks = 6  # Change this to increase difficulty

    towers = initialize_towers(num_disks)
    print("Initial tower state:")
    print_towers(towers)

    step_counter = [0]  # Use mutable list to track step count in recursion
    solve_hanoi(num_disks, "A", "C", "B", towers, step_counter)

    print("\nFinal tower state:")
    print_towers(towers)


if __name__ == "__main__":
    main()
