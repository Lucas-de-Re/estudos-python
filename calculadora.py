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

def somar(numero_um, numero_dois):
    return(numero_um + numero_dois)

def subtrair(numero_um, numero_dois):
    return(numero_um - numero_dois)

def multiplicar(numero_um, numero_dois):
    return (numero_um * numero_dois)

def dividir(numero_um, numero_dois):
    if numero_dois == 0:
        return('Impossivel dividir por 0')
    return float(numero_um / numero_dois)

while True:
    os.system('cls')
    print('*'*60)
    print('CALCULADORA')
    print('*'*60)

    opcao = int(input('1. Somar \n2. Subtrair \n3. Multiplicar \n4. Dividir \n5. Sair\n'))
    numero_um = int(input('Número: '))
    numero_dois = int(input('Número: '))

    if opcao == 5:
        break

    resultado = menu(opcao)
    print(f'Resultado: {resultado}')
    input('...')
