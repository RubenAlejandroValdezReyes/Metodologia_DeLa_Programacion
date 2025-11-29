# Funciones
"""
    Las funciones son bloques de código reutilizables que realizan una tarea específica.
    Nos permiten organizar nuestro código, hacerlo más legible y evitar la repetición.

    Sintaxis básica para definir una función:
    def nombre_function():
        acciones de la función

    Ejemplo de una función simple que saluda al usuario:
"""
def create_full_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}".title()
    return full_name

first_name = input("Ingresa tu nombre: ")
middle_name = input("Ingresa tu segundo nombre: ")
last_name = input("Ingresa tu apellido: ")

generate_fulln = create_full_name(
    first_name.strip().lower(), 
    middle_name.strip().lower(), 
    last_name.strip().lower())
print(f"Tu nombre completo es: {generate_fulln}")

generate_fulln_2 = create_full_name(
    first_name_user = first_name,
    middle_name_user = middle_name,
    last_name_user = last_name
)
print(generate_fulln_2)