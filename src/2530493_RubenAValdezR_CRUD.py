"""
Alumno: Ruben Alejandro Valdez Reyes
Matrícula: 2530493
Grupo: IM 1-3
Docente: Carlos Antonio Tovar García
Escuela: Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Proyecto: CRUD, (Create, Read, Update, Delete) in-memory using Python functions
"""
# Resumen Ejecutivo
"""
El presente proyecto implementa un gestor CRUD (Create, Read, Update, Delete) en Python 
usando una lista de diccionarios para almacenar elementos en memoria. Cada operación está 
encapsulada en funciones separadas, permitiendo organizar y estructurar la lógica del programa 
de manera clara y reutilizable. El usuario puede crear nuevos ítems, consultar información, 
actualizar datos existentes y eliminar elementos según su identificador único. 
El programa valida entradas, maneja errores y muestra mensajes claros en inglés. 
Se destaca la importancia de separar responsabilidades, usar funciones para modularidad 
y garantizar que las operaciones de datos sean robustas y comprensibles.
"""
# Problema: Administrador CRUD en memoria con funciones
"""
    Programa que implementa un CRUD simple (Crear, Leer, Actualizar, Eliminar) para elementos almacenados en 
    una lista de diccionarios que utilizan funciones independientes y un menú basado en texto.
"""
# Entradas
"""
    Menu options (int)
    For CREATE/UPDATE: item_id (string), name (string), price (float), quantity (int)
    For READ/DELETE: item_id (string)
"""
# Salidas
"""
    Messages indicating the result of each operation:
    "Item created", "Item updated", "Item deleted", "Item not found", "Items list:"
"""
# Validaciones
"""
    Menu option must be valid
    item_id must not be empty
    price >= 0.0, quantity >= 0
    CREATE: id must not already exist
    READ/UPDATE/DELETE: id must exist
"""
# Casos de Uso
"""
    a. Normal: create item, read it, update it, delete it → expected messages and final state
    b. Border: create item with minimal data (quantity=0) → valid operation
    c. Error: invalid menu option or invalid id → expected error messages
"""
items = []

def find_item_index_by_id(item_id):
    for idx, item in enumerate(items):
        if item.get("id") == item_id:
            return idx
    return None


def validate_item_existence(item_id):
    index = find_item_index_by_id(item_id)
    return (index is not None, index)

def create_item(item_id, name, price, quantity):
    exists, _ = validate_item_existence(item_id)

    if exists:
        print("Error: item id already exists")
        return

    new_item = {
        "id": item_id,
        "name": name,
        "price": price,
        "quantity": quantity,
    }

    items.append(new_item)
    if new_item in items:
        print("Item created")
    else:
        print("Error: could not create item")


def read_item(item_id):
    exists, index = validate_item_existence(item_id)
    if not exists:
        print("Item not found")
        return

    item = items[index]
    print("Item found:", item)


def update_item(item_id, new_name, new_price, new_quantity):
    exists, index = validate_item_existence(item_id)
    if not exists:
        print("Item not found")
        return

    current_item = items[index]

    current_item["name"] = new_name
    current_item["price"] = new_price
    current_item["quantity"] = new_quantity

    print("Item updated")


def delete_item(item_id):
    exists, index = validate_item_existence(item_id)
    if not exists:
        print("Item not found")
        return

    removed = items.pop(index)
    if removed:
        print("Item deleted")
    else:
        print("Error: could not delete item")


def list_items():
    if len(items) == 0:
        print("No items in the list")
        return

    print("Items list:")
    for it in items:
        print(it)

def input_float(prompt):
    text = input(prompt)
    try:
        num = float(text)
        if num < 0:
            raise ValueError
        return num
    except:
        print("Error: invalid input")
        return None


def input_int(prompt):
    text = input(prompt)
    try:
        num = int(text)
        if num < 0:
            raise ValueError
        return num
    except:
        print("Error: invalid input")
        return None

def print_menu():
    print("\nMenu:")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")


def main():
    while True:

        print_menu()
        option = input("Select an option: ").strip()

        if option == "1":
            item_id = input("Enter item id: ").strip()
            name = input("Enter item name: ").strip()
            price = input_float("Enter price: ")
            quantity = input_int("Enter quantity: ")

            if item_id and name and price is not None and quantity is not None:
                create_item(item_id, name, price, quantity)
            else:
                print("Error: invalid input")

        elif option == "2":
            item_id = input("Enter item id to read: ").strip()
            if item_id:
                read_item(item_id)
            else:
                print("Error: invalid input")

        elif option == "3":
            item_id = input("Enter item id to update: ").strip()

            if not item_id:
                print("Error: invalid input")
                continue

            new_name = input("Enter new name: ").strip()
            new_price = input_float("Enter new price: ")
            new_quantity = input_int("Enter new quantity: ")

            if new_name and new_price is not None and new_quantity is not None:
                update_item(item_id, new_name, new_price, new_quantity)
            else:
                print("Error: invalid input")

        elif option == "4":
            item_id = input("Enter item id to delete: ").strip()
            if item_id:
                delete_item(item_id)
            else:
                print("Error: invalid input")

        elif option == "5":
            list_items()

        elif option == "0":
            print("Exiting program")
            break

        else:
            print("Error: invalid input")


if __name__ == "__main__":
    main()


# Conclusiones
"""
Usar funciones para cada operación del CRUD hizo que el programa fuera más ordenado y que el código se pudiera 
reutilizar sin problema. Se utilizó una lista de diccionarios para guardar y manejar los datos de forma eficiente, 
y cada elemento se puede identificar fácilmente gracias a su ID único. Las validaciones ayudan a evitar errores 
al ingresar información y garantizan que todas las acciones se hagan correctamente. Además, el menú interactivo 
permite que el usuario realice todas las operaciones de manera sencilla. Este CRUD, que trabaja solo con datos 
en memoria, puede ampliarse sin dificultad para guardar información en archivos o incluso en bases de datos más 
completas, mostrando lo flexible que puede ser la programación modular en Python.
"""
# Referencias
"""
1. Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). Data Structures and Algorithms in Python. Wiley. 
2. McKinney, W. (2018). Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython. O’Reilly Media. 
3. Barry, P. (2016). Head First Python: A Brain-Friendly Guide. O’Reilly Media. 
4. Shaw, Z. A. (2013). Learn Python the Hard Way. Addison-Wesley. 
5. Beazley, D., & Jones, B. (2013). Python Cookbook: Recipes for Mastering Python 3. O’Reilly Media. 
"""

