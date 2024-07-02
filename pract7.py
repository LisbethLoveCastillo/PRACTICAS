def frecuencia_palabras(cadena):
    """
    Devuelve un diccionario con cada palabra de la cadena y su frecuencia.

    Args:
        cadena (str): Cadena de caracteres.

    Returns:
        dict: Diccionario con palabras como claves y frecuencias como valores.
    """
    palabras = cadena.split()
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para ignorar mayúsculas
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    """
    Devuelve una tupla con la palabra más repetida y su frecuencia.

    Args:
        frecuencias (dict): Diccionario con palabras como claves y frecuencias como valores.

    Returns:
        tuple: Tupla con la palabra más repetida y su frecuencia.
    """
    palabra_mas_repetida = max(frecuencias, key=frecuencias.get)
    frecuencia_mas_repetida = frecuencias[palabra_mas_repetida]
    return palabra_mas_repetida, frecuencia_mas_repetida