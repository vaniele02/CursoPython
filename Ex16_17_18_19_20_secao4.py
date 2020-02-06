"""
Exercício 16
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P *2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""
p = float(input("Digite um valor de comprimento em polegadas:"))

c = p * 2.54
print("O valor do comprimento em centímetros é: %s" % c)

"""
Exercício 17
Lei um valor de comprimento em centímentros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C/2.54, sendo C o comprrimento em centímetros e P o 
comprimento em polegadas.
"""
c = float(input("Digite um valor de comprimento em centímetros:"))

p = c / 2.54
print("O valor do comprimento em polegadas é: %s" % p)

"""
Exercício 18 
Leia um valor de volume em metros cúbicos e apresnete-o convertido em litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume 
em metros cúbicos.
"""
m = float(input("Digite valor do volume em metros cúbicos:"))
L = 1000 * m
print("O valor do volume em litros é: %s" % L)

"""
Exercício 19 
Leia um valor em litros e aprensete-o em metros cúbicos e apresente-o convertido em litros.
A fórmula de conversão é: M = L/1000, sendo L o volume me litrso e M o volume em 
metros cúbicos.
"""
L = float(input("Digite valor do volume em litros:"))
m = L / 1000
print("O valor do volume em metros cúbicos é: %s" % m)
"""
Exercício 20
Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K /0.45, sendo K a massa em quilogrmas e L 
a massa em libras.
"""
k = float(input("Digite o valor da massa em quilogramas:"))
L = k / 0.45
print("O valor da massa em libras é: %s" % L)
