"""
Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. 
Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.
Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um 
relatório com todos os produtos juntos?

input:
- estoque1 (tuple): uma tupla contendo os produtos do primeiro estoque.
- estoque2 (tuple): uma tupla contendo os produtos do segundo estoque.
output:
- estoque_unificado (tuple): uma tupla contendo todos os produtos dos dois estoques juntos.
"""
estoque1 = ("Produto A", "Produto B", "Produto C")
estoque2 = ("Produto D", "Produto E", "Produto F")
estoque_unificado = estoque1 + estoque2
print("Relatório de Estoque Unificado:")
for produto in estoque_unificado:
    print(produto)