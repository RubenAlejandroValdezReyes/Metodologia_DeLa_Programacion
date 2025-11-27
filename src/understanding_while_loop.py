#While
"""
El while es un ciclo controlado/comando por condición.
La estructura básica es:
while condición:
    action
"""
#While infinito
while True:
    try:
        number = int(input("Ingresa un número entre 10 y 20: "))
        if 10 <= number <= 20:
            print("Numero dentro del rango")
            break  # Salir del ciclo si el número es válido
        else:
            print("Número fuera del rango, intenta de nuevo.")
    except ValueError:
        print("Entrada inválida, por favor ingresa un número entero.")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
        break

print("saliste del while")