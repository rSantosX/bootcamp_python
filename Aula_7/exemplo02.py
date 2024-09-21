from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

media = calcular_media([20.0,30.5])

print(media)