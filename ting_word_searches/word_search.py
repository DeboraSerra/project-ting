def exists_word(word, instance):
    list = []
    length = len(instance)
    for index in range(length):
        data = instance.search(index)
        lines = data['linhas_do_arquivo']
        occurrences = []
        for index in range(len(lines)):
            if word.lower() in lines[index].lower():
                occurrences.append(index + 1)
        if len(occurrences):
            list.append({
                "palavra": word,
                "arquivo": data['nome_do_arquivo'],
                "ocorrencias": [{"linha": line} for line in occurrences]
            })
    return list


def search_by_word(word, instance):
    list = []
    length = len(instance)
    for index in range(length):
        data = instance.search(index)
        lines = data['linhas_do_arquivo']
        occurrences = []
        for index in range(len(lines)):
            if word.lower() in lines[index].lower():
                occurrences.append({
                    "linha": index + 1,
                    "conteudo": lines[index]
                })
        if len(occurrences):
            list.append({
                "palavra": word,
                "arquivo": data['nome_do_arquivo'],
                "ocorrencias": occurrences
            })
    return list
