import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.

    Args:
        radio (float): Radio del círculo.

    Returns:
        float: Área del círculo.
    """
    return math.pi * (radio ** 2)

def calcular_volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro.

    Args:
        radio (float): Radio del cilindro.
        altura (float): Altura del cilindro.

    Returns:
        float: Volumen del cilindro.
    """
    area_base = calcular_area_circulo(radio)
    return area_base * altura