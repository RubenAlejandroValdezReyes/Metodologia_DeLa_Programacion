"""
Una list comprehention combina el ciclo for y la creacion de 
nuevos elementos en una sola linea y automaticamente agrega 
cada nuevo element a la lista, es decir, sin utilizar el 
metodo append.
"""
squares = [value**2 for value in range(0, 11)]

#Para los numeros pares entre 0 y 100
evens_range = [value for value in range (0, 101, 2)]

evens_if = [value for value in range (0, 101) if value % 2 == 0]
print(evens_if)