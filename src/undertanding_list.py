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
print(bycycles) 
print(bycycles[0].title())

print(bycycles[4]. title())

print(bycycles[-1].title())
print(bycycles[-2].title())
print(bycycles[-5].title())

message = "Mi primer bicicleta fue una " + bycycles[4].upper() + "."
print(message)

message_f = f"Mi primer bicicleta fue una {bycycles[4].title()} ."
print(message_f)

print("\n")
print("Aregar elementos a la lista:")
print(bycycles)

print("Metodos de las listas agregar elementos: list_name.append(element)")
print(bycycles)

# LISTAS A-105
"""
Metodo append
|   
|   
|   
"""
print("\n--- Agregar elementos a una lista append() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) 
motorcycles.append('bmw')
motorcycles.insert(1, 'ducati')
print(motorcycles)  



print("\n--- Eliminar elementos de una lista ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
first_motorcycle = motorcycles.pop(1)
print("La primera motocicleta que tuve fue una " + first_motorcycle.title() + ".")

"""
Ordenar permanentemente
-sort(): ordena la lista de manera permanente
"""
print("\n--- Ordenar permanentemente una lista sort() ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']  
print(motorcycles)
motorcycles.sort()
print(motorcycles)
print("\n")
motorcycles.sort(reverse=True)
print(motorcycles)

students = ["josue", "victor", "ana", "mike", "paulo", "gerardo"]
print(students)
desired_students = input("Elige estudiante a eliminar: ")
students.remove(desired_students.strip().lower())
print(students)