import os
def menu(opcao):
    if opcao == 1:
        return(somar(numero_um, numero_dois))
    elif opcao == 2: 
        return(subtrair(numero_um, numero_dois))
    elif opcao == 3:
        return(multiplicar(numero_um, numero_dois)) 
    elif opcao == 4:
        return(dividir(numero_um, numero_dois))
    else:
        return('Opcao invalida!')

def ler_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Isso não é um número")


def somar(numero_um, numero_dois):
    return(numero_um + numero_dois)

def subtrair(numero_um, numero_dois):
    return(numero_um - numero_dois)

def multiplicar(numero_um, numero_dois):
    return (numero_um * numero_dois)

def dividir(numero_um, numero_dois):
    try:
        return(numero_um / numero_dois)
    except ZeroDivisionError:
        return('Impossivel dividir por 0')


while True:
    os.system('cls')
    print('*'*60)
    print('CALCULADORA')
    print('*'*60)

    opcao = ler_numero("1. Somar \n2. Subtrair \n3. Multiplicar \n4. Dividir \n5. Sair\n")

    if opcao == 5:
        break

    numero_um = ler_numero('Número: ')
    numero_dois = ler_numero('Número: ')   
    resultado = menu(opcao)

    print(f'Resultado: {resultado}')
    input('...')
