from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue) -> list:
    """
    Pesquisa uma string dada por 'word' nos dicionários da Fila,
    retornando uma lista com os relatórios da busca.
    Cada elemento desta lista é um dicionário contendo
    as informações da busca.

    Entradas:
    ---------
    word: str
        Palavra a ser pesquisada (caso insensitivo)

    instance: Queue
        Instância da classe Queue (Fila).

    Saída:
    ------
    response: list[dict]

        A lista com o(s) relatório(s) da busca, sendo este(s) dicionário(s),
        contendo: 'palavra' buscada, 'arquivo' correspondente à busca
        e a lista 'ocorrencias' contendo o(s) número(s) da 'linha' encontrada
        no texto.
    """
    response = search_by_word(word, instance)

    if len(response):
        response = [
            {
                "palavra": element["palavra"],
                "arquivo": element["arquivo"],
                "ocorrencias": [
                    {"linha": occurrence["linha"]}
                    for occurrence in element["ocorrencias"]
                ],
            }
            for element in response
        ]

    return response


def search_by_word(word: str, instance: Queue) -> list:
    """
    Pesquisa uma string dada por 'word' nos dicionários da Fila,
    retornando uma lista com os relatórios da busca.
    Cada elemento desta lista é um dicionário contendo
    as informações da busca.

    Entradas:
    ---------
    word: str
        Palavra a ser pesquisada (caso insensitivo)

    instance: Queue
        Instância da classe Queue (Fila).

    Saída:
    ------
    response: list[dict]

        A lista com o(s) relatório(s) da busca, sendo este(s) dicionário(s),
        contendo: 'palavra' buscada, 'arquivo' correspondente à busca
        e a lista 'ocorrencias' contendo o(s) 'conteudo' da(s) linha(s) e
        o(s) número(s) da 'linha' no texto.
    """
    result = []
    copied_instance = instance.copy()

    while not copied_instance.is_empty():
        occurrences = []
        meta_data = copied_instance.dequeue()

        for line, line_content in enumerate(meta_data["linhas_do_arquivo"]):
            if word.lower() in line_content.lower():
                occurrence = {"linha": line + 1, "conteudo": line_content}
                occurrences.append(occurrence)

        if len(occurrences):
            data = {
                "palavra": word,
                "arquivo": meta_data["nome_do_arquivo"],
                "ocorrencias": occurrences,
            }
            result.append(data)

    return result
