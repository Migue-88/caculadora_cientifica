print("**************** Calculadora Cientifica *****************")

numeros = []

while True:
    entrada = input("Ingrese un número (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido o 'fin' para terminar.")

if not numeros:
    print("No se ingresaron números.")
else:
    print("Ingrese una opción: ")
    print("1: Sumar ")
    print("2: Restar ")
    print("3: Dividir ")
    print("4: Multiplicar ")
    print("5: Salir ")

    opcion = int(input("Seleccione una opción: (1-5) "))

    def menu(opcion, numeros):
        match opcion:
            case 1:
                resultado = sum(numeros)
                print("La suma es: ", resultado)
            case 2:
                resultado = numeros[0]
                for num in numeros[1:]:
                    resultado -= num
                print("La resta es: ", resultado)
            case 3:
                resultado = numeros[0]
                for num in numeros[1:]:
                    resultado /= num
                print("La división es: ", resultado)
            case 4:
                resultado = 1
                for num in numeros:
                    resultado *= num
                print("La multiplicación es: ", resultado)
            case 5:
                print("Saliendo...")
            case _:
                print("Opción no válida.")

    menu(opcion, numeros)