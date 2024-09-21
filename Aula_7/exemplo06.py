from typing import List

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

valor_ausente = encontrar_valores_ausentes([0,1,3,5,9]) 

print(valor_ausente)