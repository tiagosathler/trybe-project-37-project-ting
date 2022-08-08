from ting_file_management.queue import Queue
from ting_file_management.file_process import process, remove, file_metadata
from ting_word_searches.word_search import exists_word, search_by_word


def add_file(queue: Queue) -> None:
    file_path = input("Digite o caminho e nome do arquivo: ")
    process(file_path, queue)


def remove_file(queue: Queue) -> None:
    remove(queue)


def get_file_content(queue: Queue) -> None:
    if not queue.is_empty():
        index = ""
        while not index.isdecimal():
            index = input("Digite a posição da Fila (inteiro positivo): ")
            file_metadata(queue, int(index, 10))
    else:
        print("A fila está vazia!")


def run_exists_word(queue: Queue) -> None:
    word = input("Digite a palavra a ser pesquisada na Fila: ")
    reports = exists_word(word, queue)
    if not reports:
        print(f"Palavra {word} não encontrda na Fila!")
    print(reports)


def run_search_by_word(queue: Queue) -> None:
    word = input("Digite a palavra a ser pesquisada na Fila: ")
    reports = search_by_word(word, queue)
    if not reports:
        print(f"Palavra {word} não encontrda na Fila!")
    print(reports)


def clear_all(queue: Queue) -> None:
    if not queue.is_empty():
        response = input("TEM CERTEZA? (s/n): ")
        if response.lower() == "s":
            queue.clear_all()
            print("A Fila está vazia!!!")
    else:
        print("A Fila já estava vazia!!!")


if __name__ == "__main__":
    options = {
        "1": add_file,
        "2": remove_file,
        "3": get_file_content,
        "4": run_exists_word,
        "5": run_search_by_word,
        "6": clear_all,
    }

    option = None

    files_in_queue = Queue()

    menu = (
        "Operações:\n"
        " 1: adicionar um arquivo à Fila\n"
        " 2: remover o primeiro arquivo da Fila\n"
        " 3: buscar os metadados de um arquivo da Fila\n"
        " 4: buscar por uma palavra na Fila\n"
        " 5: buscar por uma palavra na Fila e mostrar o conteúdo\n"
        " 6: limpar a Fila inteira\n"
        " 9: SAIR\n"
    )

    while option != "9":
        print(menu)
        option = input("Digite a opção: ")
        if option not in "1234569":
            print("Opção inválida!")
        elif option == "9":
            print("Bye!!!")
        else:
            options[option](files_in_queue)
            print("--------------")
