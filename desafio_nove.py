"""
A professora Helena quer facilitar sua rotina na hora de calcular a média das notas 
finais da turma. Ela sempre anota as notas dos alunos ao longo do semestre e, no final, 
precisa de um relatório para saber se a turma está indo bem.

Para isso, ajude a professora a criar um programa que receba as notas finais de todos os 
alunos e calcule a média da turma.

input:
notas = [7.5, 8.0, 6.5, 9.0, 7.0]
output:
A média da turma é: 7.6
"""
notas = []
operacao = True
media = 0
while operacao:
    try:
        nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
        if nota == -1:
            operacao = False
        else:
            notas.append(nota)
    except ValueError:
        print("Por favor, insira um número válido.")

for nota in notas:
    media += nota
media = media / len(notas)
print(f"A média da turma é: {media:.1f}")