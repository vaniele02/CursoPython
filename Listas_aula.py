"""
Listas

Listas em Python funciona como vetores ou matrize, ou seja arrays com
adiferença de serem DINÂMICOS e também podemos colocar QUALQUER tipo de dados

 Linguagens C/Java: Arrays
        -Possuem tamanho e tipo de dados fixos;
        Ou seja, nestas linguagens  se você criar um array do tipo int com tamanho 5, este array
        será SEMPRE do tipo inteiro e poderá ter SEMPRE mo máximo 5 valores.

-Já em Python
-Dinâmocos: Não possui tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
-Qualquer tipo de dados: As listas não possuem tipo de dado fixo, ou seja podemos colocar qualquer tipo de dados;
-As listas em Python são representados em colchetes: [];

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['V', 'a', 'n', 'i', 'e', 'l', 'e']
lista3 = []
lista4 = list(range(11))
lista5 = list('Vaniele')

#Podemos checar se determinador valor esta na lista
#procurando dados dentro da lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num }')
else:
    print(f'Não encontrou o {num}!')

#Podemos ordernar a lista
lista1.sort()
print(lista1)

#podemos facilmente contar o número de ocorrencias de um valor em uma lista
#conta a quantidade que determinado dado se repete dentro da lista
print(lista1.count(1))
print(lista5.count('e'))

#adicionar elementos em listas
para adicionar elementos em listas utilizamos a função apend

OBS.: com append apenas adicionamos um elemento por vez
lista1.append(1,3,5,6)

print(lista1)
lista1.append(42)
print(lista1)

#podemos colocar uma lista dentro da outra, gerando uma única lista
#coloca a lista como elemento único, tornando uma sublista
lista1.append([1, 3, 89, 15, 'Boots'])
print(lista1)

#procurando uma lista dentro da outra lista
if [1, 3, 89, 15, 'Boots'] in lista1:
    print('Encontrei a lista!')
else:
    print('Não encontrei a lista!')

#faz a mesma coisa que o append, não aceita valor único, aceita apenas iteraveis(um conjunto
#de dados)
#adiciona um por um dentro da lista
lista1.extend([85, 56, 78, 45])
print(lista1)
lista1.extend("Geek")
print(lista1)

#Podemos inserir um novo elemento na lisa informando a posição do indice
#OBS.: Isso não substitui o valor inicial o mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo Valor')
print(lista1)

#Podemos facilmente juntar duas lista
#lista6 = lista1 + lista2
#print(lista6)
#lista1.extend(lista2)
#print(lista1)
lista1 = lista1 + lista2
print(lista1)

#podemos facilmente inverter uma lista usando o reverse
#forma1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
#forma 2
print(lista1[:: -1])#islice
print(lista2[:: -1])

#Copiar uma lista
lista6 = lista2.copy()
print(lista6)

#Tamanho de uma lista, podemos contar quantos elementos tem dentro da lista
print(len(lista4))

#podemos remover facilmente o ultimo elemento de uma lista
#OBS.: O pop nao so remove o ultimo elemento como também o retorna
print(lista5)
lista5.pop()
print(lista5)


#podemos remover um elemento pelo indice
#OBS.: os elementos a direita desse indice serao deslocados para a esquerda
#OBS.: se nao houver elemento no indice indicado teremos o INDEXERROR
lista5.pop(2)
print(lista5)

#podemos remover todos os elementos, ou seja, zera a lista
print(lista5)
lista5.clear()
print(lista5)

#podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

#podemos facilmente converter uma string para lista
#Exemplo 1:

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)
#OBS.: o split por padrao separa os elementos da lista de acordo com os espaços entre elas

#Exemplo 2:
curso = 'Programação, em, Python, Essencial'
print(curso)
curso = curso.split(',')
print(curso)

#convertendo uma lista em String
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

#Abaixo estamos falando: pega a lista 6, coloca espaço entre cada elemento e transforme em String
curso = ' '.join(lista6)
print(curso)

#Abaixo estamos falando: pega a lista 6, coloca $ entre cada elemento e transforme em String
curso = '$'.join(lista6)
print(curso)

#podemos realmente colocar qualquer tipo de dados, inclusive misturando os tipos de dados
lista6 = [1, 33.45, True, 'Python', [1, 2, 3], 123226587856261]
print(lista6)
print(type(lista6))

#iterando sobre lista
#Exemplo 1 - Utlizando for:

#imprimindo cada elemento da lista em linhas separadas
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
    print(soma)

#Exemplo 2: - Utilizando while:
carrinho = []
produto = ' '
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

#utilizando váriaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

#fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul
print(cores[3]) #branco

#fazemos acesso aos elementos de forma indexada inversa
#a lista funciona como um circulo, onde o final de um elemento esta ligado ao inicio da lista

print(cores[-1]) #branco
print(cores[-2]) #azul
print(cores[-3]) #amarelo
print(cores[-4]) #verde

#loop
i = 0

for cor in cores:
    print(cor)

while i <= len(cores):
    print(cores[i])
    i = i + 1

cores = ['verde', 'amarelo', 'azul', 'branco']

#gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

#listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(43)
lista.append(43)
lista.append(42)

print(lista)

#outros metodos nao tao importantes, mas tambem uteis
#por exemplo encontrar um indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

#em qual indice esta o valor 6
#quando há repetiçao de elemento na lista, retornara o primiero indice
print(numeros.index(6))

print(numeros.index(9))

#Obs.: caso nao tenha esse elemento na lista será apresentado erro ValueError

#podemos fazer buscas dentro de um range, ou seja, qual indice começa a busca
print(numeros.index(5, 1)) #buscando a partir do indice
print(numeros.index(5, 2))
#print(numeros.index(5, 4))
#OBS.: caso nao tenha esse elemento na lista será apresentado erro ValueError

#podemos fazer buscas dentro de um range incio e fim
print(numeros.index(8, 3, 6))  # buscar o indice do valor 8, entre os indices 6 à 8

#vamos revisar o slicing
#lista[inicio:fim:passo]
#range[inicio:fim:passo]

#trabalhando com slicing de lista com parametro 'ínicio'
lista = [1, 2, 3, 4]
print(lista[1:])  #iniciando no indice 1 e pegando todos os elementos restantes

#trabalhando com slicing de lista com parametro 'fim'
print(lista[:2])  #começa em 0 e pega ate o indice 2 - 1
print(lista[:4]) #começa em 0 e pega ate o indice 4 - 1
print(lista[1:3])

#trabalhando com slicing com parametro passo
print(lista[1::2])  #começa em 1, e vai ate o final, de 2 em 2
print(lista[::2])

#invertando valores em lista
nomes = ['geek', 'university']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['geek', 'university']
nomes.reverse()
print(nomes)
#realizar soma*, procurar valor maximo*, procurar valor minimo*, tamanho
#* se todos os valores forem inteiros ou reais
lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))   # soma
print(max(lista))   # maximo
print(min(lista))   # minimo valor
print(len(lista))   # tamanho da lista

#transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#desempacotamento de lista
lista = [1, 2, 3]
print(lista)

num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
#OBS.: se tivermos mais elementos para desempacotar do que variáveis para receber os valores,
# teremos ValueError, e ao contrário também da erro

#copiando uma lista para outra(Shallow Copy e Deep Copy)
#forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy() #copia
print(nova)
nova.append(4)
print(nova)

#veja que ao utilizamros lista.copy(), copiamos os dados da lista para uma nova lista, mas elas
#ficaram totalmente independentes, ou seja, modificando uma lista nao afeta a outra. Isso em Python
#é chamado de Deep Copy(cópia profunda)

#FOrma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista  #copia
print(nova)
nova.append(4)

print(lista)
print(nova)

#veja que utilizamos a cópia via atribuiçao e copiamos os dados da lista para a nova listas, mas
# após realizar modificaçao em umda das listas, essa modificação se refletiu em ambas as listas,
#Isso em Python é chamado de Shallow Copy

"""



