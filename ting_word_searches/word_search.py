from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    response = search_by_word(word, instance)
    if len(response):
        response = [{
            "palavra": element["palavra"],
            "arquivo": element["arquivo"],
            "ocorrencias": [{
                "linha": occurrence["linha"]
            } for occurrence in element["ocorrencias"]]
        } for element in response]
    return response


def search_by_word(word: str, instance: Queue) -> list:
    result = []
    for index in range(len(instance)):
        occurrences = []
        meta_data = instance.search(index)
        for line, line_content in enumerate(meta_data["linhas_do_arquivo"]):
            if (word.lower() in line_content.lower()):
                occurrence = {
                    "linha": line + 1,
                    "conteudo": line_content
                }
                occurrences.append(occurrence)
        if len(occurrences):
            data = {
                "palavra": word,
                "arquivo": meta_data["nome_do_arquivo"],
                "ocorrencias": occurrences,
            }
            result.append(data)

    return result
