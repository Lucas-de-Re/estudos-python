import armazenamento
import gastos
import opcoes
import os
#descrição, valor, categoria
load = armazenamento.inicializar_json()
print(load)
while True:
    os.system('cls')
    opcao_selecionada = opcoes.menu()
    opcoes.validador_de_opcoes(opcao_selecionada)