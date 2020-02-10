"""
Exercício 36
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume de um cilindro circular é calculado por meio a seguinte fórmula:
V = pi * raio² * altura, onde pi = 3.141592
"""
h = float(input("Digite a altura do cilindro: "))
r = float(input("Digite o raio do cilindro: "))
V = 3.141592 * (r*2) * h
print("O volume do cilindro é: %s" % V)

"""
Exercício 37
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%.
"""
prod = float(input("Digigte o valor do produto R$"))
desc = prod * 0.12
total = prod - desc
print("O valor do produto com desconto é R$%s" % total)

"""
Exercício 38
Leia o salário de um funcionário. Calcule e imprima o valor novo salário, sabendo que
ele recebeu um aumento de 25%.
"""
salario = float(input("Digite o valor do salário R$ "))
aument = salario * 0.25
novo_salario = salario + aument
print("O novo salário é R$%s" % novo_salario)

"""
Exercício 39 
A impotância de R$ 780.000,00, será dividida entre três ganahadores de um concurso.
Sendo que da quantia total:
*O primeiro ganhador receberá 48%
*O segundo receberá 32%;
*O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""
Premio = 780_000
primeiro = 780_000 * 0.48
ganhador = 780_000 - primeiro
print("O priemiro ganhador recebera R$%s" % ganhador)
ganhador2 = 780_000 - ganhador
premio2 = ganhador2 * 0.32
total = ganhador2 - premio2
print("O segundo ganhador recebera R$%s" % total)
total2 = 780_000 - (ganhador + total)
print("O terceiro ganhador recebera R$%s" % total2)


"""
Exercício 40 
Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá 
ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""
encanador = float(input("Quantos dias trabalhado? "))
quantia = encanador * 30
liquido = quantia * 0.08
s = quantia - liquido
print("O salário é %s" % s)