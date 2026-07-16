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
    total_gastos = 0
    for i, t in enumerate (armazenamento.controle_de_gastos, start=1):
        total_gastos += t['Valor']
        print(f"{i}. {t['Descrição']} - {t['Motivo']} - R$ {t['Valor']:.2f}")

    return(f"Total dos gastos foram: {total_gastos}")

def remover_gasto():
    while True:
        if  len(armazenamento.controle_de_gastos) == 0:
            print("lista zerada")
            break
        try:


            escolha = int(input("Que iten gostaria de remover \n"))
            if escolha < 1 or escolha > len( armazenamento.controle_de_gastos):
                print("Escolha inválida")
            else:
                armazenamento.controle_de_gastos.pop(escolha-1)
                return("Iten removido")
        except ValueError:
            print(f"Valor tem que ser númerico, o valor deve ser de 1 a {len(armazenamento.controle_de_gastos)}")
        
        