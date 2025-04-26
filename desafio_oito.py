"""
Paulo está criando uma lista de pedidos para a lanchonete. Ele já tem todos os pedidos, 
mas percebeu que o último foi inserido por engano e precisa removê-lo.

Diante deste problema, ajude Paulo criando um programa que automatize essa operação, 
permitindo listar os pedidos e remover o último item automaticamente.
input:
pedidos = ['Cachorro-quente', 'Batata frita', 'Refrigerante', 'Pizza']
output:
['Cachorro-quente', 'Batata frita', 'Refrigerante']
"""
pedidos = ['Cachorro-quente', 'Batata frita', 'Refrigerante', 'Pizza']
# Remove o último pedido da lista
pedidos.pop()
# Imprime a lista de pedidos atualizada
print(pedidos)