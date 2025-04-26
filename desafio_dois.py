"""
Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas 
dos participantes para definir a ordem de premiação. Para garantir transparência, as notas 
precisam ser classificadas em ordem crescente, do menor para o maior valor.

Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as 
notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

input:
- notas (list): uma lista contendo as notas dos participantes do concurso de redação.
output:
- lista ordenada em ordem crescente.
"""

notas = [7.5, 8.0, 6.5, 9.0, 8.5, 7.0]
# Ordenando a lista de notas em ordem crescente
notas.sort()
# Exibindo a lista ordenada
print("Notas em ordem crescente:")
for nota in notas:
    print(nota)
