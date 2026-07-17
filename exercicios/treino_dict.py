import os
os.system('cls')
pessoa = {"Nome": "Lucas", "Idade": 30}
pessoa["Idade"] = 31
pessoa["Cidade"] = "Cafelândia"
precos = {"pão": 5, "Leite": 4}

print(precos.get("pão", 0))
print(precos.get("café", 0))
print(precos)
precos["café"]  = precos.get("café", 0) + 10
print(precos)


precos["pão"] = precos["pão"]+2
campo_idade = pessoa["Idade"]
print(pessoa["Nome"])
print(campo_idade)
print(precos["Leite"])
print(precos["pão"])
print(pessoa)


frutas = ["maçã", "banana", "maçã", "uva", "maçã"]
contagem = {}
for f in frutas:
    contagem[f] = contagem.get(f ,0)+1


    contagem[f] = contagem.get(f, 0) + 1
print(contagem)
print(contagem)


