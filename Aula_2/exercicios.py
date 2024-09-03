#Exercícios

## Inteiros (int)

#1 Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#valor1 = int(input("Insira um numero: "))
#valor2 = int(input("Insira outro numero: "))
#calc_valores = (valor1 + valor2) 
#print(f"O resultado do calculo é: {calc_valores}")

#2 Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

#valor1 = int(input("Insira um numero: "))
#valor2 = int(5)
#calc_valores = (valor1 % valor2) # % é usado para calcular o resto da divisão
#print(f"O resto da divisão por 5 é: {calc_valores}")

#3 Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#valor1 = int(input("Digite um numero: "))
#valor2 = int(input("Digite outro numero: "))
#calc_valores = valor1 * valor2
#print("O resultado da mutiplicação é: ",calc_valores)

#4 Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#valor1 = int(input("Digite um numero: "))
#valor2 = int(input("Digite outro numero: "))
#calc_valores = valor1 / valor2
#print("O resultado da divisão é: ", int(calc_valores)) # Usei conversão direta para não devolver um valor float -> ex: 7.0

#5 Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#valor = int(input("Digite um numero: "))
#calc_potencia = valor ** 2
#calc_potencia = pow(valor,2)
#print(f"O valor de {valor} eleveado ao quadrado é: {calc_potencia}")

## Números de Ponto Flutuante (float)

#6 Escreva um programa que receba dois números flutuantes e realize sua adição.

#valor1 = float(input("Digite o valor 1: "))
#valor2 = float(input("Digite o valor 2: "))
#calc_valor = valor1 + valor2
#print(f"A soma dos valores é: {calc_valor}")
#print("A soma dos valores é:", calc_valor)


#7 Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

#valor1 = float(input("Digite o valor 1: "))
#valor2 = float(input("Digite o valor 2: "))
#calc_valor = (valor1 + valor2) / 2  #Precedência de operadores, sempre faça as devidas separações dos calculos
#print("A media dos valores é:", calc_valor)


#8 Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
#base = 2.0  # Exemplo de entrada
#expoente = 3.0  # Exemplo de entrada
#potencia = base ** expoente
#print("O resultado da potência é:", potencia)

#9 Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#celsius = 70.0
#farenheit = (celsius * 9/5) + 32
#print("O valor de farenheit é :", farenheit)

#9.1 Faça um programa que converta a temperatura de Fahrenheit para Celsius.

#farenheit = 158.0
#celsius = (farenheit - 32) * 5/9
#print("O valor de celsius é :", celsius)

#10 Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#pi = 3.14159 # defino uma constante
#raio = float(input("Digite o valor do raio: "))
#area = pi * raio ** 2
#print(f"A aredo do circulo é: {area}")


## Strings (str) ##

#11 Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#valor1 = "plutao"
#convert = valor1.upper()
#print(f"Conversão de minuscula: {valor1} -> para maiuscula: {convert}")

#12 Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

#valor1 = input("Digite seu nome: ")
#convert = valor1.lower()
#print(f"Texto em minuscula: {convert}")

#13 Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

#valor1 = input("Digite seu nome: ")
#sem_espaco = valor1.strip()
#print("Limpa espaço em branco:", sem_espaco)

#14 Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.



#15 Escreva um programa que concatene duas strings fornecidas pelo usuário.