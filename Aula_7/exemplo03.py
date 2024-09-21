from typing import List

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
            return resultado

filtro = filtrar_acima_de([200.23],85.00)

print(filtro)