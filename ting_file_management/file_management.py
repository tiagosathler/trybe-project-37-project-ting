import sys


def txt_importer(path_file: str) -> list:
    """
    Importa o conteúdo de um arquivo de texto do tipo 'txt'.

    Entrada:
    --------
    path_file: str
        O caminho e o nome do arquivo

    Saída:
    -------
    file_content: list[str]
        Uma lista contendo cada linha do arquivo de texto
    """
    if not path_file.strip().lower().endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return None

    try:
        with open(path_file, 'r', encoding='utf8') as file:
            file_content = file.read()

    except FileNotFoundError:
        print(
            f"Arquivo {path_file} não encontrado",
            file=sys.stderr)

    else:
        return file_content.strip().split('\n')
