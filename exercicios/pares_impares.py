lista_numero = []
lista_impar  = []
lista_par    = []


while True:
    valor = input('informe um valor ou digite sair: ').strip().lower()

    if valor == "sair":
        break

    numero = int(valor)
    lista_numero.append(numero)

for i in lista_numero:

    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(f'A lista dos número {lista_numero},\n'
      f'Tem esses números que são pares {lista_par}\n'
      f'E esses impares {lista_impar}')