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
    return {"Descricao": descricao, "Motivo": motivo, "Valor": valor}


def adicionar_gasto():
    gasto = ler_gasto()
    armazenamento.controle_de_gastos.append(gasto)

def mostrar_gastos():
    pass