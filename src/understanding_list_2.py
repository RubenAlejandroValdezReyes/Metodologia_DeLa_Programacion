"""
 slicing a list
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("lista Original: ", players)

print("slice de lista original: ", players[0:3])
print("slice de lista original: ", players[1:4])
print("slice de lista original: ", players[:4])
print("slice de lista original: ", players[2:])
print("slice de lista original: ", players[-3:])
print("slice de lista original: ", players[5:2])
print("slice de lista original: ", players[-3:-1])

"""
Slicing en un for
"""
players = []

"""
Copiando una lista
"""
my_foods = ["pizza", "tacos", "totopos", "flautas", "gorditas", "pollo feliz"]
#my_foods_copy = my_foods 
#Error: esta no es la manera de copiar una lista
my_foods_1 = my_foods[:]
my_foods_2 = my_foods.copy()
my_foods_3 - list(my_foods)