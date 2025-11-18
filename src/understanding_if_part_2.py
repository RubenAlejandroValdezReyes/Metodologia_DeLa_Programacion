
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