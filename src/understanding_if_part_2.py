
try:
    age = int(input("Escribe tu edad: "))
except:
    age = -1
    print("Hazte wey")

if age >= 100:
   print("Eres mayor de un siglo")
elif age >= 18 and age < 100:
    print("Eres mayor de edad")
elif age >= 0 and age < 18:
    print("Eres menor de edad")
else:
    print("Hazte Pendejo")


try:
    age = int(input("Escribe tu edad: "))
except:
    age = -1
    print("Hazte wey")

if age >= 18:
   print("El ocsto de la entrada es de $400")
elif age > 4 and age < 18:
    print("El costo de la entrada es de $200")
elif age >= 0 and age <= 4:
    print("Entrada gratuita")
else:
    print("No valido")

print("\n")


# Utilizar varias listas
guisos = ["salsa_verde", "asado", "desebrada", "barbacoa", "huevo_con_salchicha"]
pedido_1 = ["asado", "huevo_con_salchicha", "chorizo"] 
print("Que guisos quieres ordenar?")
for guiso in pedido_1:
    print(f"Deseo {guiso}")
    if guiso in guisos:
        print(f"Agregando {guiso} a tu orden.")
    else:
        print(f"Lo siento, no tenemos {guiso}.")
print("\nTu orden está lista.")