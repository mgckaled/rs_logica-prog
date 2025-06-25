import random


def get_user_input(prompts):
    """
    Solicita ao usuário as palavras necessárias para o MadLib.

    :param prompts: dicionário com chaves de placeholder e descrições de prompt
    :return: dicionário com chave=placeholder, valor=entrada do usuário
    """
    inputs = {}
    for key, description in prompts.items():
        user_response = input(f"Por favor, insira {description}: ")
        inputs[key] = user_response
    return inputs


def choose_template(templates):
    """
    Seleciona aleatoriamente um template de MadLib.

    :param templates: lista de dicionários com 'text' e 'prompts'
    :return: template selecionado
    """
    return random.choice(templates)


def run_madlib():
    # Definição de templates complexos
    """
    Executa o MadLib com um template escolhido aleatoriamente.

    1. Define templates complexos com placeholders para inputs do usuário;
    2. escolhe um template aleatoriamente;
    3. solicita ao usuário as palavras necessárias para o MadLib;
    4. imprime o MadLib final com as palavras escolhidas pelo usuário.

    :return: None
    """
    templates = [
        {
            "text": (
                "Numa manhã de {season}, eu acordei {adverb} e fui direto para a/o {place}. "
                "Lá, encontrei um(a) {adjective1} {animal} que parecia "
                "{verb1} sem parar. Foi tão {adjective2} que eu quase "
                "{verb2} de emoção. Mas então, um(a) {profession} apareceu e ofereceu-me "
                "{number} {noun_plural} para acalmar a situação."
            ),
            "prompts": {
                "season": "uma estação do ano (ex: primavera)",
                "adverb": "um advérbio (ex: rapidamente)",
                "place": "um local (ex: parque)",
                "adjective1": "um adjetivo (ex: curioso)",
                "animal": "um animal (ex: papagaio)",
                "verb1": "um verbo no gerúndio (ex: pulando)",
                "adjective2": "outro adjetivo (ex: surpreendente)",
                "verb2": "um verbo no passado na primeira pessoa (ex: chorei)",
                "profession": "uma profissão (ex: médico)",
                "number": "um número (ex: 7)",
                "noun_plural": "um substantivo no plural (ex: balões)"
            }
        },
        {
            "text": (
                "O(a) {celebrity} estava {verb1} no meio de "
                "{noun_plural1} quando decidiu {verb2} com um(a) {adjective} amigo(a). "
                "Eles planejaram uma viagem para {place} e levaram {number} {noun_plural2}, "
                "incluindo um(a) {item} {adverb}. No final, {celebrity} disse: \"{quote}\""
            ),
            "prompts": {
                "celebrity": "o nome de uma celebridade (ex: Emma Watson)",
                "verb1": "um verbo no gerúndio (ex: correndo)",
                "noun_plural1": "substantivo no plural (ex: pirâmides)",
                "verb2": "um verbo no infinitivo (ex: dançar)",
                "adjective": "um adjetivo (ex: aventureiro)",
                "place": "um destino de viagem (ex: ilha tropical)",
                "number": "um número (ex: 3)",
                "noun_plural2": "substantivo no plural (ex: mochilas)",
                "item": "um objeto (ex: guarda-chuva)",
                "adverb": "um advérbio (ex: cuidadosamente)",
                "quote": "uma citação curta (ex: Vamos nessa!)"
            }
        }
    ]

    # Escolha de template
    template = choose_template(templates)
    # Coleta de entradas do usuário
    user_inputs = get_user_input(template['prompts'])
    # Impressão do MadLib final
    story = template['text'].format(**user_inputs)
    print("\nSua história MadLib:")
    print(story)


if __name__ == '__main__':
    run_madlib()
