abc = {'Marcus':200, 'Pedro':800, 'Glauco':600}
abc_ordenado = dict(sorted(abc.items(), reverse=True, key = lambda item: item[1])) 
print(abc_ordenado)