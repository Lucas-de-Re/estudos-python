import os
import json

lista_tarefas = []

if os.path.exists("tarefas.json"):
    with open("tarefas.json", "r", encoding="utf-8") as f:
        lista_tarefas = json.load(f)

def salvar():
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(lista_tarefas, f, ensure_ascii=False, indent=2)

def iten(mensagem):
    return input(f'Que iten deseja {mensagem} \n')   

def menu():
    while True:
        try:
            opcoes = int(input( "1. Adicionar uma tarefa à lista.\n"
                                "2. Listar as tarefas.\n"
                                "3. Marcar uma tarefa como concluída.\n"
                                "4. Remover uma tarefa.\n" \
                                "5. Salvar.\n"
                                "6. Sair.\n"))
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
        lista_tarefas.append({"Tarefa" : texto, "Concluida":False})
        return(f"Tarefa {texto} foi adicionada")

def remover(texto):
    os.system('cls')
    lista_tarefas.pop(texto-1)
    return(f"Iten {texto} foi removido")

def concluido(texto):
    lista_tarefas[texto-1] ["Concluida"] = True
    return(f'Iten{texto} foi marcado como concluido')

def opcao_selecionada(opcao):
   match opcao:
        case 1: #adciona
            texto = iten('Adicionar').strip()
            resposta = adcionar_iten(texto)
            print(resposta)

        case 2: #mostra lista
            validar = lista_tarefas_zerada()
            if validar:
                os.system('cls')
                for i, t in enumerate(lista_tarefas, start=1):
                    marcador = "[X]" if t ["Concluida"] else "[ ]"
                    print(f"{i}. {marcador} {t['Tarefa']}")                
                input("Precisone qualquer tecla para continuar ...")
        case 3: #marcar concluido
            os.system('cls')
            validar = lista_tarefas_zerada()
            if validar:
                texto = int(iten("Marcar como concluido"))
                validar = valida_tamanho(texto)
                if not validar:
                    print(f"Não tem o iten {texto} na lista")
                else:
                    resposta = concluido(texto)
                    print(resposta)

        case 4: #remove
            os.system('cls')
            validar = lista_tarefas_zerada()
            if validar:
                texto = int(iten("remover"))
                validar = valida_tamanho(texto)   
                if not validar:
                    print(f"Não tem o iten {texto} na lista")
                else:
                    resposta = remover(texto)
                    print(resposta)

        case 5: #salva
           os.system('cls')
           salvar()
           print('** SALVO **')
               
while True:
    opcao = menu()
    if opcao == 6:
        os.system('cls')
        salvar()
        break
    elif opcao < 1 or opcao > 6:
        print(f"opção invalida {opcao}")
    opcao_selecionada(opcao)

