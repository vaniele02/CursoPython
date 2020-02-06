"""
Exercício 11
Leia uma velocidade em m/s(metros por segundo) e apresente-se convertida em km/h
(quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade
em km/h e M em m/s
"""
m = float(input("Digiti uma velocidade em m/s:"))

k = m * 3.6

print("A velocidade em k/h é: %s" % k)

"""
Exercício 12
Leia a distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é: K = 1.61 * M, sendo K a distância em quilômetros e M em milhas
"""
m = float(input("Digiti uma distância em millhas:"))

k = 1.61 * m
print("A distância em quilômetros é: %s" % k)

"""
Exercício 13
Leia uma distância e quilômetros e apresente-a converitida em millhas. A fórmula de 
conversão é: M = k/1.61, sendo K a distância em quilômetros e M em millhas.
"""
k = float(input("Digiti uma distância em quilômetro:"))

m = k/1.61
print("A velocidade em milhas é: %s" % m)

"""
Exercício 14
Leia um ânglo em graus e apresente-o convertido em radianos. A fórmula de conversão 
é: R = G * PI/180, sendo G o ânglo em graus R em radianos e pi = 3.14. 
"""
g = float(input("Digiti um ângulo em graus:"))

r = g * 3.14/180
print("O valor do ângulo em Radianos é: %s" % r)

"""
Exercício 15
Leia um ângulo em radianos e apresente-o convertido em graus.A fórmula de conversão 
é: G = R *180/PI, sendo G o ângulo em graus e R em radianos e pi = 3.14.
"""
r = float(input("Digiti o ângulo em Radianos:"))

g = r * 180/3.14
print("O ângulo em Graus é: %s" % g)
