"""
Uma escola está organizando os dados dos alunos para criar um relatório resumido. 
Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. 
Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:

Nome: João
Idade: 16
Nota final: 8.5

"""
class Aluno:
    def __init__(self, nome, idade, nota_final):
        self.nome = nome
        self.idade = idade
        self.nota_final = nota_final

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nNota final: {self.nota_final}"

operacao = True
alunos = []
while operacao:
    try:
        nome = input("Digite o nome do aluno (ou 'sair' para sair): ")
        if nome.lower() == 'sair':
            operacao = False
        else:
            idade = int(input("Digite a idade do aluno: "))
            nota_final = float(input("Digite a nota final do aluno: "))
            aluno = Aluno(nome, idade, nota_final)
            alunos.append(aluno)
    except ValueError:
        print("Por favor, insira um número válido.")
for aluno in alunos:
    print(aluno)
    print("-" * 20)