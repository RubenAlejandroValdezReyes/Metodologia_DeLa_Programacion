cars = ["audi", "bmw", "chevrolet", "corvette", "tesla"]
for car in cars:
    if car == "bmw" or car == "tesla" or car == "audi":
        print(car.upper())
    else:
        print(car)
    
# Condicionales: El condificional if se utiliza para 
# ejecutar un bloque de código si una condición es verdadera.



car =  ["bmm"]
print(car == "bmw")  # Esto imprimirá True si car es igual a "bmw"

car_2 = "audi"
print(car_2.lower()== "audi")  # Esto imprimirá True si car_2 es igual a "audi"

# Condicional != para verificar desigualdad
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

# Comparaciones numéricas
age = 18
print(age == 18)  # Igual a

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)  # Menor que
print(age <= 21) # Menor o igual que
print(age > 21)  # Mayor que
print(age >= 21) # Mayor o igual a

# Multiples condiciones
age_0 = 22
age_1 = 18
print("Multiples condiciones:")
print("Operación AND:")
print(age_0 >= 21 and age_1 >= 21)  # Ambas condiciones deben ser verdaderas
print(age_0 >= 21 and age_1 >= 18)

print("Operación OR:")
print(age_0 >= 21 or age_1 >= 21)   # Al menos una condición debe ser verdadera
print(age_0 >= 21 or age_1 >= 18)

# Como nos preguntan si un valor está en una lista
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)  # True    
print("pepperoni" in requested_toppings)  # False

# A value no está en una lista
banned_users = ["andrew", "carolina", "david, max, gabriel, quevedo"]
user = "marie"
print(user not in banned_users)  # Truedad

# Variables de tipo booleano
game_active = True
can_edit = False

"""
    If stantements
    
    If condition:
        Do something

    IF condition:
        So something True

        So something false
"""
#Preguntar edad del usuario
#Y decirle si tiene la edad
#Suficiente ara votar.
#Suficiente para vothar 
#imput(**) --> str
age = int(input("\nPlease enter your age: "))
print/f"Your age is: {age}")

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")           