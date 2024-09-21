from typing import List

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]

conversao = celsius_para_fahrenheit([100])

print(conversao)