import sys


def txt_importer(path_file):
    try:
        if '.txt' not in path_file:
            return print('Formato inválido', file=sys.stderr)
        with open(path_file) as file:
            data = file.read()
            text_file = [line for line in data.split('\n')]
            print(text_file)
            return text_file
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
