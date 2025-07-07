#Las Tuercas F.C. cuenta con 25 jugadores en su planilla, cada uno de ellos recibe un
#salario mensual diferente y el equipo paga los salarios en efectivo.
#1.Por lo que le ha solicitado desarrollar un
# programa que reciba el salario de cada uno de los
#futbolistas.
#2. Posterior, debe informar cuál es el monto de
 #dinero que se debe retirar del banco y la denominación de
 #billetes y monedas necesaria para poder realizar el pago
 #exacto en efectivo.
# Considere las denominaciones de billetes y monedas
 #disponibles en nuestro país.

salarios = []
denominaciones = [50000,20000,10000,5000,2000,1000,500,100,50,25,10,5]

print ("Bienvenido al sistema de salarios")
for x in range (0,25):
    while True:
        salario = float(input("Ingrese el salario neto:" ))
        if salario > 0:
            salarios.append(salario)
            break
        else:
            print ("Ingrese monto positivo")

monto_salarios = sum (salarios)
print ("El monto a retirar del banco es de: ",monto_salarios,"colones")



print("Distribución de billetes y monedas por jugador:")

for i, salario in enumerate(salarios, 1):
    restante = salario
    print(f"\nJugador {i} - Salario: {salario:,.2f} colones")
    for denominacion in denominaciones:
        cantidad = int(restante // denominacion)
        if cantidad > 0:
            print(f"{cantidad} x {denominacion} colones")
        restante = round(restante % denominacion, 2)

    if restante > 0:
        print(f"Restante sin asignar: {restante:.2f} colones")



 
           







            
