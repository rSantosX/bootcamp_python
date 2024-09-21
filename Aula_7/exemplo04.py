from typing import List

def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))

valores_unicos = contar_valores_unicos([0,0,2,1,3,4])

print(valores_unicos)