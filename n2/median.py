def verificar_aprovacao(notas) -> str:
    """
    Recebe uma lista de notas de provas, calcula a média simples
    e retorna uma mensagem indicando se o aluno foi aprovado ou não.
    A média mínima para aprovação é 7.
    """
    if not notas:
        raise ValueError("A lista de notas não pode ser vazia.")

    # Calcula a média simples
    media = sum(notas) / len(notas)

    # Verifica se atingiu a média mínima (7)
    if media >= 7:
        return f"Média: {media:.2f} - Aprovado"

    return f"Média: {media:.2f} - Reprovado"


# Exemplo de uso
if __name__ == "__main__":
    notas_exemplo = [8.5, 6.0, 7.0, 9.0, 9.5, 5.2, 6.8]
    resultado = verificar_aprovacao(notas_exemplo)
    print(resultado)
