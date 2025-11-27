"""
    Docstring for src/understanding_while_loop_centinel.py

    Un programa que:
        -cuente cuantos numeros ingresa el usuario 
        -Realice la suma de los numeros ingresados
        -Me diga cual es el minimo y el maximo numero ingresado
"""
counter = 0
total_sum = 0
min_number = None
max_number = None

while True:
    print("Escribe exit pa salir")
    user_input = input("Ingresa una cantidad en MXN: ")
    if user_input == "exit":
        break
    try:
        value = float(user_input)
    except ValueError:
        print("Por favor ingresa un número válido o 'exit' para salir.")
        continue
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
        break

    counter = counter + 1
    total_sum = total_sum + value
    if min_number is None or value < min_number:
        min_number = value
    if max_number is None or value > max_number:
        max_number = value
    
print(f"Cantidad de números ingresados: {counter}")
print(f"Suma total de los números ingresados: {total_sum}") 
print(f"Número mínimo ingresado: {min_number}")
print(f"Número máximo ingresado: {max_number}")
