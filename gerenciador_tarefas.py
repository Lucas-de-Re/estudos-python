"""
Adicionar uma tarefa à lista.
Listar as tarefas, numeradas (lembra do enumerate?).
Marcar uma tarefa como concluída.
Remover uma tarefa.
Sair.
"""
#import os

def menu():
    while True:
        try:
            opcoes = int(input("1. Adicionar uma tarefa à lista.\n"
                                "2. Listar as tarefas.\n"
                                "3. Marcar uma tarefa como concluída."
                                "4. Remover uma tarefa.\n"
                                "5. Sair\n"))
            return opcoes
        except ValueError:
            print("Opção invalida! Precisa ser um número.")

def opcao_selecionada(opcao):
    if opcao == 1:
        print('Adicionar') 
    elif opcao == 2:
        print('Listar')
    elif opcao == 3:
        print('Marcar') 
    elif opcao == 4:
        print('Remover')
    elif opcao == 5:
        print('Sair') 
    else:
        print('Opcao invalida!') 

while True:
    opcao = menu()
    if opcao == 5:
        break
    opcao_selecionada(opcao)
