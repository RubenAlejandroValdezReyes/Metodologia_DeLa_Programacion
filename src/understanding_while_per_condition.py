"""
    Vamos a realizar un programa que defina un PIN para dar acceso.
    El usuario tendrá n intentos para ingresar el PIN correcto.
    Si el usuario ingresa el PIN correcto, se le dará acceso.
    Si el usuario agota sus intentos, se le negará el acceso.
"""
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempts = 0
reamining_attempts = MAX_ATTEMPTS

while attempts < MAX_ATTEMPTS:
    user_pin = input(f"Ingresa tu PIN tienes {MAX_ATTEMPTS - attempts} :  ")
    if user_pin == CORRECT_PIN:
        print("Acceso concedido.")
        break
    else:
        attempts += 1
        reamining_attempts = MAX_ATTEMPTS - attempts
        print("PIN incorrecto.")
        if reamining_attempts > 1:
            print(f"Te quedan {reamining_attempts} intentos.")
        else:
            print("Cuenta bloqueada.")