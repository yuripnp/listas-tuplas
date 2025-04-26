"""
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação 
final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador 
precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a 
lista exibindo a nova classificação ao final?
input:
classificacao = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']
nome_errado = 'Carlos'
nome_correto = 'Carla'
output:
['Ana', 'Bruno', 'Carla', 'Daniela', 'Eduardo']
"""
classificacao = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']
# Solicita o nome errado e o nome correto
nome_errado = input("Digite o nome errado: ")
nome_correto = input("Digite o nome correto: ")
# Verifica se o nome errado está na lista
if nome_errado in classificacao:
    # Substitui o nome errado pelo nome correto
    indice = classificacao.index(nome_errado)
    classificacao[indice] = nome_correto
else:
    print(f"O nome {nome_errado} não está na lista de classificação.")
# Imprime a nova classificação
print(classificacao)
