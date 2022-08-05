from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


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


def remove(instance: Queue) -> None:
    if not len(instance):
        print("Não há elementos", file=sys.stdout)

    else:
        instance.dequeue()
        print("Arquivo statics/arquivo_teste.txt removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
