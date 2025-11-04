# Listas
"""
Las listas son elementos mutables.
Las listas nos permiten almacenar información en un lugar, la cantidad
que tenga: ya sean poco elementos o millones de elementos.

Se recomienda nombrar una variable de tipo lista en plural.

En python los corchetes [], definen una linea de sus elementos van separados por comas.

Ejemplos:
"""

bycycles = 'trek', 'canondale', 'redline', 'specialized', 'gigant'
[[print(bycycles)], title()]

print(bycycles [4]. title())

print(bycycles[-1].title())
print(bycycles[-2].title())
print(bycycles[-5].title())

message = "Mi primer bicicleta fue una " + bycycles[4].upper() + "."
print(message)

message_f = f"Mi primer bicicleta fue una {bycycles[4].title[]}."
print(message_f)

print("\n")
print("Aregar elementos a la lista:")
print(bycycles)

print("Metodos de las listas agregar elementos: list_name.append(element)")
bycycles.append("ducatti")
print(bycycles)
