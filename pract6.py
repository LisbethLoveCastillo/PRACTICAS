def decimal_a_binario(n):
    """
    Convierte un número decimal en binario.

    Args:
        n (int): Número decimal.

    Returns:
        str: Representación binaria del número decimal.
    """
    return bin(n)[2:]

def binario_a_decimal(b):
    """
    Convierte un número binario en decimal.

    Args:
        b (str): Número binario como cadena de caracteres.

    Returns:
        int: Representación decimal del número binario.
    """
    return int(b, 2)