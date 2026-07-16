import armazenamento
import opcoes
import os
#descrição, valor, categoria
while True:
    os.system('cls')
    opcao_selecionada = opcoes.menu()
    if opcao_selecionada == 5:
        armazenamento.save()
        break
    opcoes.executar(opcao_selecionada)