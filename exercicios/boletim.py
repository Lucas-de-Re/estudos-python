notas_aluno = []
notas_maior = []

maior_nota = 0
quantidade_notas = int(input('Quantas notas o aluno tem \n' \
                             ''))
for i in range(quantidade_notas):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    notas_aluno.append(nota)


media_nota = sum(notas_aluno) / len(notas_aluno)

print(f'Maior nota {max(notas_aluno)} \nMenor nota {min(notas_aluno)}' )

for i in notas_aluno:
    if i > maior_nota:
        maior_nota = i
    if i >= 70:
        notas_maior.append(i)

print(f'ficaram {len(notas_maior)} notas acima da média das notas do aluno')

if media_nota >= 70:
    print(f'Aprovado media final {media_nota}')
else:
    print(f'Reprovado {media_nota}')

print(maior_nota)

