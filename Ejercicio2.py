#Se debe capturar la cantidad de pasajeros de cada uno de los 4 servicios que se
#realizan al día para los 5 días de la semana.

casadora = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def cantidadp ():
    for filas in range (0,4):
        print ("Servicio: ",filas+1)
        for columnas in range (0,5):
            print("Dia: ",columnas+1,end=". ")
            casadora [filas][columnas] = int(input("Ingrese la cantidad de pasajeros: "))

#Ya que el autobús tiene un capacidad máxima de 60 pasajeros, se debe verificar que
 #no se ingrese un valor mayor a 60.

def cantidadmax ():
    for filas in range (0,4):
        print ("Servicio: ",filas+1)
        for columnas in range (0,5):
            if casadora [filas][columnas] < 49:
                print("Dia",columnas+1,"capacidad adecuada")
            elif casadora [filas][columnas] < 59:
                print("Dia",columnas+1,"cerca del maximo de capacidad")
            elif casadora [filas][columnas] == 60:
                print("Dia",columnas+1,"al maximo de capacidad")
     
                

#El programa debe mostrar el promedio de pasajeros de cada uno de los días.

def promediodiario ():
    for filas in range (0,4):
        suma=0
        print ("Servicio: ",filas+1)
        for columnas in range (0,5):
            suma = suma  + casadora [filas][columnas]
        promedio = suma / 5
        print ("El promedio de pasajeros de cada uno de los dias es: ",promedio)

#El programa debe mostrar el promedio general de todos los días y todos los
# servicios.

def promediog ():
    suma=0
    for filas in range (0,4):
        print ("Servicio: ",filas+1)
        for columnas in range (0,5):
            suma = suma  + casadora [filas][columnas]
        promediogen = suma / 20
        print ("El promedio general de todos los pasajeros es de: ",promediogen)

#El programa debe mostrar el momento en que menos pasajeros se transportaron
#(servicio y día).

def encontrarmenos():
    menor_pasajeros=casadora[0][0]
    servicio_minimo=1
    dia_minimo=1
    for filas in range (0,4):
        for columnas in range (0,5):
            if casadora [filas][columnas] < menor_pasajeros:
                menor_pasajeros = casadora [filas][columnas]
                servicio_minimo=filas+1
                dia_minimo=columnas+1
                print ("El menor numero de pasajeros fue en el servicio: ",filas+1,servicio_minimo,"el dia: "columnas+1,dia_minimo," con menos pasajeros: ",menor_pasajeros)
    

    
                

            
               
        



            
            

#La captura de los datos y cada uno de los procesos que muestran información deben
#estar ubicados en su propio sub proceso.
#
 
     
            
                
                
            
    


cantidadp ()
cantidadmax ()
promediodiario ()
promediog ()
encontrarmenos()
