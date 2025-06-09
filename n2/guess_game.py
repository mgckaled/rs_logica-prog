"""
Jogo de Adivinhação Inteligente de Animais.

Este módulo implementa um jogo de adivinhação que aprende novas perguntas
e animais conforme o usuário interage. A lógica é baseada em uma árvore de
decisão binária, onde cada nó representa uma pergunta que leva a dois
ramos: “sim” ou “não”. As folhas da árvore são palpites (nomes de animais).

O jogo persiste o conhecimento em um arquivo JSON para que saiba mais
sobre animais a cada execução.
"""

from __future__ import annotations

import json
import os

# Caminho do arquivo para persistir a árvore de decisão
DATA_FILE_PATH = "./n2/animal_guess_tree.json"


class Node:
    """
    Representa um nó na árvore de decisão.

    Um nó pode ser de dois tipos:
    - Nó de pergunta: contém o texto da pergunta e referências para
      os nós filhos (respostas "sim" e "não").
    - Nó de palpite (folha): contém o nome do animal que será chutado.
    """

    def __init__(
        self,
        question: str | None = None,
        guess: str | None = None,
        yes_branch: Node | None = None,
        no_branch: Node | None = None,
    ) -> None:
        self.question: str | None = question
        self.guess: str | None = guess
        self.yes_branch: Node | None = yes_branch
        self.no_branch: Node | None = no_branch

    def is_leaf(self) -> bool:
        """
        Retorna True se o nó for uma folha (palpite), ou False se for um nó de pergunta.
        """
        return self.guess is not None

    def to_dict(self) -> dict[str, any]:
        """
        Converte o nó (e seus filhos) em um dicionário serializável em JSON.
        """
        if self.is_leaf():
            return {"guess": self.guess}

        return {
            "question": self.question,
            "yes": self.yes_branch.to_dict() if self.yes_branch else None,
            "no": self.no_branch.to_dict() if self.no_branch else None,
        }

    @staticmethod
    def from_dict(data: dict[str, any]) -> Node:
        """
        Constrói um nó (e seus filhos) a partir de um dicionário carregado de JSON.
        """
        if "guess" in data:
            return Node(guess=data["guess"])

        yes_node = Node.from_dict(data["yes"]) if data.get("yes") else None
        no_node = Node.from_dict(data["no"]) if data.get("no") else None
        return Node(question=data.get("question"), yes_branch=yes_node, no_branch=no_node)


def load_tree(file_path: str) -> Node:
    """
    Carrega a árvore de decisão a partir de um arquivo JSON.

    Se o arquivo não existir ou estiver corrompido, cria uma árvore inicial
    com um palpite genérico.
    """
    if not os.path.isfile(file_path):
        # Árvore inicial: pergunta simples sobre macaco e elefante
        return Node(
            question="Seu animal gosta de bananas?",
            guess=None,
            yes_branch=Node(guess="macaco"),
            no_branch=Node(guess="elefante"),
        )

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return Node.from_dict(data)
    except (json.JSONDecodeError, IOError):
        # Em caso de falha, retornar árvore padrão
        return Node(
            question="Seu animal gosta de bananas?",
            guess=None,
            yes_branch=Node(guess="macaco"),
            no_branch=Node(guess="elefante"),
        )


def save_tree(root: Node, file_path: str) -> None:
    """
    Salva a árvore de decisão em um arquivo JSON.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(root.to_dict(), file, ensure_ascii=False, indent=4)


def ask_yes_no(prompt_text: str) -> bool:
    """
    Exibe uma pergunta de sim/não ao usuário e retorna True para 's' e False para 'n'.

    Repete até receber uma resposta válida.
    """
    while True:
        answer = input(f"{prompt_text} (s/n): ").strip().lower()
        if answer == "s":
            return True
        if answer == "n":
            return False
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


def traverse_and_learn(current_node: Node) -> None:
    """
    Percorre a árvore de decisão recursivamente, fazendo perguntas ao usuário.

    Quando chega a um nó folha (palpite), tenta acertar o animal. Se errar,
    solicita ao usuário o animal correto e a pergunta que distinga dos palpites
    atuais, expandindo a árvore.
    """
    if current_node.is_leaf():
        # Folha: faz o palpite
        guess = current_node.guess  # tipo garantido por is_leaf()
        if ask_yes_no(f"Você está pensando em {guess}?"):
            print("Uhul! Acertei de novo!")
        else:
            # Aprender novo animal
            learn_new_animal(current_node)
        return

    # Nó de pergunta: faz a pergunta e segue para a ramificação correta
    question = current_node.question  # tipo garantido por não ser folha
    if ask_yes_no(question):
        if current_node.yes_branch:
            traverse_and_learn(current_node.yes_branch)
    else:
        if current_node.no_branch:
            traverse_and_learn(current_node.no_branch)


def learn_new_animal(leaf_node: Node) -> None:
    """
    Atualiza a árvore quando o palpite estiver errado.

    Solicita ao usuário:
    - O animal correto em que ele pensou.
    - Uma pergunta que diferencie o animal correto do palpite.
    - Qual seria a resposta para essa nova pergunta no caso do novo animal.
    Substitui o nó folha por um nó de pergunta e ajusta as ramificações.
    """
    correct_animal = input("Desisto! Em qual animal você pensou? ").strip()
    new_question = input(
        f"Qual pergunta você faria para diferenciar {correct_animal} de "
        f"{leaf_node.guess}? "
    ).strip()

    answer_for_new = ask_yes_no(
        f"Para o animal {correct_animal}, qual seria a resposta para a pergunta "
        f"\"{new_question}\"?"
    )

    # Cria novo nó folha para o animal correto
    new_leaf = Node(guess=correct_animal)

    # Nó antigo que será substituído
    old_leaf = Node(guess=leaf_node.guess)  # tipo garantido por is_leaf()

    # Atualiza o nó atual para uma pergunta
    leaf_node.question = new_question
    leaf_node.guess = None

    if answer_for_new:
        leaf_node.yes_branch = new_leaf
        leaf_node.no_branch = old_leaf
    else:
        leaf_node.yes_branch = old_leaf
        leaf_node.no_branch = new_leaf

    print("Obrigado! Aprendi algo novo!")


def main() -> None:
    """
    Função principal que carrega a árvore, executa o loop do jogo e salva
    o conhecimento aprendido pelo usuário.
    """
    print("Bem-vindo ao Jogo de Adivinhação de Animais!")
    print("Pense em um animal e responda às perguntas com 's' ou 'n'.\n")

    # Carregar ou criar a árvore de decisão
    root_node = load_tree(DATA_FILE_PATH)

    try:
        while True:
            traverse_and_learn(root_node)
            if not ask_yes_no("Deseja jogar novamente?"):
                break
            print("\nVamos jogar novamente! Pense em outro animal.\n")
    except KeyboardInterrupt:
        print("\nEncerrando o jogo...")

    # Salvar a árvore atualizada
    save_tree(root_node, DATA_FILE_PATH)
    print("Até a próxima! Obrigado por jogar.")


if __name__ == "__main__":
    main()
