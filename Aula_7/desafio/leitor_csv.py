import csv

def leitor_cvs(nome_do_arquivo_csv: str) -> list[dict]:
    
    lista = [] #crio uma variavel lista

    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo: #transformo a funcao em uma variavel
        leitor = csv.DictReader(arquivo)
        for linha in leitor: #faço a leitura de linha a linha
            lista.append(linha)
    
    return lista

def filtrar_produtos_por_categoria(lista: list[dict]) -> list[dict]:

    lista_com_produtos_categoria = []

    for produto in lista:
        if produto.get("Categoria") == "Electronics":
            lista_com_produtos_categoria.append(produto)
    return lista_com_produtos_categoria


def soma_produtos_por_categoria(lista_com_produtos_categoria: list[dict]) -> int:

    valor_total = int(0)

    for produto in lista_com_produtos_categoria:
        valor_total += int(produto.get("Venda"))
    
    return valor_total