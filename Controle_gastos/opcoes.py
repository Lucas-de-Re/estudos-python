import gastos
import armazenamento
def menu():
    while True:
        try:
            return(int(input("OPÇÕES\n\n"
                            "1. Inserir gasto\n" \
                            "2. Listar gasto\n" \
                            "3. Remover gasto\n" \
                            "4. Salvar\n" \
                            "5. Sair\n")))
        except ValueError:
            print("Opcao deve ser um número!")
def validador_de_opcoes(opcao_selecionada):
    if  opcao_selecionada == 1: #Adicionar
        mensagem = gastos.adicionar_gasto()
        print(mensagem)
        input("Precisone uma tecla para continuar....")
    elif opcao_selecionada == 2: #Mostrar
        mensagem = gastos.mostrar_gastos()
        print(mensagem)
        input("Precisone uma tecla para continuar....")
    elif opcao_selecionada == 3: #Remover
        mensagem = gastos.remover_gasto()
        print(mensagem)
        input("Precisone uma tecla para continuar....")
    elif opcao_selecionada == 4: #Salvar
        armazenamento.save()
        input("Precisone uma tecla para continuar....")
    else:
        print("Opção invalida")
        input("Precisone uma tecla para continuar....")


"""
import gastos
import armazenamento

PAUSA = "Pressione uma tecla para continuar..."
SAIR = 5

ACOES = {
    1:    ("Inserir gasto",  gastos.adicionar_gasto),
    2:    ("Listar gastos",  gastos.mostrar_gastos),
    3:    ("Remover gasto",  gastos.remover_gasto),
    4:    ("Salvar",         armazenamento.save),
    SAIR: ("Sair",           None),
}


def menu():
    #Mostra o menu e devolve uma opção válida
    print("OPÇÕES\n")
    for numero, (rotulo, _) in ACOES.items():
        print(f"{numero}. {rotulo}")

    while True:
        try:
            escolha = int(input("\nEscolha: "))
        except ValueError:
            print("A opção deve ser um número.")
            continue

        if escolha in ACOES:
            return escolha
        print("Opção inválida.")


def executar(opcao):
    #Executa a ação correspondente à opção
    _, acao = ACOES[opcao]
    mensagem = acao()
    if mensagem:
        print(mensagem)
    input(PAUSA)

"""