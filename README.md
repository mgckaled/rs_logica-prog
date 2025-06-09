<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD014 -->

# Formação Rocketseat - Lógica de Programação

## Sobre

Repositório contendo a formação completa de Lógica de Programação (2025), desenvolvido pela Faculdade de Tecnologia Rocketseat

## Conteúdo

### Nível 1 - Fundamentos de Lógica de Programação

Neste módulo, você aprenderá os fundamentos da lógica de programação, desde conectivos lógicos e tabelas verdade até a construção de algoritmos e desenvolvimento de programas. Exploraremos fluxogramas, pseudocódigo, controle de fluxo, variáveis, funções e arrays, preparando você para estruturar soluções eficientes. O aprendizado será consolidado com projetos práticos, como um jogo de adivinhação e um Jogo da Velha.

> Acesso ao [conteúdo das aulas](.github/docs/content/notes/n1.md).
>
> [Quizzes e Teste Avaliativo](.github/docs/content/tests/t1.md#questionário-avaliativo)
>
> [Exercício Prático de Fixação](./n1/tabela_verdade.py) - [Tabela Verdade](./n1/tabela_verdade.md)

---

### Nível 2 - Escrevendo o seu primeiro programa

Neste módulo, você aprenderá os princípios essenciais para começar enfim a programar. Vamos desde a preparação do ambiente até a construção de programas interativos, explorando variáveis, estruturas condicionais, loops e funções. Você desenvolverá projetos práticos, como um jogo de adivinhação, consolidando os conceitos enquanto escreve código de verdade.

> Acesso ao [conteúdo das aulas](.github/docs/content/notes/n2.md).
>
> [Quizzes e Teste Avaliativo](.github/docs/content/tests/t2.md#questionário-avaliativo)

---

### Nível 3 - Lendo, Depurando e entendendo códigos

Neste módulo, vamos desenvolver uma habilidade essencial para qualquer pessoa que programa: a capacidade de ler, entender e depurar códigos com segurança. Você vaboas práticas e também dar os primeiros passos em refatoração - aprendendo a melhorar códigos já existentes. O objetivo é que você desenvolva não só para funcionar, mas para ser entendido, mantido e evoluído com facilidade.

---

### Nível 5 - Desafios com raciocínio lógico

Neste módulo, vamos colocar a lógica em prática com desafios clássicos e envolventes que estimulam o raciocínio e a criatividade na resolução de problemas. Abordaremos conceitos como recursividade, decisões e possibilidades, além de desenvolver o pensamento exploratório por meio de exercícios como a Torre de Hanói, o Sapo na Lagoa e outros desafios lógicos. Prepare-se para treinar sua mente, aprender a pensar como um programador e fortalecer sua capacidade de encontrar soluções elegantes para problemas complexos.

---

### Conteúdo Bonús - Estrutura de Dados

Neste módulo, você vai mergulhar nas principais estruturas de dados utilizadas na programação. Vamos aprofundar o entendimento sobre os tipos de dados e explorar, na prática, como funcionam tuplas, listas, dicionários, conjuntos, pilhas, filas, listas encadeadas entre outros. Com exemplos claros e acessíveis, você vai entender quando e por que usar cada estrutura, além de desenvolver um raciocínio mais organizado e eficiente na hora de escrever seus algoritmos.

---

## Tecnologias

### Linguagem de Programação

- [`python`](https://www.python.org/) (v3.11.9)

### Gerenciadores de Ambiente Virtual e Dependências

- [`pyenv`](https://github.com/pyenv/pyenv)
- [`pipenv`](https://pipenv.pypa.io/en/latest/)
  
- [![Pipfile](https://img.shields.io/badge/Consultar-Pipfile-blue?style=flat-square)](./Pipfile)  *(Clique no badge para consultar dependências)*

## Como clonar o projeto?

1. Certifique-se de que está usando o `pyenv` e o `pipenv` para gerenciar as dependências do projeto. Veja como instalar e configurar clicando nos respectivos links do tópico [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual-e-dependências).

2. Faça o clone pelo Github:

    ```shell
    git clone https://github.com/mgckaled/rs_logica-prog.git
    ```

3. Acesse o diretório:

    ```shell
    cd rs_logica-prog.git
    ```

4. Ative o ambiente virtual pelo terminal

    ```shell
    pipenv shell
    ```

5. Instale as dependências. (Certifique-se de estar utilzando a versão exata do python - 3.11.9)

    ```shell
    pipenv install
    ```

    ou, como um recurso de segurança, instale dependências exatas do `requirements.txt`:

    ```shell
    pipenv install -r requirements.txt
    ```

---

<h5 align="center">
  2025 - <a href="https://github.com/mgckaled/">Marcel Kaled</a>
</h5>
