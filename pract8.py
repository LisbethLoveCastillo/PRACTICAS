def maximo_comun_divisor(a, b):
    """
    Calcula el máximo común divisor de dos números.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: Máximo común divisor de a y b.
    """
    while b != 0:
        a, b = b, a % b
    return a

def minimo_comun_multiplo(a, b):
    """
    Calcula el mínimo común múltiplo de dos números.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: Mínimo común múltiplo de a y b.
    """
    mcd = maximo_comun_divisor(a, b)
    return a * b // mcd