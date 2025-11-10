"""
Las listas tambien pueden almacenar numeros y de hecho, 
son ideales para esto. Python ofrece una gran cantidad
herramientas que ayudan a trabajar eficienciamente
listas de números.
"""
# Metodo built-in range()
"""
El metodo range() nos permite crear listas de numeros
de una manera facil y rapida.

Ejemplo: 
"""
print("numeros del 1 al 512:" )
for value in range(1, 513): # 10 numeros entre 1 y 513
    print(value)

print("numeros del 512 al 1024:")  
for value in range(512, 1025, 8): # 512 numeros entre 1 y 1024
    print(value)

for value in range(10):
    print(value)

square = []
for number in range(1, 21):
    print(square)