"""
Roberto está organizando sua despensa e quer verificar se determinados itens 
já estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique 
se ele está na lista de itens disponíveis na despensa. Caso o item não esteja 
na lista, o programa deve informar que ele precisa ser comprado.

input:
- item (str): o item desejado pelo usuário.
output:
- "O item {item} já está na despensa." (se o item estiver na lista)
- "O item {item} não está na despensa. Você precisa comprá-lo." (se o item não estiver na lista)
"""

# Lista de itens disponíveis na despensa
itens_despensa = ["arroz", "feijão", "açúcar", "sal", "óleo", "macarrão"]
# Pergunta ao usuário qual item ele deseja verificar
item = input("Qual item você deseja verificar na despensa? ").strip().lower()
# Verifica se o item está na lista de itens disponíveis
if item in itens_despensa:
    print(f"O item {item} já está na despensa.")
else:
    print(f"O item {item} não está na despensa. Você precisa comprá-lo.")