from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance: Queue) -> None:
    if (len(instance) > 0):
        for index in range(len(instance)):
            data = instance.search(index)
            if data["nome_do_arquivo"] == path_file:
                return None

    file_content = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }

    instance.enqueue(data)
    print(data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
