import itertools
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

import pandas as pd


def parse_sentence(
    sentence: str
) -> Tuple[List[str], str, Callable[..., bool], Optional[Tuple[str, Callable[..., bool]]]]:
    """
    Retorna:
      - props: lista de rótulos das variáveis (2 ou 3 itens)
      - symbol: símbolo do conectivo final ('→','↔','∧','∨')
      - fn: função que recebe N booleans e retorna o resultado final
      - inner: opcional (inner_symbol, inner_fn) para subexpressões
    """
    s = sentence.strip().rstrip('.')
    low = s.lower()

    # Bicondicional
    if ' se e somente se ' in low:
        a, b = s.split(' se e somente se ')

        def bicond(p: bool, q: bool) -> bool:
            return p == q
        return [a.strip(), b.strip()], '↔', bicond, None

    # Implicação com consequent composto
    if low.startswith('se ') and ' então ' in low:
        ant, cons = s[3:].split(' então ', maxsplit=1)
        ant = ant.strip()

        # q ∧ r no consequent
        if ' e ' in cons:
            q_label, r_label = [x.strip()
                                for x in cons.split(' e ', maxsplit=1)]

            def inner_and(q: bool, r: bool) -> bool:
                return q and r

            def impl_and(p: bool, q: bool, r: bool) -> bool:
                return (not p) or inner_and(q, r)
            return [ant, q_label, r_label], '→', impl_and, ('∧', inner_and)

        # q ∨ r no consequent
        if ' ou ' in cons:
            q_label, r_label = [x.strip()
                                for x in cons.split(' ou ', maxsplit=1)]

            def inner_or(q: bool, r: bool) -> bool:
                return q or r

            def impl_or(p: bool, q: bool, r: bool) -> bool:
                return (not p) or inner_or(q, r)
            return [ant, q_label, r_label], '→', impl_or, ('∨', inner_or)

        # consequent simples
        def impl(p: bool, q: bool) -> bool:
            return (not p) or q
        return [ant, cons.strip()], '→', impl, None

    # Conjunção simples
    if ' e ' in s:
        a_label, b_label = [x.strip() for x in s.split(' e ', maxsplit=1)]

        def conj(p: bool, q: bool) -> bool:
            return p and q
        return [a_label, b_label], '∧', conj, None

    # Disjunção simples
    if ' ou ' in s:
        a_label, b_label = [x.strip() for x in s.split(' ou ', maxsplit=1)]

        def disj(p: bool, q: bool) -> bool:
            return p or q
        return [a_label, b_label], '∨', disj, None

    raise ValueError(f'Conectivo não suportado: {sentence!r}')


def generate_truth_table_df(sentence: str) -> pd.DataFrame:
    """Gera uma tabela-verdade para uma senten a l gica.

    :param sentence: Uma sentenca logica com conectivos  ,  ,  e  .
    :return: DataFrame com colunas para cada propriedade, e a ltima coluna
             com o resultado da avalia o da senten a l gica.
    """
    props, symbol, fn, inner = parse_sentence(sentence)
    n = len(props)
    rows: List[Dict[str, Any]] = []

    for vals in itertools.product([False, True], repeat=n):
        row: Dict[str, Any] = {props[i]: vals[i] for i in range(n)}

        # Se existe subexpressão interna, calcule e insira
        if inner:
            inner_symbol, inner_fn = inner
            # q = vals[1], r = vals[2]
            inner_val = inner_fn(vals[1], vals[2])
            row[inner_symbol] = inner_val
            # fn recebe p, q, r
            result = fn(vals[0], vals[1], vals[2])
        else:
            # fn recebe p, q
            result = fn(*vals)

        row[symbol] = result
        rows.append(row)

    return pd.DataFrame(rows)


def df_to_markdown(df: pd.DataFrame) -> str:
    """
    Converte um DataFrame em uma string Markdown representando uma tabela.

    :param df: O DataFrame a ser convertido.
    :return: Uma string Markdown representando a tabela.
    """
    headers = df.columns.tolist()
    md = "| " + " | ".join(headers) + " |\n"
    md += "| " + " | ".join("---" for _ in headers) + " |\n"
    for _, row in df.iterrows():
        md += "| " + " | ".join(str(row[h]) for h in headers) + " |\n"
    return md


def generate_markdown_document(
    sentences: List[str],
    filename: str
) -> Path:
    """
    Gera um documento Markdown com as tabelas-verdade das sentenças lógicas
    fornecidas.

    :param sentences: As sentenças lógicas a serem geradas.
    :param filename: O nome do arquivo a ser gerado.
    :return: O Path do arquivo gerado.
    """
    md = "# Tabelas-Verdade – Sentenças\n\n"
    for sent in sentences:
        df = generate_truth_table_df(sent)
        md += f"## {sent}\n\n"
        md += df_to_markdown(df) + "\n"

    out = Path(filename)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    return out


if __name__ == "__main__":
    sentencas = [
        "Eu estudei para a prova e fiz todos os exercícios",
        "Eu vou ao cinema ou fico em casa assistindo séries",
        "Se eu acordar cedo, então conseguirei pegar o ônibus",
        "Se eu estudar muito, então passarei na prova e ganharei um presente",
        "Eu vou jogar videogame ou vou estudar lógica de programação",
        "Eu comi pizza e tomei refrigerante",
        "Se eu tiver dinheiro, então viajarei nas férias",
        "Eu lerei um livro se e somente se terminar meu trabalho",
        "Se estiver sol, então irei à praia ou ao parque",
        "Eu farei um bolo se e somente se comprar os ingredientes",
        "Se eu concluir o trabalho a tempo, então serei recompensado com um bônus",
        "Eu vou terminar o projeto se e somente se conseguir ajuda do meu colega"
    ]
    output = generate_markdown_document(
        sentencas,
        "./n1/tabela_verdade.md"
    )
    print(f"Documento gerado em: {output}")
