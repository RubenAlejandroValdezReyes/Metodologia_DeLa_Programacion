"""
| Un string es de manera sencilla una serie de caracteres. En python,
| todo lo que se encuentre dentro de comillas simples (' ') o dobles (" ")
| sera considerado un string.
Ejemplos:
| "Esto es un string"
| 'Esto es un string también'
' Le dije a un amigo "Python es mi lenguaje favorito" '
"El lenguaje 'Python' lleva el nombre por Monty Python, no por la serpiente"
"""
#Whitespaces
"""
|  Un whitespace se refiere a cualquier caracter que no se imprime, es decir 
|  espacio o tabulador Y finales de línea los Bowl Space se utilizan complemente 
|  para organizar la salida de tal manera que sea más amigable de leer o ver para 
|  el usuario.
| Ejemplo:
|  + Tabuladore: \t
|  + Salto de linea: \n
"""
print("whitesaces tabulador")
print("Python")
print("\tPython")
print("\t\tPython")

print("whitespaces salto de linea")
print("languuages: \nPython\cd:\nJavaScrips")
python01 =  " Python "
print(python01)
print(python01.rstrip())
print(python01.lstrip())
print(python01.strip())

# Syntax Error con strings
message = 'Una fortaleza de python es su comunidad' 
print(message)

first_name = "Taylor"
last_name = "Switf"
full_name = first_name + " " + last_name
print(full_name)
#f-strings
famous_Person = ""
message =  "una vez dijo me voy al oxxo en avion"

"""
Elige el nombre de uan persona famosa (quien quieras)
Elige una cita famosa de esa persona
Iguala ambos strings a una variable

1} Realiza la concatenación usando signo de suma
2} Realiza la concatenación usando f-strings
"""
