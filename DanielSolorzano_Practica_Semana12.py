#Daniel Solorzano Damaceno
#Practica de semana 12
#Ejercicio 1. Promedio de Notas

print("Bienvenido! Calculo de promedio de notas \n") #mensaje inicial
notas=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] #crear arreglo de 3x5

def ingresoDatos (): #creo la funcion de ingreso de informacion
    for x in range (0,3):
        print ("Programacion Basica Curso#",x+1)
        for y in range (0,5):
            print ("Estudiante",y+1,end=". ")
            notas [x][y] = int (input("Ingrese la nota: "))

def promediogeneral (): #creo la funcion de calculo de promedio
    sumatoria = 0
    for x in range (0,3):
        for y in range (0,5):
            sumatoria = sumatoria + notas [x][y]

    promedioG=sumatoria/15
    print ("El promedio de todos los cursos es de",promedioG)

def promediocurso (): #creo la funcion de calculo de promedio de c/u
    for x in range (0,3):
        sumatoria = 0
        for y in range (0,5):
                sumatoria = sumatoria + notas [x][y]
        promedioC=sumatoria/5
        print ("El promedio del curso#",x+1,"es de:",promedioC)

def aprobados (): #creo la funcion de estudiante aprobado
    for x in range (0,3):
        apro=0
        for y in range (0,5):
            if notas [x][y] >= 70:
                apro=apro+1
                          

                
        porcentaje=(apro*100)/5
        print ("El porcentaje de aprobados del curso,x+1",x+1,"es de:",porcentaje,"%")




ingresoDatos ()
promediogeneral ()
promediocurso()


