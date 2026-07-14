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
    while True:
        if   opcao_selecionada == 1:
            mensagem = gastos.adicionar_gasto()
            print(mensagem)
            break
        elif opcao_selecionada == 2:
            mensagem = gastos.mostrar_gastos()
            input("Precisone uma tecla para continuar....")
            break
        elif opcao_selecionada == 3:
            pass
        elif opcao_selecionada == 4:
            armazenamento.save()
            break
        elif opcao_selecionada == 5:
            pass
        else:
            print("Opção invalida")