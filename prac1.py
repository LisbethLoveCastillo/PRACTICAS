def calcular_total_con_igv(monto_sin_igv, porcentaje_igv=18):
  """
  Calcula el total de una factura tras aplicarle el IGV.

  Parámetros:
    monto_sin_igv: El monto de la factura sin IGV.
    porcentaje_igv (opcional): El porcentaje de IGV a aplicar. Por defecto es 18%.

  Retorno:
    El total de la factura con IGV incluido.
  """

  if monto_sin_igv <= 0:
    raise ValueError("El monto de la factura debe ser un número positivo")

  if porcentaje_igv <= 0:
    raise ValueError("El porcentaje de IGV debe ser un número positivo")

  igv = monto_sin_igv * (porcentaje_igv / 100)
  total_con_igv = monto_sin_igv + igv

  return total_con_igv

# Ejemplo de uso con IGV por defecto (18%)
monto_sin_igv = 1000
total_con_igv = calcular_total_con_igv(monto_sin_igv)
print(f"Total con IGV (18%): {total_con_igv}")

# Ejemplo de uso con IGV especificado
monto_sin_igv = 500
porcentaje_igv = 10
total_con_igv = calcular_total_con_igv(monto_sin_igv, porcentaje_igv)
print(f"Total con IGV ({porcentaje_igv}%): {total_con_igv}")
