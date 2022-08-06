import sys


def txt_importer(path_file: str) -> list:
    if "txt" not in path_file.lower():
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
