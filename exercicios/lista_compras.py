import os

lista_compras = []

def repetir_acao(acao, texto):
    while True:
        acao()
        while True:                                          # loop só pra validar a resposta
            resposta = input(f'Deseja {texto} mais itens? S/N\n').strip().upper()
            if resposta in ('S', 'N'):                       # resposta válida? sai do loop de validação
                break
            print('Opção inválida.')                         # senão, avisa e pergunta DE NOVO
        if resposta == 'N':                                  # agora sim decide: repete ou para
            break



def adicionar():
    os.system('cls')
    adicionar_iten = input('O que deseja adicionar a lista?\n').strip().upper()
    lista_compras.append(adicionar_iten)

def remover():
    if len(lista_compras) != 0:
        os.system('cls')
        remover_iten = input('Que iten gostaria de retirar da lista?\n').strip().upper()

        if remover_iten in lista_compras:
            lista_compras.remove(remover_iten)
            print('iten removido.')
        else:
            print('iten não localizado')

    else:
        print('Lista vazia')
        

def opcoes():
    os.system('cls')
    print('1. Adicionar itens a lista de compra\n' 
          '2. Excluir iten na lista de compra\n' 
          '3. Mostrar lista de compra\n' 
          '4. Finalizar lista de compra e mostrar\n')

while True:
    opcoes()
    escolha = int(input('Escolha a opção desejada: \n')) 

    if escolha == 1:
        repetir_acao(adicionar, 'inserir')

    elif escolha == 2:
        repetir_acao(remover, 'remover')
        
    elif escolha == 3:
        for i, iten in enumerate(lista_compras, start=1):
            print(f'{i}. {iten}')
        input('pressione uma tecla para continuar...')    

    elif escolha == 4:
        break

    else:
        print('opcao invalida')