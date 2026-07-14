#Pergunta o ano de nascimento e calcula a idade (reaproveite o que você já sabe — e dessa vez, nomes honestos! 

nome = input('Nome: ')
ano_nascimento = input('Ano nascimento: ')
cidade = input('Cidade: ')
ano_nascimento = int(ano_nascimento)

idade = 2026 - ano_nascimento

print(f'{nome} mora em {cidade} e tem {idade} anos.')

#Usando if/elif/else, classifica e imprime a categoria: #menos de 12 → "criança" 12 a 17 → "adolescente" 18 a 59 → "adulto" 60 ou mais → "idoso"
#Bônus (se quiser desafio): pergunte também se a pessoa tem habilitação (input) e, usando and, diga "Pode dirigir" só se ela for adulta e tiver habilitação.

if idade >= 18:
    habilitacao = input('Tem habilitação? S/N ').strip().upper()
    pode_dirigir = habilitacao[0]
    while pode_dirigir not in ('S', 'N'):
        print('sim ou nao apenas')
        habilitacao = input('Tem habilitação? S/N ').strip().upper()
        pode_dirigir = habilitacao[0]

if idade < 12:
    print('criança')
elif idade <= 17:
    print('adolescente')
elif idade <=59:
    print('adulto')

if idade >= 18 and pode_dirigir == 'S':
    print("Pode dirigir.")
elif idade >= 18:
    print("Não pode dirigir, pois não possui carteira.")
    