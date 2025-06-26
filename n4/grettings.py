def saudacao(nome) -> str:
    """
    Gera uma saudação personalizada com um nome.

    Parâmetros:
    nome (str): Nome da pessoa.

    Retorna:
    str: Mensagem de saudação.
    """
    return f"Olá, {nome}!"


def outra_funcao() -> None:
    print('oi')


print(saudacao('Jão'))
