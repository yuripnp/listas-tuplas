"""
Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a 
ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. 
Camila quer adicionar novos nomes e organizá-los em posições específicas.
Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo 
nome em uma posição escolhida e exiba a lista atualizada?

input:
- lista_convidados (list): uma lista contendo os nomes dos convidados.
output:
- lista_convidados_atualizada (list): uma lista contendo os nomes dos convidados, 
  incluindo o novo nome na posição escolhida.
"""
# Lista inicial de convidados
lista_convidados = ["Ana", "Bruno", "Carlos", "Diana"]
lista_convidados_atualizada = []

for convidado in lista_convidados:
    print(f"Convidado: {convidado}, digite a posição que deseja adicionar o convidado.")
    posicao = int(input(f"Digite a posição (0 a {len(lista_convidados)}): "))
    # Verifica se a posição é válida
    if 0 <= posicao <= len(lista_convidados):
        # Adiciona o convidado na posição escolhida
        lista_convidados_atualizada.insert(posicao, convidado)
    else:
        print("Posição inválida. O convidado não foi adicionado.")
# Exibe a lista atualizada
print("Lista de convidados atualizada:")
for convidado in lista_convidados_atualizada:
    print(convidado)
