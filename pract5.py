import math

def estadisticas(muestra):
    """
    Calcula la media, varianza y desviación típica de una muestra de números.

    Args:
        muestra (list): Lista de números.

    Returns:
        dict: Diccionario con la media, varianza y desviación típica de la muestra.
    """
    n = len(muestra)
    media = sum(muestra) / n
    varianza = sum((x - media) ** 2 for x in muestra) / n
    desviacion_tipica = math.sqrt(varianza)

    return {
        'media': media,
        'varianza': varianza,
        'desviacion_tipica': desviacion_tipica
    }