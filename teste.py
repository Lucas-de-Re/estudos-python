import json

with open("teste.json", "r", encoding="utf-8") as f:
    teste = json.load(f)

print(teste)         # a lista de dicionários volta INTEIRA
print(teste[0]["texto"])   # estudar