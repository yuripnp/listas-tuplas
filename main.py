lista = [1, 2, 3, 4, 5]
lista_mista = [1, "a", 3.14, True]
tupla = (1, 2, 3, 4, 5) # tupla é imutável
# tupla_mista é uma tupla com diferentes tipos de dados
tupla_mista = (1, "a", 3.14, True)

print(lista)
print(tupla)
print(lista[0])
print(tupla[0])

# slice
print(lista[0:2]) # [1, 2]
print(tupla[0:2]) # (1, 2)


print( 20 in lista)
print( 20 in tupla)

# Adicionando elementos
lista.append(6)
print(lista) # [1, 2, 3, 4, 5, 6]
lista.insert(0, 0)
print(lista) # [0, 1, 2, 3, 4, 5, 6]
# Removendo elementos
lista.remove(0)
print(lista) # [1, 2, 3, 4, 5, 6]
# Removendo o último elemento
lista.pop()
print(lista) # [1, 2, 3, 4, 5]
# Removendo o primeiro elemento
lista.pop(0)
print(lista) # [2, 3, 4, 5]
# Removendo todos os elementos
lista.clear()
print(lista) # []
# Adicionando elementos
lista.extend([1, 2, 3])
print(lista) # [1, 2, 3]
# ordenando a lista
lista.sort()
print(lista) # [1, 2, 3]
# Revertendo a lista
lista.reverse()
print(lista) # [3, 2, 1]

tuplaUm = (1, 2, 3)
tuplaDois = (4, 5, 6)
tuplaTres = tuplaUm + tuplaDois
print(tuplaTres) # (1, 2, 3, 4, 5, 6)
# Repetindo a tupla
tuplaQuatro = tuplaUm * 3
print(tuplaQuatro) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# Contando elementos
print(tuplaQuatro.count(1)) # 3

a, b, c = tuplaUm
print(a) # 1
print(b) # 2
print(c) # 3

