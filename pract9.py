def operaciones_basicas():
    print("Operaciones básicas y potencia")
    print("-------------------------------")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operation (+, -, *, /, **): ")

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: no se puede dividir entre cero")
            return
    elif operacion == "**":
        resultado = num1 ** num2
    else:
        print("Error: operación no válida")
        return

    print("Resultado:", resultado)

operaciones_basicas()