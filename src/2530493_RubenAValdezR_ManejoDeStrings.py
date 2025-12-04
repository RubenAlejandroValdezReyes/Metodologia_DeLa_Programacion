"""
Alumno: Ruben Alejandro Valdez Reyes
Matrícula: 2530493
Grupo: IM 1-3
Docente: Carlos Antonio Tovar García
Escuela: Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Proyecto: Manejo de Strings en Python
"""
# Resumen ejecutivo
"""
    El proyecto de Manejo de Strings en Python reúne seis ejercicios creados para practicar las operaciones
    básicas con cadenas de texto. Cada actividad presenta una situación real donde el usuario escribe algún 
    texto que debe ser limpiado, revisado y trabajado correctamente.
    Los programas incluyen tareas como: dar formato a un nombre completo usando iniciales, revisar si un 
    correo electrónico es válido, identificar si una palabra o frase es un palíndromo sin tomar en cuenta 
    espacios, analizar cuántas palabras hay en una oración, clasificar contraseñas según su nivel de seguridad 
    y crear etiquetas de producto con un tamaño fijo. Para esto se usan funciones como strip(), lower(), 
    split(), replace(), cortes de texto (slicing), conteo de caracteres y revisión de patrones sencillos.
    Este conjunto de ejercicios muestra la importancia de limpiar el texto antes de usarlo, verificar las 
    entradas para evitar errores y aprovechar que los strings no se pueden modificar directamente, lo que 
    permite generar nuevas versiones más ordenadas y seguras. El documento también incluye pruebas y 
    conclusiones que explican la lógica utilizada en cada programa.
"""
# Problema 1 - Full name formatter
"""
    Formatea un nombre completo en mayúsculas y minúsculas y genera iniciales utilizando la entrada limpia.
"""
# Entradas:
"""
    full_n: string
"""
# Salidas:  
"""
    Formatted name: <...>
    Initials: <...>
"""
# Validaciones:
"""
    Input cannot be empty.
    Must contain at least two words.
"""
# Casos de prueba:
"""
    a. Normal: "Ruben Valdez Reyes" -> Formatted name: Ruben Valdez Reyes | Initials: R.V.R.
    b. Border: "  ruben   valdez  " -> Ruben Valdez | R.V.
    c. Error: "   " -> Error: invalid input
"""

full_n = input("Enter full name: ").strip()

def is_valid_name(name):
    return not (name == "" or len(name.split()) < 2)

if not is_valid_name(full_n):
    print("Error: invalid input")

else:
    parts = full_n.lower().split()

    formatted_parts = []
    for p in parts:
        formatted_parts.append(p.title())

    formatted = " ".join(formatted_parts)

    initials_list = []
    for p in parts:
        initials_list.append(p[0].upper())
    initials = ".".join(initials_list) + "."

    print(f"Formatted name: {formatted}")
    print(f"Initials: {initials}")

print("\n")

# Problema 2 - Simple email validator
"""
    Valida si un correo electrónico es correcto y extrae el dominio si es válido.
"""
# Entradas:
"""
    email_txt: string
"""
# Salidas:
"""
    Valid email: true/false
    Domain: <...> (if valid)
"""
# Validaciones:
"""
    Email cannot be empty.
    Must have exactly one '@'.
    No spaces allowed.
"""
# Casos de prueba:
"""
    a. Normal: "user@mail.com" -> Valid email: true | Domain: mail.com
    b. Border: "test@domain" -> Valid email: false
    c. Error: "user@@mail.com" -> Valid email: false
"""
email_txt = input("Enter email: ").strip()

def basic_email_check(mail):
    if mail == "" or " " in mail:
        return False
    if mail.count("@") != 1:
        return False
    return True

if not basic_email_check(email_txt):
    print("Valid email: false")

else:
    at_index = email_txt.find("@")
    domain = email_txt[at_index + 1:]

    if "." in domain:
        print("Valid email: true")
        print(f"Domain: {domain}")
    else:
        print("Valid email: false")

print("\n")

# Problema 3 - Palindrome checker
"""
    Revisa si una frase es un palíndromo ignorando espacios y mayúsculas.
"""
# Entradas:
"""
    phr: string
"""
# Salidas:
"""
    Is palindrome: true/false
"""
# Validaciones:
"""
    Input cannot be empty.
    Minimum length after cleaning: 3 characters.
"""
# Casos de prueba:
"""
    a. Normal: "Arroz zorra" -> true
    b. Border: "ele" -> true
    c. Error: "o" -> Error: too short
"""
phr = input("Enter phrase: ").strip()

def clean_text(txt):
    return txt.replace(" ", "").lower()

if phr == "":
    print("Error: invalid input")
else:
    cleaned = clean_text(phr)

    if len(cleaned) < 3:
        print("Error: too short")
    else:
        is_pal = cleaned == cleaned[::-1]
        print(f"Is palindrome: {str(is_pal).lower()}")

print("\n")

# Problema 4 - Sentence word stats
"""
    Analiza una oración para contar palabras, identificar la primera y última, y encontrar la más corta 
    y larga.
"""
# Entradas:
"""
    snc: string
"""
# Salidas:
"""
    First word
    Word count
    Last word
    Shortest and longest words
"""
# Validaciones:
"""
    Cannot be empty.
    Must contain at least one valid word.
"""
# Casos de prueba:
"""
    a. Normal: "hello world from python" -> count = 4, first = hello, last = python
    b. Border: "   hi   " -> count = 1
    c. Error: "    " -> Error: invalid input
"""

snc = input("Enter sentence: ").strip()

def split_words(text):
    return text.split()

if snc == "":
    print("Error: invalid input")

else:
    wrd = split_words(snc)

    if len(wrd) == 0:
        print("Error: invalid input")
    else:
        shortest = min(wrd, key=len)
        longest = max(wrd, key=len)

        print(f"Word count: {len(wrd)}")
        print(f"First word: {wrd[0]}")
        print(f"Last word: {wrd[-1]}")
        print(f"Shortest word: {shortest}")
        print(f"Longest word: {longest}")

print("\n")

# Problema 5 - Password strength classifier
"""
    Clasifica la fortaleza de una contraseña según su longitud y variedad de caracteres.
"""
# Entradas:
"""
    pass_i: string
"""
# Salidas:
"""
    Password strength: weak/medium/strong
"""
# Validaciones:
"""
    Cannot be empty.
    Length must be checked.
"""
# Casos de prueba:
"""
    a. Normal: "Abc123!!" -> strong
    b. Border: "password" -> weak
    c. Error: "" -> Error: invalid input
"""

pass_i = input("Enter password: ")

if pass_i.strip() == "":
    print("Error: invalid input")

else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for c in pass_i:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif not c.isalnum():
            has_symbol = True

    length = len(pass_i)

    # MISMA lógica original
    if length < 8 or (has_lower and not has_upper and not has_digit and not has_symbol):
        print("Password strength: weak")

    elif length >= 8 and ((has_upper and has_lower) or has_digit):

        if has_upper and has_lower and has_digit and has_symbol:
            print("Password strength: strong")
        else:
            print("Password strength: medium")

    else:
        print("Password strength: weak")


print("\n")

#Problem 6 - Product label formatter
"""
    Crea una etiqueta de producto con un nombre y precio formateados en una cadena de longitud fija.
"""
# Entradas:
"""
    name_product: string
    cost_value: string/number
"""
# Salidas:
"""
    Label: "<30 char string>"
"""
# Validaciones:
"""
    name_product cannot be empty.
    cost_value must be numeric and positive.
"""
# Casos de prueba:
"""
    a. Normal: product = "Apple", price = "10" -> valid label 30 chars
    b. Border: long product name -> trimmed
    c. Error: price = "abc" -> invalid price
"""

name_product = input("Enter product name: ").strip()
cost_value = input("Enter price: ").strip()

def valid_fields(n, p):
    return n != "" and p != ""

if not valid_fields(name_product, cost_value):
    print("Error: invalid input")

else:
    try:
        price = float(cost_value)

        label = f"Product: {name_product} | Price: ${price}"

        if len(label) < 30:
            missing = 30 - len(label)
            label = label + (" " * missing)
        else:
            label = label[:30]

        print(f"Label: \"{label}\"")

    except:
        print("Error: invalid price")

print("\n")

# Conclusion
"""
Las actividades realizadas demostraron que trabajar con cadenas de texto en Python es esencial para revisar, 
limpiar y transformar los datos que el usuario escribe. Usando operaciones como strip(), lower(), split(), 
join(), replace() y cortes de texto (slicing), es posible asegurar que la información se procese de manera 
correcta y segura. Durante los seis ejercicios, se reforzó lo importante que es normalizar los datos antes 
de compararlos, ya que detalles como mayúsculas, espacios o caracteres extra pueden cambiar los resultados. 
También se vio que, como los strings no se pueden modificar directamente, es más fácil trabajar con ellos 
porque cada cambio genera una nueva cadena de forma ordenada y predecible.Crear validaciones claras ayuda a 
evitar errores y permite construir programas más confiables y fáciles de usar. Manejar correctamente el texto 
es una habilidad clave y necesaria en casi cualquier aplicación real.
"""
# References:
"""
1. Ramalho, L. (2021). Fluent Python: Clear, Concise, and Effective Programming (2nd ed.). O’Reilly Media.
2. Zelle, J. (2016). Python Programming: An Introduction to Computer Science (3rd ed.). Franklin, Beedle & Associates.
3. Sweigart, A. (2020). Beyond the Basic Stuff with Python: Best Practices for Writing Clean Code. No Starch Press.
4. McKinney, W. (2018). Python for Data Analysis (2nd ed.). O’Reilly Media.
5. Punch, W. F., & Enbody, R. C. (2020). Introduction to Data Structures Using Python. Pearson.
"""