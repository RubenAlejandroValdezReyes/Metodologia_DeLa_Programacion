"""
Alumno: Ruben Alejandro Valdez Reyes
Matrícula: 2530493
Grupo: IM 1-3
Docente: Carlos Antonio Tovar García
Escuela: Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Proyecto: Manejo de Números y Booleanos en Python
"""
#Resumen Ejecutivo
"""
    Este proyecto reúne siete programas hechos en Python que trabajan con números, 
    valores verdaderos o falsos y textos. En cada ejercicio se revisa que los datos 
    que se ingresan sean correctos, se usan condiciones lógicas, se controlan posibles 
    errores y se organiza bien la información que se muestra al final para que el 
    resultado sea fácil de entender. Los programas sirven como ejemplos de cómo usar 
    números enteros y decimales en operaciones básicas, cómo modificar cadenas de texto 
    con diferentes métodos, y cómo usar valores booleanos para tomar decisiones dentro 
    del código. Estas ideas se aplican en situaciones comunes como convertir unidades, 
    revisar datos, comparar valores, clasificar información y procesar correctamente lo 
    que escribe el usuario. Además, el proyecto ayuda a practicar habilidades importantes 
    de programación, como planear pasos (algoritmos), explicar bien qué datos entran y qué 
    datos salen, crear casos para probar que el programa funciona y agregar revisiones que 
    eviten errores durante su ejecución. En conjunto, este trabajo permite comprender mejor 
    cómo Python maneja datos, realiza cálculos y toma decisiones para crear programas 
    seguros y bien organizados.
"""
# Problema 1: Temperature Converter
"""
    Convertir celsius a fahrenheit.
"""
# Entradas:
"""
    temp_celsius: number
"""
# Salidas:
"""
    Fahrenheit temperature
"""
# Validaciones:
"""
    Input must be numeric.
"""
# Casos de prueba:
"""
    a. 0 -> 32
    b. "abc" -> Error
"""
temp_celsius = input("Enter Celsius: ").strip()

def to_float(value):
    try:
        return float(value), True
    except:
        return None, False

value, ok = to_float(temp_celsius)

if ok:
    c = value
    f = (c * 9/5) + 32
    print(f"Fahrenheit: {f}")
else:
    print("Error")


print("\n")

# Problema 2: Extra Hours Salary Calculator
"""
    Calcula el pago en función de las horas trabajadas y la tarifa por hora. 
    Las horas extra (>40) pagan 1,5 veces.
"""
# Entradas:
"""
    hrs: number
    rate: number
"""
# Salidas:
"""
    Total salary
"""
# Validaciones:
"""
    Both inputs must be numeric and positive.
"""
# Casos de prueba:
"""
    a. hrs = 40, rate=10 -> 400
    b. hrs = "abc" -> Error
"""

hrs = input("Hours worked: ").strip()
rate = input("Hourly rate: ").strip()

def conv_float(txt):
    try:
        return float(txt), True
    except:
        return None, False

hours, ok1 = conv_float(hrs)
r, ok2 = conv_float(rate)

if ok1 and ok2:
    if hours < 0 or r < 0:
        print("Error")
    else:
        if hours > 40:
            overtime = hours - 40
            total = (40 * r) + (overtime * r * 1.5)
        else:
            total = hours * r
        print(total)
else:
    print("Error")


print("\n")

# Problema 3: Discount Evaluator
"""
    Evalúa el precio final después del descuento en función del monto.
"""
# Entradas:
"""
    am: number
"""
# Salidas:
"""
    Final price with discount
"""
# Validaciones:
"""
    Amount must be numeric and >= 0.
"""
# Casos de prueba:
"""
    a, 250 -> no discount
    b. 750 -> 10% discount
    c. "bc" -> Error
"""

am = input("Amount: ").strip()

def convert(text):
    try:
        return float(text), True
    except:
        return None, False

a, valid = convert(am)

if valid:
    if a < 0:
        print("Error")
    else:
        if a >= 500:
            final_price = a * 0.90
        else:
            final_price = a
        print(final_price)
else:
    print("Error")


print("\n")

# Problema 4: Integer Stats
"""
    Lee tres números enteros e imprime mínimo, máximo y promedio.
"""
# Entradas:
"""
    integer_1, integer_2, integer_3: integers
"""
# Salidas:
"""
    Minimum, maximum, average
"""
# Validaciones:
"""
    All inputs must be integers.
"""
# Casos de prueba:
"""
    a. 1, 5, 10 -> min=1, max=10, avg=5.33
    b. -3, 0, 3 -> min=-3, max=3, avg=0
    c. "a", 5, 9 -> Error
"""

integer_1 = input("Enter integer 1: ").strip()
integer_2 = input("Enter integer 2: ").strip()
integer_3 = input("Enter integer 3: ").strip()

def conv_int(txt):
    try:
        return int(txt), True
    except:
        return None, False

n1, ok1 = conv_int(integer_1)
n2, ok2 = conv_int(integer_2)
n3, ok3 = conv_int(integer_3)

if ok1 and ok2 and ok3:
    try:
        minium = min(n1, n2, n3)
        maxium = max(n1, n2, n3)
        average = (n1 + n2 + n3) / 3

        # Mantener error original: avegage
        print(minium, maxium, average)

    except:
        print("Error")
else:
    print("Error")


print("\n")

# Problema 5: Loan Eligibility Checker
"""
    Determina si una persona es elegible para un préstamo basado en edad e ingresos.
"""
# Entradas:
"""
    age: number
    inc: number
"""
# Salidas:
"""
    eligible / not eligible
"""
# Validaciones:
"""
    Age and income must be numeric and >= 0.
"""
# Casos de prueba:
"""
    a. age = 25, income = 15000 -> eligible
    b. age = 17, income = 20000 -> not eligible
    c. "abc", 20000 -> Error
"""

age = input("Enter age: ").strip()
inc = input("Enter income: ").strip()

def safe_float(t):
    try:
        return float(t), True
    except:
        return None, False

ag, ok1 = safe_float(age)
inc_val, ok2 = safe_float(inc)

if ok1 and ok2:
    if ag < 0 or inc_val < 0:
        print("Error")
    else:
        if ag >= 18 and inc_val >= 10000:
            print("Eligible")
        else:
            print("Not Eligible")
else:
    print("Error")


print("\n")

# Problema 6: Product Label Formatter
"""
    Crea una etiqueta de producto con un nombre y precio formateados en 
    una cadena de longitud fija.
"""
# Entradas:
"""
    name_product: string
    cost: number/string
"""
# Salidas:
"""
    30-character label
"""
# Validaciones:
"""
    Name must not be empty.
    Price must be numeric and positive.
"""
# Casos de prueba:
"""
    a. "Apple", 10 -> label (30 chars)
    b. long name -> trimmed
    c. price="abc" -> Error
"""

name_product = input("Enter product name: ").strip()
cost = input("Enter price: ").strip()

def text_valid(t):
    return t != ""

if not text_valid(name_product) or not text_valid(cost):
    print("Error")
else:
    try:
        price_num = float(cost)

        label = f"Product: {name_product} | Price: ${price_num}"

        if len(label) < 30:
            padding = 30 - len(label)
            label = label + (" " * padding)
        else:
            label = label[:30]

        print(f'Label: "{label}"')

    except:
        print("Error")


print("\n")

# Problem 7: Password Strength Classifier
"""
    Clasifica la fortaleza de una contraseña como débil, media o fuerte.
"""
# Entradas:
"""
    password: string
"""
# Salidas:
"""
    weak / medium / strong
"""
# Validaciones:
"""
    Must not be empty.
"""
# Casos de prueba:
"""
    a. "666Abc!" -> strong
    b. "password" -> weak
    c. "" -> Error
"""

password = input("Enter password: ").strip()

def check_strength(pwd):
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)

    score = 0

    if length >= 8:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    return score

if password == "":
    print("Error")
else:
    strength = check_strength(password)

    if strength >= 3:
        print("strong")
    elif strength == 2:
        print("medium")
    else:
        print("weak")


print("\n")

# Conclusions
"""
All seven programs demonstrate practical use of numeric processing,
boolean logic and string manipulation in Python. Input validation
proved essential to avoid runtime errors and ensure correct behavior.
Each problem required applying conditions, comparisons, arithmetic
operations and classification logic. These exercises strengthen the
foundational programming skills needed for more complex applications.
"""

# References
"""
1) Python Documentation – Built-in Types.
2) Python String Methods – Official Docs.
3) Real Python – Boolean Logic in Python.
4) W3Schools – Python Input and Data Types.
5) Automate the Boring Stuff with Python – Chapters on strings & logic.
"""
