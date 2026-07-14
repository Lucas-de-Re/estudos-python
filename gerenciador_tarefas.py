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
                                "4. Remover uma tarefa.\n" \
                                "5. Salvar TXT.\n"
                                "6. Sair\n"))
            return opcoes
        except ValueError:
            print("Opção invalida! Precisa ser um número.")

def lista_tarefas_zerada():
    if len(lista_tarefas) == 0:
        print("*** LISTA DE TAREFAS ZERADAS ***")
        return False
    else:
        return True

    
def valida_tamanho(texto):
    if texto < 1 or texto > len(lista_tarefas):
        os.system('cls')
        return(False)
    else:
        return(True)

def adcionar_iten(texto):
    if texto == "":
        os.system('cls')
        return("Tarefa vazia?!")
    else:
        os.system('cls')
        lista_tarefas.append('[ ]'+texto)
        return(f"Tarefa {texto} foi adicionada")

def remover(texto):
    os.system('cls')
    lista_tarefas.pop(texto-1)
    return(f"Iten {texto} foi removido")

def concluido(texto):
    lista_tarefas[texto-1] = "[X]" + lista_tarefas[texto-1][3:]
    return(f'Iten{texto} foi marcado como concluido')

def opcao_selecionada(opcao):
   match opcao:
        case 1:
            texto = iten('Adicionar').strip()
            resposta = adcionar_iten(texto)
            print(resposta)

        case 2:
            validar = lista_tarefas_zerada()
            if validar:
                for i, itens in enumerate(lista_tarefas, start=1):
                    print(f"{i}. {itens}")                

        case 3:
            validar = lista_tarefas_zerada()
            if validar:
                texto = int(iten("Marcar como concluido"))
                validar = valida_tamanho(texto)
                if not validar:
                    print(f"Não tem o iten {texto} na lista")
                elif validar:
                    resposta = concluido(texto)
                    print(resposta)

        case 4:
            validar = lista_tarefas_zerada()
            if validar:
                texto = int(iten("remover?"))
                validar = valida_tamanho(texto)   
                if not validar:
                    print(f"Não tem o iten {texto} na lista")
                elif validar:
                    resposta = remover(texto)
                    print(resposta)

        case 5:
           os.system('cls')
           salvar_txt()
           print('** TXT SALVO **')
               

def adcionar(iten):
    lista_tarefas.append(iten)

def salvar_txt():
    with open("lista_de_tarefas.txt", "w", encoding="utf-8") as f:
        for nome in lista_tarefas:
            f.write(f"{nome}\n")

while True:
    opcao = menu()
    if opcao == 6:
        os.system('cls')
        salvar_txt()
        break
    elif opcao < 1 or opcao > 6:
        print(f"opção invalida {opcao}")
    opcao_selecionada(opcao)

