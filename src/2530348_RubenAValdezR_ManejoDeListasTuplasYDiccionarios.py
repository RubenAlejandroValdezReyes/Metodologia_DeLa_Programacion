"""
Alumno: Ruben Alejandro Valdez Reyes
Matrícula: 2530493
Grupo: IM 1-3
Docente: Carlos Antonio Tovar García
Escuela: Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Proyecto: Manejo de Listas, Tuplas y Diccionarios en Python
"""
# Resumen Ejecutivo
"""
    En Python,  las colecciones sirven para organizar datos y trabajar con ellos de manera práctica.
    Las listas (list) son conjuntos de elementos ordenados que se pueden cambiar, es decir, puedes 
    añadir, borrar o modificar datos mientras el programa está funcionando.
    Las tuplas (tuple) también son ordenadas, pero no se pueden modificar, por lo que son útiles 
    para guardar información que debe mantenerse igual, como coordenadas o datos que no deben cambiar.
    Los diccionarios (dict) guardan información en forma de clave y valor, lo que permite encontrar 
    datos rápido y manejar información relacionada, como listas de contactos, productos o calificaciones.
    Este documento incluye seis ejercicios que muestran cómo usar listas, tuplas y diccionarios en 
    situaciones reales. Cada ejercicio explica el problema, las entradas, salidas, validaciones y varios 
    casos de prueba (normales, límites y errores). A través de estos ejemplos se practican acciones 
    básicas como buscar, actualizar, agregar y  procesar datos, ayudando a comprender mejor el uso de 
    estas estructuras en la programación cotidiana.
"""
# Problema 1 – Shopping List Basics
"""
    Este programa trabaja con una lista de artículos. Crea una lista inicial, añade un 
    nuevo artículo, cuenta el total de artículos y comprueba si existe un producto específico.
"""
# Entradas:
"""
    inicial_it_txt (string)
    new_it (string)
    srch_it (string)
"""
# Salidas:
"""
    Items list
    Total items count
    Boolean value showing if item was found
"""
# Validaciones:
"""
    initial_items_text must not be empty
    All items must be cleaned using strip()
    new_item and search_item must not be empty
"""
# Casos de prueba:
"""
    a. Normal: "apple,banana", "orange", "banana"
    b. Normal: "milk,bread,eggs", "coffee", "eggs"
    c. Border: "", "apple", "apple"
    d. Border: "apple", "", "apple"
    e. Error: "apple,banana", "orange", ""
"""

inicial_it_txt = "apple,banana,orange"
new_it = "grape"
srch_it = "banana"

# Función para limpiar texto
def clean_text(txt):
    return txt.strip()

# Función para convertir texto en lista de items
def parse_items(txt):
    if clean_text(txt) == "":
        return []
    return [item.strip() for item in txt.split(",") if item.strip()]

# Crear lista inicial
items_list = parse_items(inicial_it_txt)

# Agregar un nuevo ítem si es válido
if clean_text(new_it) != "":
    cleaned_item = clean_text(new_it)
    if cleaned_item:
        items_list.append(cleaned_item)

# Verificar si el elemento buscado existe en la lista
if clean_text(srch_it):
    is_in_list = clean_text(srch_it) in items_list
else:
    is_in_list = False

# Salidas finales (las mismas)
print("Items list:", items_list)
print("Total items:", len(items_list))
print("Found item:", is_in_list)

print("\n")

# Problema 2 – Points and Distances with Tuples
"""
    Este programa utiliza tuplas para almacenar las coordenadas de dos puntos y 
    calcula la distancia euclidiana y el punto medio.
"""
# Entradas:
"""
    x1, y1, x2, y2 (float)
"""
# Salidas:
"""
    Point A, Point B
    Distance between points
    Midpoint tuple
"""
# Validaciones:
"""
    Inputs must be convertible to float
"""
# Casos de prueba:
"""
    a. Normal: (0,0) and (3,4)
    b. Normal: (1,2) and (5,9)
    c. Border: (0,0) and (0,0)
    d. Border: (-5,-5) and (5,5)
    e. Error: x1 = "abc"
"""

x1 = 0.0
y1 = 0.0
x2 = 3.0
y2 = 4.0

point_a = (x1, y1)
point_b = (x2, y2)

# Función para calcular distancia
def calc_distance(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return (dx**2 + dy**2) ** 0.5

# Función para calcular punto medio
def calc_midpoint(a, b):
    mx = (a[0] + b[0]) / 2
    my = (a[1] + b[1]) / 2
    return (mx, my)

distance = calc_distance(point_a, point_b)
midpoint = calc_midpoint(point_a, point_b)

print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", distance)
print("Midpoint:", midpoint)


print("\n")

# Problema 3 – Product Catalog Dictionary
"""
    Administra un diccionario de productos y calcula el precio total en función de la cantidad.
"""
# Entradas:
"""
product_name (string)
quantity (int)
"""
# Salidas:
"""
    Unit price
    Quantity
    Total price
    Error if product does not exist
"""
# Validaciones:
"""
    quantity > 0
    product_name must not be empty
    product must exist in dictionary
"""
# Casos de prueba:
"""
    a. Normal: "apple", 2
    b. Normal: "banana", 5
    c. Border: product in dict but quantity = 1
    d. Error: product does not exist
    e. Error: quantity = 0
"""

product_prices = {"apple": 10.0, "banana": 7.5, "milk": 22.0}

product_name = "apple"
quantity = 3

def validate_input(name, qty):
    if name.strip() == "" or qty <= 0:
        return False
    return True

def product_exists(name, db):
    return name in db

if not validate_input(product_name, quantity):
    print("Error: invalid input")
elif not product_exists(product_name, product_prices):
    print("Error: product not found")
else:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity

    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)


print("\n")

# Problema 4 – Student Grades
"""
    Utiliza un diccionario donde cada clave es el nombre de un estudiante y 
    el valor es una lista de calificaciones. Calcula el promedio y determina 
    si se aprobó la asignatura.
"""
# Entradas:
"""
    student_name (string)
"""
# Salidas:
"""
    Grades list
    Average
    Passed boolean
    Error if student does not exist
"""
# Validaciones:
"""
    student_name must not be empty
    student must exist
    grades list must not be empty
"""
# Casos de prueba:
"""
    a. Normal: "Alice"
    b. Normal: "Bob"
    c. Border: student has exactly 1 grade
    d. Error: student does not exist
    e. Error: student_name = ""
"""

grades = {
    "Alice": [90, 85, 88],
    "Bob": [70, 75, 72],
    "Carol": [60, 65, 55]
}

student_name = "Alice"

def is_valid_name(name):
    return name.strip() != ""

def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count

if not is_valid_name(student_name):
    print("Error: invalid input")
elif student_name not in grades:
    print("Error: student not found")
else:
    student_grades = grades[student_name]
    average = calculate_average(student_grades)
    is_passed = average >= 70.0

    print("Grades:", student_grades)
    print("Average:", average)
    print("Passed:", is_passed)


print("\n")

# Problema 5 – Word Frequency Counter
"""
    Cuenta la frecuencia de cada palabra en una oración usando lista + diccionario.
"""
# Entradas:
"""
    sentence (string)
"""
# Salidas:
"""
    Words list
    Frequency dictionary
    Most common word
"""
# Validaciones:
"""
    sentence must not be empty
    words list must not be empty
"""
# Casos de prueba:
"""
    a. Normal: "apple banana apple orange"
    b. Normal: "hello world hello"
    c. Border: "apple"
    d. Border: "A A A a"
    e. Error: ""
"""

sentence = "apple banana apple orange"

def clean_sentence(txt):
    return txt.strip().lower()

if clean_sentence(sentence) == "":
    print("Error: invalid input")
else:
    words_list = clean_sentence(sentence).split()

    freq = {}
    for w in words_list:
        freq[w] = freq.get(w, 0) + 1

    most_common = max(freq, key=freq.get)

    print("Words list:", words_list)
    print("Frequencies:", freq)
    print("Most common word:", most_common)


print("\n")

# Problema 6 – Contact Book CRUD
"""
    Implementa una libreta de contactos utilizando un diccionario con acciones "agregar,
    buscar y eliminar" contactos.
"""
# Entradas:
"""
    action_text
    name
    phone (only for ADD)
"""
# Salidas:
"""
    Contact saved
    Phone found
    Contact deleted
    Error if not found
"""
# Validaciones:
"""
    action must be ADD, SEARCH or DELETE
    name must not be empty
    phone must not be empty when adding
"""
# Casos de prueba:
"""
    ADD: ("ADD", "Alice", "12345")
    SEARCH: ("SEARCH", "Alice")
    DELETE: ("DELETE", "Alice")
    Error: search non-existing name
     Error: ADD with empty phone
"""

contacts = {"Bob": "777888999"}

action_text = "ADD".upper()
name = "Alice"
phone = "555222111"

valid_actions = ["ADD", "SEARCH", "DELETE"]

def is_valid_action(action):
    return action in valid_actions

def save_contact(db, n, p):
    db[n] = p

def search_contact(db, n):
    return db.get(n)

def delete_contact(db, n):
    if n in db:
        db.pop(n)

if not is_valid_action(action_text):
    print("Error: invalid action")
else:
    if action_text == "ADD":
        if name.strip() == "" or phone.strip() == "":
            print("Error: invalid input")
        else:
            save_contact(contacts, name, phone)
            print("Contact saved:", name, phone)

    elif action_text == "SEARCH":
        result = search_contact(contacts, name)
        if result:
            print("Phone:", result)
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            delete_contact(contacts, name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")


print("\n")

# Conclusión
"""
    Durante el desarrollo de los programas, se reforzó el uso práctico de los tipos de 
    datos básicos de Python, como enteros, flotantes, booleanos y cadenas de texto. En 
    cada ejercicio se mostró cómo la validación correcta de entradas, el uso de condiciones 
    y una salida bien organizada ayudan a que un programa funcione de forma confiable y 
    sin sorpresas.
    Los ejercicios permitieron combinar operaciones numéricas, manejo de cadenas y 
    evaluaciones lógicas para resolver tareas como comparar datos, clasificar información, 
    convertir unidades y procesar datos. Al crear algoritmos ordenados y probarlos con 
    diferentes situaciones, los proyectos ayudaron a mejorar el pensamiento analítico y 
    las habilidades para resolver problemas.
    Además, el enfoque en documentar entradas, salidas y casos de prueba dio más claridad 
    y facilitó el mantenimiento del código, resaltando lo importante que es escribir programas 
    limpios, ordenados y bien diseñados. En general, este conjunto de programas ayuda a formar 
    una base sólida para aprender temas más avanzados y crear aplicaciones en Python que sean 
    eficientes y profesionales.
"""
# Referencias
"""
    [1] M. Summerfield, Programming in Python 3: A Complete Introduction to the Python Language, 
    2nd ed. Addison-Wesley Professional, 2010.
    [2] A. Sweigart, Automate the Boring Stuff with Python: Practical Programming for Total 
    Beginners, 2nd ed. No Starch Press, 2019.
    [3] Python Software Foundation, “The Python Standard Library Documentation,” python.org.
    [4] B. J. Chun, Core Python Programming, 3rd ed. Prentice Hall, 2012.
    [5] L. Atwood, Effective Python: 90 Specific Ways to Write Better Python, 2nd ed. 
    Addison-Wesley Professional, 2019.
"""
