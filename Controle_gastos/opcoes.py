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
    """Mostra o menu e devolve uma opção válida."""
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
    """Executa a ação correspondente à opção."""
    _, acao = ACOES[opcao]
    mensagem = acao()
    if mensagem:
        print(mensagem)
    input(PAUSA)