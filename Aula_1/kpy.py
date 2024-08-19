print("Calculo de KPI")
print("--------------")

CONSTANTE_BONUS = float(1000)

nome = str(input("Digite seu nome: "))
salario = float(input("Digite o valor do seu salario: "))
bonus = float(input("Digite o valor do seu bonus: "))

#calc_kpi = (float(1000) + salario * bonus) # não é bom setar o valor fixo direto no calculo, uma opção é criar uma CONSTANTE

calc_kpi = (CONSTANTE_BONUS + salario * bonus)

print(calc_kpi)

#print("Ola "+ nome + " o seu valor bônus foi de: " + str(calc_kpi)) #funciona

print(f"Ola {nome} o seu valor bônus foi de: {calc_kpi}") # O print(f) é usado quando queremos printar o valor da vaiavel junto ao texto 

