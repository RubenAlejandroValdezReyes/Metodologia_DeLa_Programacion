"""
Alumno: Ruben Alejandro Valdez Reyes
Matrícula: 2530493
Grupo: IM 1-3
Docente: Carlos Antonio Tovar García
Escuela: Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Proyecto: Fibonacci Series with Python
"""
# Resumen Ejecutivo
"""
    Este proyecto crea un programa en Python que genera la serie de Fibonacci. El usuario 
    ingresa un número entero n, y después de verificar que el dato sea válido, el programa 
    muestra los primeros n valores de la secuencia, empezando por 0 y 1. En este trabajo 
    se resaltan puntos importantes de la programación estructurada, como el uso de bucles 
    para repetir procesos, la revisión de los datos que escribe el usuario y la forma 
    correcta de mostrar los resultados. La solución demuestra que una lógica ordenada y 
    clara ayuda a reutilizar el código y garantiza que los resultados sean exactos, incluso 
    cuando se trata de valores muy pequeños o casos especiales. También se subraya la 
    importancia de detectar entradas incorrectas para evitar fallos mientras el programa 
    se ejecuta.
"""
# Entradas
"""
    n (int; number of terms to generate)
"""
# Salidas
"""
    "Number of terms:" n
    "Fibonacci series:" followed by the n terms separated by spaces
"""
# Validaciones 
"""
    n must be an integer
    n >= 1
    n <= 50 (to avoid very large sequences)
"""
# Casos de Uso
"""
    a. Normal: n = 5 → expected series: 0 1 1 2 3
    b. Border: n = 1 → expected series: 0
    c. Error: n = 0 → expected message: "Error: invalid input"
"""
def validate_input(user_input):
    try:
        value = int(user_input)
        if value < 1 or value > 50:
            raise ValueError
        return value
    except ValueError:
        raise ValueError("Invalid input: must be an integer between 1 and 50")

def generate_fibonacci_series(count):
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def display_fibonacci(count, sequence):
    print(f"Number of terms: {count}")
    print("Fibonacci series:", " ".join(str(num) for num in sequence))

def main():
    try:
        user_input = input("Enter the number of terms: ")

        n = validate_input(user_input)

        fibonacci_series = generate_fibonacci_series(n)

        display_fibonacci(n, fibonacci_series)

    except ValueError:
        print("Error: invalid input")

if __name__ == "__main__":
    main()

# Conclusión
"""
    El desarrollo de este programa ayudó a entender cómo los bucles permiten crear series numéricas 
    de forma rápida y repetida, evitando hacer cálculos a mano y asegurando resultados precisos. Las 
    validaciones de entrada hacen que el programa sea más seguro, porque evitan errores cuando el 
    usuario escribe datos incorrectos o fuera del rango permitido. También se manejaron correctamente 
    los casos especiales, como cuando n = 1 o n = 2, lo que asegura que la serie sea correcta incluso con 
    números pequeños. La lógica que se usó aquí puede servir en otros programas donde se necesiten 
    cálculos paso a paso o generar patrones numéricos. Además, este proyecto refuerza buenas prácticas 
    de programación, como escribir documentación clara, mantener el código bien organizado y presentar 
    los resultados de forma ordenada. Todo esto ayuda a trabajar de manera más profesional en el 
    desarrollo de software.
"""
# Referencias
"""
    1. Hetland, M. L. (2017). Beginning Python: From Novice to Professional (3rd ed.). Apress.
    2. Love, J. (2019). Python for Beginners: Learn Python Programming. Independently Published.
    3. Downey, A. (2015). Think Python: How to Think Like a Computer Scientist (2nd ed.). O’Reilly Media.
    4. Python Software Foundation. (s. f.). Python documentation – Built-in Functions. https://docs.python.org/3/library/functions.html
    5. Real Python. (s. f.). Loops in Python: For, While, and Nested Loops. https://realpython.com/python-loops/
"""
