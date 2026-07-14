import armazenamento

def ler_gasto():    #1. Almoço - R$ 25.00 (comida)
    descricao = input("1. Descrição do gasto: \n")
    motivo = input("3. motivo do gasto\n")
    while True:
        try:
            valor = float(input("2. Valor do gasto\n"))
            break
        except ValueError:
            print("Precisa ser um valor em números>>>")
    return{"Descrição": descricao, "Motivo": motivo, "Valor": valor}


def adicionar_gasto():
    gasto = ler_gasto()
    armazenamento.controle_de_gastos.append(gasto)
    return("gasto adicionado\n")

def mostrar_gastos():
    for i, t in enumerate (armazenamento.controle_de_gastos, start=1):
        print(f"{i}. {t['Descrição']} - {t['Motivo']} - R$ {t['Valor']:.2f}")



"""for i, t in enumerate(lista_tarefas, start=1):
                    marcador = "[X]" if t ["Concluida"] else "[ ]"
                    print(f"{i}. {marcador} {t['Tarefa']}")   """     