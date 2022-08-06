from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file: str, instance: Queue) -> None:
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


def remove(instance: Queue) -> None:
    if not len(instance):
        print("Não há elementos")

    else:
        while (len(instance)):
            data = instance.dequeue()
            path_file = data["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance: Queue, position: int) -> None:
    if (position > len(instance) - 1):
        print("Posição inválida", file=sys.stderr)

    else:
        data = instance.search(position)
        print(data)
