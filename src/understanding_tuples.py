#Tuples
"""
    Las tuplas son listas de elementos que no cambian de 
    tamaño. Las tuplas son INMUTABLES.

    Se utilizan los () para definir una tupla.
"""
rectangle_mesaures = (200, 50) # (Largo, ancho)
print(rectangle_mesaures[0])
print(rectangle_mesaures[1])

for mesaure in rectangle_mesaures:
    print(mesaure)

rectangle_mesaures = (300, 100)

"""
    No podemos modificar una tupla directamente, lo que si
    es cambiar la asignación a una variable que almacena
    una tupla.
"""