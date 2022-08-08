from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file: str, instance: Queue) -> None:
    """
    Processa o conteúdo de um arquivo de texto, gerando
    metadados em um dicionário e o enfileira na Fila

    Metadados: dict
        {
            "nome_do_arquivo": path_file,

            "qtd_linhas": <quantidade de linhas do texto: int>,

            "linhas_do_arquivo": <linhas do texto: list[str]>
        }

    Entradas:
    ---------
    path_file: str
        Caminho e nome do arquivo de texto (txt).

    instance: Queue
        Instância da classe Queue (Fila).

    Saída:
    ------
    sys.stdout: str
        Print do dicionário com os metadados na saída padrão do sistema.
    """
    for index in range(len(instance)):
        data = instance.search(index)
        if data["nome_do_arquivo"] == path_file:
            return None

    file_content = txt_importer(path_file)

    if file_content:
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_content),
            "linhas_do_arquivo": file_content,
        }

        instance.enqueue(data)
        print(data)


def remove(instance: Queue) -> None:
    """
    Remove o primeiro dicionário da Fila, desenfileirando-a.

    Entrada:
    --------
    instance: Queue
        Instância da classe Queue (Fila).

    Saída:
    ------
    sys.stdout: str
        Print do caminho e nome do arquivo removido da Fila
    """
    if instance.is_empty():
        print("Não há elementos")

    else:
        first_file_processed = instance.dequeue()
        first_path_file = first_file_processed["nome_do_arquivo"]
        print(f"Arquivo {first_path_file} removido com sucesso")


def file_metadata(instance: Queue, position: int) -> None:
    """
    Faz o print do dicionário na posição 'position' da Fila,
    caso exista.

    Entradas:
    ---------
    instance: Queue
        Instância da classe Queue (Fila).

    position: int
        Posição do dicionário.

    Saída:
    ------
    sys.stdout: str
        Print do dicionário encontrado na Fila
    """
    try:
        data = instance.search(position)

    except IndexError:
        print("Posição inválida", file=sys.stderr)

    else:
        print(data)
