from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    current_path = None
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            current_path = instance.search(index)
    if current_path is None:
        data = txt_importer(path_file)
        lines = len(data)
        item = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': lines,
            'linhas_do_arquivo': data
        }
        instance.enqueue(item)
        sys.stdout.write(f"{item}")


def remove(instance):
    if not len(instance):
        sys.stdout.write('Não há elementos\n')
        return
    first_item = instance.dequeue()
    print(first_item)
    path_file = first_item['nome_do_arquivo']
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(f"{instance.search(position)}")
    except IndexError:
        sys.stderr.write('Posição inválida\n')
