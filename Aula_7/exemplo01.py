valor_1 = 4
valor_2 = 6

valor_3 = 10
valor_4 = 25

def soma(valor_soma_1:float, valor_soma_2:float) -> float:

    resultado_soma = valor_soma_1 + valor_soma_2
    return resultado_soma

valor_5 = soma(valor_soma_1 = valor_1, valor_soma_2 = valor_2)
valor_6 = soma(valor_3, valor_4)

print(valor_5)
print(valor_6)