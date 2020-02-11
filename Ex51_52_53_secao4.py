"""
Exercício 51
Escreva um programa que leia as coordenadas x e y de pontos R² e
calcule sua distância de origem(0,0).
"""
import math

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))
R = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
print("A distância entre dois pontos é: %s" % R)
"""
Exercício 52 
Três amigos jogaram na loteria. Caso eles ganhem, o prêmo dever ser repartido 
proporcionalmente ao valor que cada um deu para realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima 
quanto cada um ganharia do prêmio com base no valor investido.
"""
aposta1 = float(input("Digite a primeira aposta: "))
aposta2 = float(input("Digite a segunda aposta: "))
aposta3 = float(input("Digite a terceira aposta: "))
premio = float(input("Digite o valor do premio"))
totalapost = aposta1 + aposta2 + aposta3 #somando as apostas
#tirando a porcentagem
p1 = aposta1 / totalapost
p2 = aposta2 / totalapost
p3 = aposta3 / totalapost
#fazendo o calculo que cada um recebera
recebe1 = premio * p1
recebe2 = premio * p2
recebe3 = premio * p3

print("O valor ser rebido pelo o primeiro apostador é: %s" % recebe1)
print("O valor ser rebido pelo o segundo apostador é: %s" % recebe2)
print("O valor ser rebido pelo o terceiro apostador é: %s" % recebe3)
"""
Exercício 53
Faça um programa para ler as dimensões de um terreno(comprimento c e latgura l),
bem como o preço do metro de tela p. Imprima o custo para cercar este
mesmo terreno com tela.
"""
c = float(input("Digite o comprimento do terreno "))
L = float(input("Digite a largura  do terreno "))
valor = float(input("Digite o valor da tela: "))

m = c * L #metros quadrados do terreno 
p = m * valor
print("O valor total para fechar o terreno de tela é: %s" % p)


