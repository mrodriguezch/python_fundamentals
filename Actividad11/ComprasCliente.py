#actividad básica
print("="*50,"\nBásica\n","="*50)

total = 0
print("Ingrese 0 para terminar")
monto = float(input("Ingrese el monto del articulo: "))
while monto != 0:
    if monto>0:
        total+=monto
    monto = float(input("Ingrese el monto del articulo: "))
if total>=1000:
    total*=0.9
    print("Recibio un 10% de descuento. Su total a pagar es: {0}".format(total))
else:
    print("Su total a pagar es: {0}".format(total))


#actividad avanzada
print("="*50,"\nAvanzada\n","="*50)

print("="*50)
print("Costo primera hora: $25")
print("Costo hora(o fracción) adicional: $15")
print("Tarifa extra por 8 o más horas: $200")
print("="*50)
minutos = 0
costo = 0
print("Ingrese 0 para terminar")
tiempo = float(input("Ingrese los minutos dentro del estacionamiento: "))
while tiempo != 0:
    if tiempo>0:
        minutos+=tiempo
    tiempo = float(input("Ingrese los minutos dentro del estacionamiento: "))

#si el tiempo es mayor a 8 horas
if minutos>8*60:    
    costo=25+(minutos-1)//60*15+200
    print("Su total a pagar por {1}hrs es: {0}".format(costo, minutos/60))
#si el tiempo es mayor a 1 hora
elif minutos>1*60:
    costo=25+(minutos-1) //60 * 15
    print("Su total a pagar por {1}hrs es: {0}".format(costo, minutos/60))
else:
    costo=25
    print("Su total a pagar por {1}hrs es: {0}".format(costo, minutos/60))





