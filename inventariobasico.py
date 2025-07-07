
# Creamos un arreglo unidimensional (lista) para el inventario
inventario = [["Vacío", 0, 0.0] for _ in range(10)]  # Cada posición tiene: [nombre, cantidad, precio]

# Función para mostrar el inventario
def mostrar_inventario():
    print("\nInventario actual:")
    for i, item in enumerate(inventario):
        nombre, cantidad, precio = item
        print(f"Posición {i}: Producto: {nombre}, Cantidad: {cantidad}, Precio: {precio}")

# Función para agregar un producto al inventario
def agregar_producto(nombre, cantidad, precio):
    for i in range(len(inventario)):
        if inventario[i][0] == "Vacío":  # Busca la primera posición vacía
            inventario[i] = [nombre, cantidad, precio]
            print(f"Producto '{nombre}' agregado en la posición {i}.")
            return
    print("Error: El inventario está lleno. No se puede agregar más productos.")

# Función para eliminar un producto del inventario
def eliminar_producto(nombre):
    for i in range(len(inventario)):
        if inventario[i][0] == nombre:  # Busca el producto por su nombre
            inventario[i] = ["Vacío", 0, 0.0]  # Marca la posición como vacía
            print(f"Producto '{nombre}' eliminado del inventario.")
            return
    print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")

# Programa principal
while True:
    print("\nMenú del inventario:")
    print("1. Agregar producto")  # Cambiado como primera opción
    print("2. Mostrar inventario")
    print("3. Eliminar producto")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Introduce el nombre del producto: ")
        cantidad = int(input("Introduce la cantidad: "))
        precio = float(input("Introduce el precio: "))
        agregar_producto(nombre, cantidad, precio)
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        nombre = input("Introduce el nombre del producto que deseas eliminar: ")
        eliminar_producto(nombre)
    elif opcion == "4":
        print("Saliendo del programa. ¡Gracias!")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
