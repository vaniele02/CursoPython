"""
Estruturas Lógicas
And, or, not, is
Operadores unários:
    -not
Operadores binários:
    -and, or,is

Regras de funcionamento:
Para o and, ambos os valores precisam ser True
Para o or, um ou outro valor precisa ser True
Para o not, o valor do booleano é invertido.

"""

ativo = True
logado = False


"""if ativo or logado:
    print("Bem vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail. ")
"""

# se nao estiver ativo
"""if not ativo:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
else:
    print("Bem-vindo usuário! ")
"""

if ativo:
    print("Bem-vindo usuário! ")

else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

#print(not True)
#print(not False)

#ativo é falso?
print(ativo is False)
