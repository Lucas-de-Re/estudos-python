"""
Adicionar uma tarefa à lista.
Listar as tarefas, numeradas (lembra do enumerate?).
Marcar uma tarefa como concluída.
Remover uma tarefa.
Sair.
"""
import os

lista_tarefas = []

arquivo = "lista_de_tarefas.txt"
if os.path.exists("lista_de_tarefas.txt"):
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            lista_tarefas.append(linha.strip())


def iten(mensagem):
    return input(f'Que iten deseja {mensagem} \n')
    

def menu():
    while True:
        try:
            opcoes = int(input( "1. Adicionar uma tarefa à lista.\n"
                                "2. Listar as tarefas.\n"
                                "3. Marcar uma tarefa como concluída.\n"
                                "4. Remover uma tarefa.\n"
                                "5. Sair\n"))
            return opcoes
        except ValueError:
            print("Opção invalida! Precisa ser um número.")

def opcao_selecionada(opcao):
   match opcao:
        case 1:
            texto = iten('Adicionar').strip()
            if texto == "":
                print("Tarefa vazia?!")
            else:
                lista_tarefas.append('[ ]'+texto)
        case 2:
           for i, itens in enumerate(lista_tarefas, start=1):
               print(f"{i}. {itens}")
        case 3:
           texto = int(iten("Marcar como concluido"))
           if texto < 0 or texto > len(lista_tarefas):
               print(f"Não tem o iten {texto} na lista")
           else:
               lista_tarefas[texto-1] = "[X]" + lista_tarefas[texto-1][3:]
        case 4:
            texto = int(iten("Que iten gostaria de remover ?"))
            if texto < 0 or texto > len(lista_tarefas):
                print(f"Não tem o iten {texto} na lista")
            else:
               lista_tarefas.pop(texto-1)
               

def adcionar(iten):
    lista_tarefas.append(iten)

while True:
    opcao = menu()
    if opcao == 5:
        break
    elif opcao < 1 or opcao > 5:
        print(f"opção invalida {opcao}")
    opcao_selecionada(opcao)

with open("lista_de_tarefas.txt", "w", encoding="utf-8") as f:
    for i, nome in enumerate(lista_tarefas, start=1):
        f.write(f"{nome}\n")