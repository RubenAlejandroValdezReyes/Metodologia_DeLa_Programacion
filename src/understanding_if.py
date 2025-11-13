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