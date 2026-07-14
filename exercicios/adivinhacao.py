import random

tentativas = 5
numero_secreto = random.randint(1, 100)

print('*' * 46)
print(f' Jogo do número secreto — você tem {tentativas} tentativas')
print('*' * 46)

while True:
    chute = int(input('Tente adivinhar o número, meu chapa: '))

    if chute == numero_secreto:
        print('Parabéns!! Acertou!')
        break

    tentativas -= 1
    if tentativas == 0:
        print(f'GAME OVER! O número era {numero_secreto}')
        break

    if numero_secreto > chute:
        print('Dica: Chuta um valor mais alto!')
    else:
        print('Dica: Chuta um valor mais baixo!')
    print(f'Você errou!! Ainda tem {tentativas} tentativas')