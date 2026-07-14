import gastos
def menu():
    while True:
        try:
            return(int(input("OPÇÕES"
                            "1. Inserir gasto\n" \
                            "2. Listar gasto\n" \
                            "3. Remover gasto\n" \
                            "4. Salvar\n" \
                            "5. Sair\n")))
        except ValueError:
            print("Opcao deve ser um número!")
def validador_de_opcoes(opcao_selecionada):
    while True:
        if   opcao_selecionada == 1:
            gastos.adicionar_gasto
            print("gasto adicionado")
        elif opcao_selecionada == 2:
            pass
        elif opcao_selecionada == 3:
            pass
        elif opcao_selecionada == 4:
            pass
        elif opcao_selecionada == 5:
            pass
        else:
            print("Opção invalida")