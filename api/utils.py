def sortDicionario(dicionario):
    return dict(sorted(dicionario.items(), reverse=True, key = lambda item: item[1]))