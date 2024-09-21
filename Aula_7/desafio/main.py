from leitor_csv import leitor_cvs, filtrar_produtos_por_categoria, soma_produtos_por_categoria

nome_arquivo = '../files/vendas.csv'

lista_de_produtos = leitor_cvs(nome_arquivo)
categoria_de_produtos = filtrar_produtos_por_categoria(lista_de_produtos)
valor_dos_produtos_entregues = soma_produtos_por_categoria(categoria_de_produtos)

print(valor_dos_produtos_entregues)