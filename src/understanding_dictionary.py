# H
homer_0 = {"color": "yellow", "bag": "maggie_bag"}
print(homer_0)
print(type(homer_0))
marge = {"color": "yellow", "bag": "homer_chino", "headshot": 1.5, "hair": "blue", "dress": "green"}
gun = {"color": "yellow-orange", "headshot": 1.5}

print(marge["bag"])

covenant_grounts = {
    "color": "orange",
    "weapon": "plasma_gun",
    "armament": "plasma_granade",
    "health": 2,

}
covenant_Elite = {
    "color": "blue",
    "weapon": "energy_sword",
    "armament": "plasma_granade",
    "health": 7,
}
covenant_jackal = {
    "color": "gray",
    "weapon": "plasma_gun",
    "armament": "plasma_granade",
    "health": 5,
}
covenants = [
    covenant_grounts,
    covenant_Elite, 
    covenant_jackal
]

for covenant in covenants:
    print("\n", covenant)
    for key, value in covenant.items():
        print(key, value)

print("\n")
students = {
    "santiago": ["reprobado", "prepal", "rebelde"],
    "jorge-crack ": ["aprobado", "cbtis271", "irrespetuoso"],
    "gabriel": ["aprobado", "119muerte", "fornite"]
}

##Diccionarios en diccionarios
sensors = {
    "temperature": {
        "value": 23,
        "location": "aula 105"
        "id": "T-1000"
        "unit": "Celsius"
        },  
    "humidity": {
        "value": 60,
        "location": "aula 105"
        "id": "H-2000"
        "unit": "%"
        },
}
print("Temperatura")
print(sensors["temperature"]["value"])
print   
print(sensors["humidity"]["location"])