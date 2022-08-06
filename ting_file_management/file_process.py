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
    if instance.is_empty():
        print("Não há elementos")

    else:
        first_file_processed = instance.dequeue()
        first_path_file = first_file_processed["nome_do_arquivo"]
        print(f"Arquivo {first_path_file} removido com sucesso")


def file_metadata(instance: Queue, position: int) -> None:
    if (position > len(instance) - 1):
        print("Posição inválida", file=sys.stderr)

    else:
        data = instance.search(position)
        print(data)
