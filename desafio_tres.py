"""
Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa 
registrar os nomes dos voluntários que vão ajudar na ação. À medida que os voluntários 
se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra 
sair o programa deve encerrar.

Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

input:
- voluntarios (list): uma lista contendo os nomes dos voluntários que se inscreveram.
output:
- lista de voluntários inscritos.
"""

operacao = True
voluntarios = []
while operacao:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ").strip()
    if nome.lower() == "sair":
        operacao = False
    else:
        voluntarios.append(nome)
print("Lista de voluntários inscritos:")
for voluntario in voluntarios:
    print(voluntario)
