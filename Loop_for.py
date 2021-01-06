"""
Loop for
Loop: estrutura de repetição
For: é uma delas

for iten in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis
Exemplos de iteráveis:
-String:
   nome = 'Geek University'
-Lista
    Lista = {1,2,3,5,7,9}
-RAnge
   numeros = range(1,10)
#exemplo de for 1(Iterando em um String)
for letra in nomes:
    print(letra)

#exemplo de for 2(Iterando em uma lista
for numero in lista:
    print(numero)

#Exemplo de for 3(Iterando sobre um range)
#Obs: o valor final não é inclusive
#range (valor_inicial, valor_final)
for numero in range(1, 10):
    print(numero)
"""

"""
Enumerate:
Gera um tupla
{(0 ,'G'), (1, 'e'),...}

for i, v in enumerate(nomes):
    print(nomes[i])

for indice, letra in enumerate(nomes):
    print(letra)
for _, letra in enumerate(nomes): 
    print(letra)
#quando não precisamos de um valor, podemose usar _ descartar um valor     


nomes = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #temos que transformar em uma lista

for valor in enumerate(nomes):
    print(valor)

qtd = int(input("Quantas vezes esse loop deve rodar?"))
soma = 0
for n in range (1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd}'))
    soma = soma + num
    #print(f'Imprimindo {n}')
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')
    
Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

#Original U + 1F60C
#Modificado: U0001F60C

for x in range(3):
    for num in range(1, 10):
        print('\U0001F622' * num)
