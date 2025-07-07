#Proyecto Entrega final
#Tema: Inventario y facturación de una tienda de implementos deportivos
#Universidad Fidélitas
#Curso de programación básica
#Estudiante: Daniel Solórzano Damaceno
#Profesor: Olmán Coto

#•Variables globales, almacenan los precios por unidad de cada producto.
#•Un total de 5 variables con los nombres: uniformes, espinilleras, tacos, balon y medias.
uniformes = 15000
espinilleras = 9950
tacos = 55000
balon = 11950
medias = 2500

#•Listas y arreglo bidimensional:
#•En esta sección almacenáremos los datos resultantes de los siguientes módulos:
#•inicio de sesión, registro, venta de paquetes, horario de atención, productos y usuarios válidos. 

datosclientes = []
ventas_paquetes = []
venta_productos = []
horarios_seleccionados =[]
usuarios_validos = [["Olman", "455"],["Daniel", "466"]]

#1. Módulo de Inicio de sesión:
#• Crear un mensaje de bienvenida al sistema. 
#• Solicita el nombre de usuario y clave.  
#• Realiza la validación de los usuarios autorizados y contraseñas.
#• A la hora de realizar la validación, el programa recorre la lista con arreglo bidimensional para validar los datos.
#• Solo se permiten 3 intentos de ingreso, si los datos son incorrectos al tercer intento sale del programa.
#• El programa muestra un conteo de intentos en la consola luego de cada intento fallido. 
#• Para crear este módulo se utilizaron estructuras de control como: if, y estructuras repetitivas como while y for. Operadores relacionales y operadores lógicos.
#Usuario1: Olman y contraseña: 455
#Usuario2: Daniel y contraseña: 466

print("-----------------------------------------------------------------------------------------")
print ("\nBienvenido al sistema de Inventario y facturación\n")
print("-----------------------------------------------------------------------------------------")
print("\nTienda de implementos deportivos la buena compra\n")
print("-----------------------------------------------------------------------------------------")
def inicio_sesion ():
    intentos = 0
    while intentos < 3:
        print ("\nIncio de sesión\n")
        print("-----------------------------------------------------------------------------------------")
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input ("Ingrese su contraseña: ")
        for u, c in usuarios_validos:
            if usuario == u and contraseña == c:
                print("-----------------------------------------------------------------------------------------")
                print("\nInicio de sesión completado exitosamente\n")
                print("-----------------------------------------------------------------------------------------")
                return "éxito"
        intentos += 1
        print("-----------------------------------------------------------------------------------------")
        print("\nAcceso Denegado. Máximo de Intentos 3, Intento#: ",intentos,"\n")
        print("-----------------------------------------------------------------------------------------")
    return "fallo"

#2. Módulos de registro:
#• Permite al usuario ingresar la información en el módulo de registro:
#• Nombre completo 
#• Cedula 
#• Celular 
#• Correo 
#• Dirección
#• Luego los datos resultantes son almacenados en una lista.
             
def registro ():
    print ("\nRegistro\n")
    print("-----------------------------------------------------------------------------------------")
    print ("\nIngrese la siguiente información del cliente:\n")
    print("-----------------------------------------------------------------------------------------")
    nombre = input ("Ingrese el nombre completo del cliente: ")
    ced = input ("Ingrese el número de cédula del cliente y use el formato de ingreso. Ejemplo: 1-2222-3333: ")
    tel = input ("Ingrese el número de teléfono celular del cliente y use el formato de ingreso. Ejemplo: 506-2222-3333: ")
    email = input ("Ingrese el email del cliente: ")
    direccion = input ("Ingrese la dirección del cliente: ")
    print("-----------------------------------------------------------------------------------------")
    print ("\nRegistro exitoso! \n")
    print("-----------------------------------------------------------------------------------------")
    datosclientes.append([nombre, ced, tel, email, direccion])

#3. Módulo de venta de paquetes.
#• Crea 4 paquetes de venta de productos seleccionados, con su respectivo costo y descuento.
#• Permite que el usuario seleccione un paquete del módulo, luego el programa solicitará al usuario que ingrese la cantidad de productos que desea comprar.
#• Luego de ingresar la cantidad, el programa realiza el cálculo del costo del paquete realizando las operaciones aritméticas de suma y multiplicación. 
#• Para crear este módulo se utilizaron estructuras de control como: if, elif y else. Operadores relacionales y operadores aritméticos.
#• Los datos resultantes son almacenados en una lista.
#• Si el usuario entra una opción que no es válida en la selección, el programa mostrará un mensaje de error y regresará al menú principal.
#• Luego de realizar un pedido en este módulo, el programa mostrará el nombre del paquete comprado, la cantidad y total de la compra. 
    
def venta_de_paquetes ():
    print("-----------------------------------------------------------------------------------------")
    print("\nVenta de paquetes\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nVenta de paquetes de productos selecionados y incluyen descuentos desde 5% hasta 20%.")
    print("Todos nuestros paquetes se encuentran en oferta\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nSeleccione uno de los siguientes paquetes: \n")    
    print("-----------------------------------------------------------------------------------------")
    print("\nPaquete 1: Un conjunto de uniforme de futbol, un par de espinilleras, un par de tacos de futbol,")
    print("un balón de futbol, calcetines de futbol e incluye 20% de descuento\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nPaquete 2: Un conjunto de uniforme de futbol, un par de tacos de futbol, un balón de futbol,")
    print("un par de espinilleras e incluye 15% de descuento\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nPaquete 3: Un balón de fútbol, un par espinilleras, tacos de futbol e incluye 10% de descuento\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nPaquete 4: Un par de tacos de futbol, un balón de futbol e incluye 5% de descuento\n")
    print("-----------------------------------------------------------------------------------------")
    paquete = int(input("Digite el número del paquete que deseas adquirir y luego agregue la cantidad de paquetes que desea comprar: "))
    if paquete == 1:
        qty = int(input("Ingrese la cantidad de paquetes que quiere comprar: "))
        package = "Paquete 1 Comprado| Un conjunto de uniforme de futbol, un par de espinilleras, un par de tacos de futbol, un balón de futbol, calcetines de futbol e incluye 20% de descuento"
        print("-----------------------------------------------------------------------------------------")
        print (package)
        print ("\nCantidad: ",qty)
        print("-----------------------------------------------------------------------------------------")
        subtotal = uniformes + espinilleras + tacos + balon + medias
        subtotal = subtotal * qty
        descuento = subtotal * 0.20
        precio_descuento = subtotal - descuento
        iva = precio_descuento * 0.13
        total = precio_descuento + iva
        ventas_paquetes.append([package, qty, descuento, subtotal, precio_descuento, iva, total])
        print ("\nGracias por su compra. Total: ",total,"CRC.\n")
        print("-----------------------------------------------------------------------------------------")
    elif paquete == 2:
        qty = int(input("Ingrese la cantidad de paquetes que quiere comprar: "))
        package = "Paquete 2 Comprado | Un conjunto de uniforme de futbol, un par de tacos de futbol, un balón de futbol, un par de espinilleras e incluye 15% de descuento"
        print("-----------------------------------------------------------------------------------------")
        print (package)
        print ("\nCantidad: ",qty)
        print("-----------------------------------------------------------------------------------------")
        subtotal = uniformes + espinilleras + tacos + balon
        subtotal = subtotal * qty
        descuento = subtotal * 0.15
        precio_descuento = subtotal - descuento
        iva = precio_descuento * 0.13
        total = precio_descuento + iva
        ventas_paquetes.append([package, qty, descuento, subtotal, precio_descuento, iva, total])
        print ("\nGracias por su compra. Total: ",total,"CRC.\n")
        print("-----------------------------------------------------------------------------------------")
    elif paquete == 3:
        qty = int(input("Ingrese la cantidad de paquetes que quiere comprar: "))
        package = "Paquete 3 Comprado | Un balón de fútbol, un par espinilleras, tacos de futbol e incluye 10% de descuento"
        print("-----------------------------------------------------------------------------------------")
        print (package)
        print ("\nCantidad: ",qty)
        print("-----------------------------------------------------------------------------------------")
        subtotal = espinilleras + tacos + balon
        subtotal = subtotal * qty
        descuento = subtotal * 0.10
        precio_descuento = subtotal - descuento
        iva = precio_descuento * 0.13
        total = precio_descuento + iva
        print ("\nGracias por su compra. Total: ",total,"CRC.\n")
        print("-----------------------------------------------------------------------------------------")
        ventas_paquetes.append([package, qty, descuento, subtotal, precio_descuento, iva, total])
    elif paquete == 4:
        qty = int(input("Ingrese la cantidad de paquetes que quiere comprar: "))
        package = "Paquete 4 Comprado | Un par de tacos de futbol, un balón de futbol e incluye 5% de descuento"
        print (package)
        print ("\nCantidad: ",qty)
        print("-----------------------------------------------------------------------------------------")
        subtotal = espinilleras + tacos + balon
        subtotal = subtotal * qty
        descuento = subtotal * 0.05
        precio_descuento = subtotal - descuento
        iva = precio_descuento * 0.13
        total = precio_descuento + iva
        print ("\nGracias por su compra. Total: ",total,"CRC.\n")
        print("-----------------------------------------------------------------------------------------")
        ventas_paquetes.append([package, qty, descuento, subtotal, precio_descuento, iva, total])
    else:
        print ("\nOpción seleccionada no existe. Realiza una nueva selección")
        print("-----------------------------------------------------------------------------------------")

#4. Módulo de horario de atención:
#• Este módulo permite al usuario seleccionar entre 3 diferentes opciones de horario por medio de un número y los datos resultantes son almacenados en una lista.
#• Para crear este módulo se utilizaron estructuras de control como: if, elif y else, y operadores relacionales.
#• Si el usuario entra una opción que no es válida en la selección, el programa mostrará un mensaje de error y regresará al menú principal.
#• Luego de realizar un pedido en este módulo, el programa mostrará un mensaje con la opción seleccionada. 

def horario_de_atención ():
    print("-----------------------------------------------------------------------------------------")
    print("\nHorarios de ateción\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nTrabajamos 24/7. Nuestros horarios de ateción al cliente aparecen en el siguiente ménu: \n")
    print("-----------------------------------------------------------------------------------------")
    print("\nSeleccione una opción de horario: \n")
    print("-----------------------------------------------------------------------------------------")
    print("\n1. Horario matutino: 6:00 am a 3:00 pm\n")
    print("-----------------------------------------------------------------------------------------")
    print("\n2. Horario de tarde: 3:00 pm a 10:00 pm\n")
    print("-----------------------------------------------------------------------------------------")
    print("\n3. Horario nocturno: 10:00 pm a 6:00 am\n")
    print("-----------------------------------------------------------------------------------------")
    horario = int (input("Digite la opción de horario que desea seleccionar el cliente: "))     
    if horario == 1:
        horario_dato = "Matituno 6:00 am a 3:00pm"
        print("-----------------------------------------------------------------------------------------")
        print("\nOpción 1 Seleccionada\n")
        print("-----------------------------------------------------------------------------------------")
        horarios_seleccionados.append (horario_dato)
    elif horario == 2:
        horario_dato = "Tarde 3:00 pm a 10:00pm"
        print("-----------------------------------------------------------------------------------------")
        print("\nOpción 2 Seleccionada\n")
        print("-----------------------------------------------------------------------------------------")
        horarios_seleccionados.append (horario_dato)
    elif horario == 3:
        horario_dato = "Nocturno 10:00 pm a 6:00am"
        print("-----------------------------------------------------------------------------------------")
        print("\nOpción 3 Seleccionada\n")
        print("-----------------------------------------------------------------------------------------")
        horarios_seleccionados.append (horario_dato)
    else:
        print("-----------------------------------------------------------------------------------------")
        print("Opción seleccionada no existe. Realiza una nueva selección")
        
    
#5. Módulo de productos
#• El usuario puede seleccionar entre 5 productos diferentes seleccionándolo mediante un número.
#• Permite que el usuario seleccione un producto del módulo, luego el programa solicitará al usuario que ingrese la cantidad de productos que desea comprar.
#• Luego de ingresar la cantidad, el programa realiza el cálculo del costo del paquete realizando las operaciones aritméticas de suma y multiplicación.
#• Los datos resultantes son almacenados en una lista.
#• Para crear este módulo se utilizaron estructuras de control como: if, elif y else. Operadores relacionales y operadores aritméticos.
#• Si el usuario entra una opción que no es válida en la selección, el programa mostrará un mensaje de error y regresará al menú principal.
#• Luego de realizar un pedido en este módulo, el programa mostrará el nombre del producto comprado, la cantidad y total de la compra.
        
def Productos ():
    print("-----------------------------------------------------------------------------------------")
    print("\nProductos\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nSeleccione uno de los siguientes productos: \n")
    print("-----------------------------------------------------------------------------------------")
    print("\n1. Conjunto de uniforme de fútbol y su costo es de 15000 CRC por unidad\n")
    print("-----------------------------------------------------------------------------------------")
    print("\n2. Espinelleras y su costo es de 9950 CRC por unidad\n" )
    print("-----------------------------------------------------------------------------------------")
    print("\n3. Tacos de fútbol y su costo es de 55000 CRC por unidad\n")
    print("-----------------------------------------------------------------------------------------")
    print("\n4. Balón de fútbol y su costo es de 11950 CRC por unidad\n")
    print("-----------------------------------------------------------------------------------------")
    print("\n5. Calcetines de fútbol y su costo es de 2500 CRC por unidad\n")
    print("-----------------------------------------------------------------------------------------")
    producto = int(input("Digite el número del producto que desea adquirir: "))
    if producto == 1:
        qty1 = int(input("Ingrese la cantidad de productos que quiere comprar: "))
        producto = "Producto 1 Comprado | Conjunto de uniforme de fútbol"
        print("-----------------------------------------------------------------------------------------")
        print (producto)
        print ("\nCantidad: ",qty1)
        print("-----------------------------------------------------------------------------------------")
        subtotal1 = uniformes
        subtotal1 = subtotal1 * qty1
        iva1 = subtotal1 * 0.13
        total1 = subtotal1 + iva1
        venta_productos.append([producto, qty1, subtotal1, iva1, total1])
        print ("\nGracias por su compra. Total: ",total1,"CRC.\n")
        print("-----------------------------------------------------------------------------------------")
    elif producto == 2:
        qty1 = int(input("Ingrese la cantidad de productos que quiere comprar: "))
        producto = "Producto 2 Comprado | Espinilleras"
        print("-----------------------------------------------------------------------------------------")
        print (producto)
        print ("\nCantidad: ",qty1)
        print("-----------------------------------------------------------------------------------------")
        subtotal1 = espinilleras
        subtotal1 = subtotal1 * qty1
        iva1 = subtotal1 * 0.13
        total1 = subtotal1 + iva1
        venta_productos.append([producto, qty1, subtotal1, iva1, total1])
        print ("\nGracias por su compra. Total: ",total1,"CRC.\n")
        print("-----------------------------------------------------------------------------------------")
    elif producto == 3:
        qty1 = int(input("Ingrese la cantidad de productos que quiere comprar: "))
        producto = "Producto 3 Comprado | Tacos de fútbol"
        print("-----------------------------------------------------------------------------------------")
        print (producto)
        print ("\nCantidad: ",qty1)
        print("-----------------------------------------------------------------------------------------")
        subtotal1 = tacos
        subtotal1 = subtotal1 * qty1
        iva1 = subtotal1 * 0.13
        total1 = subtotal1 + iva1
        venta_productos.append([producto, qty1, subtotal1, iva1, total1])
        print ("\nGracias por su compra. Total: ",total1,"CRC.\n")
        print("-----------------------------------------------------------------------------------------")
    elif producto == 4:
        qty1 = int(input("Ingrese la cantidad de productos que quiere comprar: "))
        producto = "Producto 4 Comprado | Balón de fútbol"
        print("-----------------------------------------------------------------------------------------")
        print (producto)
        print ("\nCantidad: ",qty1)
        print("-----------------------------------------------------------------------------------------")
        subtotal1 = balon
        subtotal1 = subtotal1 * qty1
        iva1 = subtotal1 * 0.13
        total1 = subtotal1 + iva1
        venta_productos.append([producto, qty1, subtotal1, iva1, total1])
        print ("\nGracias por su compra. Total: ",total1,"CRC.\n")
        print("-----------------------------------------------------------------------------------------")
    elif producto == 5:
        qty1 = int(input("Ingrese la cantidad de productos que quiere comprar: "))
        producto = "Producto 5 Comprado | Calcetines de fútbol"
        print("-----------------------------------------------------------------------------------------")
        print (producto)
        print ("\nCantidad: ",qty1)
        print("-----------------------------------------------------------------------------------------")
        subtotal1 = medias
        subtotal1 = subtotal1 * qty1
        iva1 = subtotal1 * 0.13
        total1 = subtotal1 + iva1
        venta_productos.append([producto, qty1, subtotal1, iva1, total1])
        print ("\nGracias por su compra. Total: ",total1,"CRC.\n")
        print("-----------------------------------------------------------------------------------------")
    else:
        print("\nOpción seleccionada no existe. Realiza una nueva selección\n")
        print("-----------------------------------------------------------------------------------------")

#6. Módulo de historial
#• El usuario puede visualizar la información capturada en los módulos anteriores como el registro, venta de paquetes, horarios de atención y productos.
#• Luego la información es desplegada en la consola. 
#• Para crear este módulo se utilizaron estructuras de control como: if, elif y else, operadores relacionales, y la estructura repetitiva: for
#• Regresá al menú principal.
   
def historial ():
    print("-----------------------------------------------------------------------------------------")
    print("\nHistorial\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nHistórico de información capturada en el programa\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nHorario de atención: \n")
    print(*horarios_seleccionados)
    print("\n-----------------------------------------------------------------------------------------")
    for cliente in datosclientes:
        print("\nDatos del cliente: ")
        print("\n-----------------------------------------------------------------------------------------")
        print("\nNombre: " + cliente[0]+" | Cédula: " + cliente[1] +
              " | Teléfono: " + cliente[2] + " | Email: " + cliente[3] +
              " | Dirección: " + cliente[4] + "\n")  
        print("-----------------------------------------------------------------------------------------")
        print("\nDetalles de ventas:\n")
        print("-----------------------------------------------------------------------------------------")    
    for datosdepaquete in ventas_paquetes:            
        print("\nNombre: " + datosdepaquete[0] + " | Cantidad: " + str(datosdepaquete[1]) +
      " | Descuento: " + str(datosdepaquete[2]) + " CRC | Subtotal: " + str(datosdepaquete[3]) + "CRC"
      " | Precio con descuento aplicado: " + str(datosdepaquete[4]) + " CRC  |  IVA: " + str(datosdepaquete[5]) +
                             " CRC  |  Total: " + str(datosdepaquete[6]) + " CRC \n")  
    for datosdeproducto in venta_productos:            
        print("\nNombre: " + datosdeproducto[0] + " | Cantidad: " + str(datosdeproducto[1]) +
      " | Subtotal: " + str(datosdeproducto[2]) + " CRC | IVA: " + str(datosdeproducto[3]) + "CRC"
      " | Total: " + str(datosdeproducto[4]) + " CRC \n")
                             
       
#7. Módulo de facturación
#• El usuario será capaz de imprimir una factura por la venta paquetes y productos.
#• La factura incluye la siguiente información: horario de atención, nombre del cliente, cédula, teléfono celular, email, dirección, total, subtotal, IVA,
#• descuento, cantidad, nombre del producto o paquete.       
#• El módulo realiza la suma de la venta de productos y paquetes para obtener el resultado final de la factura.            
#• Para crear este módulo se utilizaron estructuras de control como: if, elif y else, operadores relacionales, y la estructura repetitiva: for.
#• Regresá al menú principal.

def facturación ():
    print("-----------------------------------------------------------------------------------------")
    print("\nTienda de implementos deportivos La Buena Compra\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nFactura de compra\n")
    print("-----------------------------------------------------------------------------------------")
    print("\nHorario de atención: \n")
    print(*horarios_seleccionados)
    print("\n-----------------------------------------------------------------------------------------")
    print("\nDatos del cliente: ")
    print("\n-----------------------------------------------------------------------------------------")
    for cliente in datosclientes:
        print("\nNombre: " + cliente[0]+" | Cédula: " + cliente[1] +
        " | Teléfono: " + cliente[2] + " | Email: " + cliente[3] +
        " | Dirección: " + cliente[4] + "\n")
        print("-----------------------------------------------------------------------------------------")
    total_productos=0
    total_paquetes=0
    print("\nDetalles de venta: \n")
    print("-----------------------------------------------------------------------------------------")
    for datosdepaquete in ventas_paquetes:
        print("\nNombre: " + datosdepaquete[0] + " | Cantidad: " + str(datosdepaquete[1]) +
      " | Descuento: " + str(datosdepaquete[2]) + " CRC | Subtotal: " + str(datosdepaquete[3]) + " CRC "
      " | Precio con descuento aplicado: " + str(datosdepaquete[4]) + " CRC  |  IVA: " + str(datosdepaquete[5]) +
        " CRC  |  Total: " + str(datosdepaquete[6]) + " CRC \n")    
    for datosdeproducto in venta_productos:
        print("\nNombre: " + datosdeproducto[0] + " | Cantidad: " + str(datosdeproducto[1]) +
      " | Subtotal: " + str(datosdeproducto[2]) + " CRC | IVA: " + str(datosdeproducto[3]) + " CRC "
      " | Total: " + str(datosdeproducto[4]) + " CRC \n")
    total_productos += datosdeproducto[4]    
    total_paquetes += datosdepaquete[6]
    resultado = total_productos+total_paquetes
    print("-----------------------------------------------------------------------------------------")
    print("Total: " + str (resultado) + " CRC \n")
    print("Gracias por su compra y lo esperamos pronto de nuevo.")
    print("-----------------------------------------------------------------------------------------")                
                
#8. Módulo de menú principal
#• Este menú de opciones le permite al usuario seleccionar una opción por medio de un número, las funciones a escoger del programa son las siguientes
#• inicio de sesión, registro, venta de paquetes, horario de atención, productos, historial, facturación y ofrece la opción salir para finalizar el programa.
#• Muestra un mensaje de agradecimiento al final.
#• Si el usuario entra una opción que no es válida en la selección, el programa mostrará un mensaje de error y regresará al menú principal.
#• Para crear este módulo se utilizaron estructuras de control como: if, elif y else, operadores relacionales, operadores lógicos y la estructura repetitiva: while.

def menu_principal ():
    while True:
        print("\nMénu Principal\n")
        print("-----------------------------------------------------------------------------------------")
        print("\nElige el número que deseas seleccionar:\n")
        print("-----------------------------------------------------------------------------------------")
        print("1. Venta de paquetes")
        print("2. Horario de atención")
        print("3. Productos")
        print("4. Historial")
        print("5. Facturación")
        print("6. Salir")
        option = int(input("Digita el número que deseas elegir: "))
        if option == 1:
            venta_de_paquetes ()
        elif option == 2:
            horario_de_atención ()
        elif option == 3:
            Productos ()
        elif option == 4:
            historial ()
        elif option == 5:
            facturación()
        elif option == 6:
            print("Cerrando el sistema. Gracias por su visita y lo esperamos pronto de nuevo")
            break
        else:
            print("-----------------------------------------------------------------------------------------")
            print("\nOpción invalida. Realiza una nueva selección\n")
            print("-----------------------------------------------------------------------------------------")

#9. Programa principal
#•Realiza una validación del inicio de sesión, si el retorno de la validación es "éxito", el usuario fue validado correctamente
#•y permite que el usuario entre en el módulo de registro y menú principal.
#•El resultado del inicio de sesión es almacenado en la variable de nombre: usuariovalidado.
#•Si el retorno de inicio de sesión no es validado, despliega un mensaje de error y sale del programa.       
#•Para crear el programa principal se utilizaron estructuras de control como: if, y operadores relacionales.
#•Realiza el llamado de los módulos de inicio de sesión, registro y menú principal.

usuariovalidado = inicio_sesion()
if usuariovalidado == "éxito":
    registro ()
    menu_principal()        
        
else:
    print("\nAcceso Denegado! Máximo de intentos alcanzado\n")
