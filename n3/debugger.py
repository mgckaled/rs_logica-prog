def calcular_media(notas) -> float:
    soma = sum(notas)
    media = soma / len(notas)
    return media


def classificar_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def processar_alunos(alunos):
    resultados = []
    for aluno in alunos:
        nome = aluno["nome"]
        notas = aluno["notas"]
        media = calcular_media(notas)
        classificacao = classificar_aluno(media)

        resultado = {
            "nome": nome,
            "notas": notas,
            "media": media,
            "classificacao": classificacao
        }

        resultados.append(resultado)

    return resultados


def imprimir_resultados(resultados) -> None:
    for resultado in resultados:
        print(
            f"{resultado['nome']}: Média = {resultado['media']:.2f}, Situação = {resultado['classificacao']}")


def main() -> None:
    alunos = [
        {"nome": "Alice", "notas": [8.5, 7.0, 9.0]},
        {"nome": "Bruno", "notas": [5.0, 6.0, 5.5]},
        {"nome": "Carla", "notas": [3.0, 4.5, 2.5]},
        {"nome": "Daniel", "notas": [10.0, 9.5, 9.0]}
    ]

    resultados = processar_alunos(alunos)
    imprimir_resultados(resultados)


if __name__ == "__main__":
    main()
