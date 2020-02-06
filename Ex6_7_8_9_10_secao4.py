"""
Exercício 6
Leia uma temperatura em graus Ceslsius e aprenseta-a convertida em graus Fahrenheit.
A fórmula de conversão é: F =C*(9.0/5.0)+32, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""
c = float(input("Digite uma temperatura em Celsius: "))
print(c)

f = c*(9.0/5.0)+32
print("A temperatura em Fahrenheit é: %s" % f)

"""
Exercício 7
Leia uma temperatura em graus Fahrenheit e aprenseta-a convertida em graus Celsius.
A fórmula de conversão é: C =5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.
"""
f = float(input("Digite uma temperatura em Fahrenheit:"))
print(f)

c = 5.0*(f-32.0)/9.0
print("A temperatura em Celsius é: %s" % c)

"""
Exercício 8 
Leia uma temperatura em graus Kelvin e aprenseta-a convertida em graus Celsius.
A fórmula de conversão é: C = K -273.15, sendo C a temperatura em Celsius
e K a temperatura em Kelvin.
"""
k = float(input("Digite uma temperatura em Kelvin: "))

C = k - 273.15

print("A temperatura em Celsius é: %s" % C)

"""
Exercício 9 
Leia uma temperatura em graus Celsius e aprenseta-a convertida em graus Kelvin.
A fórmula de conversão é: K = C +273.15, sendo K a temperatura em Kelvin
e C a temperatura em Celsius.
"""
C = float(input("Digite uma temperatura em Celsius: "))

k = C + 273.15

print("A temperatura em Kelvin é: %s" % k)

"""
Exercício 10
Leia uma velocidade em km/h(quilômetoros por hora) e apresente-a convertidade em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M em m/s
"""
K = float(input("Digite a velocidae em km/h:"))

M = k/3.6

print("A velocidade em m/s é: %s" % M)
