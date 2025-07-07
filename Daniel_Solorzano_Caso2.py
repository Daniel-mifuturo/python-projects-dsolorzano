#Semana 13
#Caso Evaluado II
#Programador: Daniel Solorzano Damaceno

costo_viaje = 3850
viajesporsemana = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes"]

print ("Recaudación Semanal TRACOPA")
chofer = input ("Ingrese el nombre del conductor del autobus: ")

def Datosdeviajes ():
    for dia in range (5):
        print("\nDia: ",dias[dia])
        for viaje in range (3):
            while True:
                pasajeros = int(input("Ingrese la cantidad de pasajeros: "))                         
                if pasajeros < 55:
                    print("Dia",viaje+1,"capacidad adecuada")
                    viajesporsemana[dia][viaje] = pasajeros
                    break
                else:
                    print("Error de Dato")

def promediodiario ():
    for dia in range (5):
        suma=0
        print("\nDia: ",dias[dia])
        for viaje in range (3):
            suma = suma  + viajesporsemana[dia][viaje]
        promedio = suma / 3
        print("------------------------------------------------------------------------------------")
        print ("El promedio de pasajeros de cada uno de los dias es: ",promedio)
        
def calculos ():
    print("------------------------------------------------------------------------------------")
    print("Recaudación Semanal TRACOPA")
    print("Nombre del chofer: ",chofer)
    print("------------------------------------------------------------------------------------")
    total_semana = 0
    for dia in range(5):
        suma_dia = sum(viajesporsemana[dia])
        recaudacion_dia = suma_dia * costo_viaje
        total_semana += recaudacion_dia
        print (dias[dia] + ": " + str (recaudacion_dia) + " colones")

    print ("------------------------------------------------------------------------------------")
    print ("Total Semanal: " + str(total_semana) + " colones")
    print ("------------------------------------------------------------------------------------")          
                    
                        
Datosdeviajes ()
promediodiario ()
calculos ()                   
            
                    
                
            







