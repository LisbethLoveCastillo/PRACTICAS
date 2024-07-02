def calcular_media(lista_numeros):
  """
  Calcula la media aritmética de una lista de números.

  Parámetro:
    lista_numeros: La lista de números de la que se quiere calcular la media.

  Retorno:
    La media aritmética de la lista.
  """

  if not lista_numeros:
    raise ValueError("La lista no puede estar vacía")

  if not all(isinstance(numero, float) or isinstance(numero, int) for numero in lista_numeros):
    raise TypeError("La lista solo puede contener números")

  total = sum(lista_numeros)
  media = total / len(lista_numeros)
  return media

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5]
media = calcular_media(lista_numeros)
print(f"La media de la lista es: {media}")
