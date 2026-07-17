letras = ["a", "b", "a", "c", "b", "a"]
contagem = {}
# monte: {'a': 3, 'b': 2, 'c': 1}

for i in letras:
    print(i)
    contagem [i] = contagem.get(i, 0) + 1
    print(contagem)
