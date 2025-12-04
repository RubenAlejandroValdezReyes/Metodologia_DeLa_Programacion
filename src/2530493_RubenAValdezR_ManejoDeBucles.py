"""
Alumno: Ruben Alejandro Valdez Reyes
Matrícula: 2530493
Grupo: IM 1-3
Docente: Carlos Antonio Tovar García
Escuela: Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Proyecto: Manejo de Bucles en Python
"""
# Resumen ejecutivo
"""
    Esto trata sobre cómo usar los bucles en Python, especialmente las estructuras "for" y "while". Estas herramientas permiten 
    que un programa repita tareas de forma rápida, automatice procesos y trabaje con datos sin tener que escribir las mismas 
    instrucciones una y otra vez.
    Los ejercicios muestran cómo los bucles funcionan con rangos de números, listas, cadenas de texto, contadores, acumuladores 
    y condiciones. Cada actividad incluye validación de datos, un formato claro en las respuestas y el uso correcto de condiciones 
    para evitar que el programa se quede en un ciclo infinito.
    Al resolver situaciones prácticas como cálculos repetidos, creación de patrones, recorridos de datos y decisiones basadas en 
    repetición, el proyecto ayuda al estudiante a crear algoritmos bien organizados. También fortalece principios importantes de 
    programación como la claridad del código, la organización y la precisión, ofreciendo una base firme para crear programas más 
    avanzados en Python.
"""

# Problema 1 - Sum of range with for
"""
    Consiste en calcular la suma de todos los enteros desde 1 hasta n. Tambien puede calcular 
    la suma únicamente de los números pares dentro del mismo rango usando un ciclo for.
"""
# Entradas:
"""
    n (int): upper limit of the range.
"""
# Salidas:
"""
    "Sum 1..n:" <total_sum>
    "Even sum 1..n:" <even_sum>
"""
# Validaciones:
"""
    n >= 1; otherwise print "Error: invalid input".
    n must be convertible to int.
"""
# Casos de prueba:
"""
    a. n = 10 → Sum = 55, Even sum = 30
    b. n = -2 → Error
    c. n = 5 → Sum = 15, Even sum = 6
    d. n = "hola" → Error
    e. n = 1 → Sum = 1, Even sum = 0

"""
input_n = input("Enter n: ")

def convert_to_int(v):
    try:
        return int(v), True
    except:
        return None, False

# Convertimos el input
num_n, ok = convert_to_int(input_n)

if not ok:
    print("Error: invalid input")

else:
    if num_n < 1:
        print("Error: invalid input")
    else:

        total_s = 0
        even_s = 0

        # Recorremos 1..num_n (corrección final)
        for i in range(1, num_n + 1):
            total_s += i
            if i % 2 == 0:
                even_s += i

        print("Sum 1..n:", total_s)
        print("Even sum 1..n:", even_s)

print("\n")

# Problema 2 - Multiplication table with for
"""
    Genera la tabla de multiplicar de un número base, desde 1 hasta x, usando un ciclo for.
"""
# Entradas:
"""
    base (int)
    x (int): table limit.
"""
# Salidas:
"""
    One line per multiplication: "<base> x <i> = <result>"
"""
# Validaciones:
"""
    base and m must be convertible to int.
    x >= 1; otherwise print "Error: invalid input".
"""
# Casos de prueba:
"""
    a. x = 0 → Error
    b. base="aaa" → Error
    c. base=9, x = 10 → prints 10 lines
    d. base=5, x = 4 → prints 4 lines
    e. base=3, x = 1 → prints "3 x 1 = 3"
"""

input_base = input("Enter base: ")
x_input = input("Enter x: ")

def safe_int(text):
    try:
        return int(text), True
    except:
        return None, False

base, ok1 = safe_int(input_base)
x, ok2 = safe_int(x_input)

if ok1 and ok2:
    if x < 1:
        print("Error: invalid input")
    else:
        for i in range(1, x + 1):
            result = base * i
            print(f"{base} x {i} = {result}")
else:
    print("Error: invalid input")


print("\n")

# Problema 3 - Average with while and sentinel
"""
    Lo que hace es leer números uno por uno hasta que el usuario ingrese el valor centinela (-1), 
    tambien calcula el promedio y la cantidad de números ingresados. Si no se ingresa ningún valor 
    válido procede a mostrar error.
"""
# Entradas:
"""
    number (float) repeatedly
    sentinel = -1
"""
# Salidas:
"""
    "Count:" <count>
    "Average:" <average>
    "Error: no data" if no valid input.
"""
# Validaciones:
"""
    Each number must be convertible to float.
    Sentinel must not be included in calculations.
"""
# Casos de prueba:
"""
    a. 10, -1 → Count=1, Avg=10
    b. 3, 6, 9, -1 → Count=3, Avg=6
    c. 2.5, 2.5, 2.5, -1 → Avg=2.5
    d. abc → ignored
    e. -1 → Error
"""

sentinel = -1
count = 0
total = 0.0

def to_float(v):
    try:
        return float(v), True
    except:
        return None, False

while True:
    value = input("Enter number (-1 to stop): ")
    num, ok = to_float(value)

    if ok:
        if num == sentinel:
            break
        total += num
        count += 1
    else:
        print("Invalid number, ignored.")

if count == 0:
    print("Error: no data")
else:
    avg = total / count
    print("Count:", count)
    print("Average:", avg)


print("\n")

# Problema 4 - Password attempts with while
"""
    Es un sistema de verificación de contraseña con un número máximo de intentos, si
    la contraseña ingresada es correcta antes de agotar los intentos, se muestra éxito; 
    sin embargo, si se agotan los intentos, se bloquea la cuenta.
"""
# Entradas:
"""
    user_password (string)
"""
# Salidas:
"""
    "Login success" if correct
    "Account locked" if attempts exhausted
"""
# Validaciones:
"""
    max_att > 0
    Count attempts correctly
"""
# Casos de prueba:
"""
    a. Password with spaces → valid if matches
    b. Correct on first try → success
    c. Empty input → attempts consumed
    d. Wrong, wrong, correct → success
    e. Wrong all attempts → locked
"""

correct_password = "charly123"
max_att = 3
att = 0

def validate_password(inp, correct):
    return inp == correct

while att < max_att:
    pwd = input("Enter password: ")

    if validate_password(pwd, correct_password):
        print("Login success")
        break
    else:
        att += 1

if att == max_att:
    print("Account locked")

    
print("\n")

# Problema 5 - Simple menu with while
"""
    Menú interactivo que se repite hasta que el usuario elija 0 para salir, tambien contiene 
    un contador que puede visualizarse o incrementarse.
"""
# Entradas:
"""
    option (int)
"""
# Salidas:
"""
    "Hello!"
    "Counter:" <value>
    "Counter incremented"
    "Bye!"
    "Error: invalid option"
"""
# Validaciones:
"""
    Option must be convertible to int
    Only 0, 1, 2, 3 valid
"""
# Casos de prueba:
"""
    a. Sequence 1, 2, 3, 0 → all features
    b. 9 → error
    c. 1 → Hello!
    d. 2 → shows counter
    e. 3 → increments counter
"""

counter = 0

def convert_option(v):
    try:
        return int(v), True
    except:
        return None, False

while True:
    print("0) Exit")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")

    opt_raw = input("Select option: ")
    opt, ok = convert_option(opt_raw)

    if not ok:
        print("Error: invalid option")
        continue

    if opt == 0:
        print("Bye!")
        break
    elif opt == 1:
        print("Hello!")
    elif opt == 2:
        print("Counter:", counter)
    elif opt == 3:
        counter += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")


print("\n")

# Problema 6 - Pattern printing with nested loops
"""
    Consiste en imprimir un patrón de asteriscos en forma de triángulo rectángulo 
    usando ciclos for anidados, puede imprimirse también un triángulo invertido.
"""
# Entradas:
"""
    n (int): number of rows for the pattern.
"""
# Salidas:
"""
    Pattern printed line by line:
    *
    **
    ***
"""
# Validaciones:
"""
    n must be convertible to int
    n >= 1
"""
# Casos de prueba:
"""
    a. n = "hola" → error
    b. n = 0 → error
    c. n = 1 → "*"
    d. n = 3 → "*", "**", "***"
    e. n = 5 → prints 5 lines
"""

n_input = input("Enter n: ")

def parse_int(t):
    try:
        return int(t), True
    except:
        return None, False

n, ok = parse_int(n_input)

if ok:
    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            row = "*" * i
            print(row)
else:
    print("Error: invalid input")

print("\n")

# Conclusión
"""
    La ejecución de este proyecto contribuyó de manera significativa al fortalecimiento del conocimiento sobre las 
    estructuras de repetición en Python y su papel esencial en la automatización de procesos. A través del uso de 
    los bucles "for" y "while", se evidenció cómo la iteración puede aplicarse en rangos numéricos, listas, 
    manipulación de cadenas, contadores y evaluaciones condicionadas.
    Cada ejercicio subrayó la relevancia de gestionar adecuadamente los bucles mediante condiciones de salida claras, 
    validación correcta de los datos y una lógica bien definida que impida la generación de ciclos infinitos. 
    El trabajo con estructuras repetitivas permitió elaborar algoritmos eficientes, capaces de procesar información 
    de manera ordenada y adaptarse a distintos tipos de problemas.
    En conjunto, este proyecto ofreció una base sólida para continuar con metodologías de programación más avanzadas, 
    fortaleciendo la precisión, la claridad y la capacidad analítica necesaria para resolver problemas mediante el uso 
    adecuado de estructuras iterativas en Python.
"""
# Referencias
"""
    1. Shaw, Z. A. (2017). Learn Python the Hard Way (3rd ed.). Addison-Wesley Professional.
    2. Sweigart, A. (2019). Automate the Boring Stuff with Python: Practical Programming for Total Beginners (2nd ed.). No Starch Press.
    3. Ramalho, L. (2021). Fluent Python: Clear, Concise, and Effective Programming (2nd ed.). O’Reilly Media.
    4. Punch, W., & Enbody, R. (2016). The Practice of Computing Using Python (3rd ed.). Pearson.
    5. Miller, B. N., & Ranum, D. L. (2020). Python Programming in Context (3rd ed.). Jones & Bartlett Learning.
"""
