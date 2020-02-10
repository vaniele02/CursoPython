"""
Exercíco 31
Leia um número inteiro e imprima o seu antecessor e seu sucessor.
"""
import math

a = float(input("Digite um valor: "))
b = a - 1 #antecessor
c = a + 1 #sucessor
print("Seu antecessor é: %s" % b, "Seu sucessor é: %s" % c)

"""
Exercício 32
Leia um número inteiro e imprima a soma do sucessor de seu triplo com antecessor de 
seu dobro.
"""
a = float(input("Digie um valor:"))
b = (a * 3 + 1)
c = (a * 2 - 1)
total = b + c
print("A soma do valor é: %s" % total)

"""
Exercício 33
Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
"""
L = float(input("Digit um lado do quadrado: "))
A = L * L
print("A área do quadrado é: %scm²" % A)

"""
Exercício 34 
Leia o valor do raio de um cículo e calcule e imprima a área do círculo correspondente.
A área do círculo é pi * raio², consider pi = 3.141592.
"""
r = float(input("Digiti um valor do raio de um circulo: "))
a = 3.141592 * (r*2)
print("Área do circulo é: %s" % a)

"""
Exercício 35 
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz quadrada a² + b². Faça um programa que receba os valores a e b
e calcule o valor da hipotenusa da equação. Imprima o resultado dessa operação.
"""
a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
h = math.sqrt((a * a) + (b + b))
print("O valor da hipotenusa é: %s" %h)
