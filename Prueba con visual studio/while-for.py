# Un peaje ed la ciudad quiere que ud sistematice el control del pago de los peajes. Por este pasan tres tipos de automotores.
#1. Autos
#2. Camiones
#3. Tractomulas
#No se sabe cuántos de estos pasan al día por el peaje, pero cunado el día finaliza se registra un tipo de automotor cero. El cobro por cada tipo de automotor es el siguiente:
#Tipo valor:
#1. Auto $3.50
#2. Camion $ 12.0
#3.Tractomula $16.0

#Desarrolle un programa en python donde conociendo el tipo de automotor se determine que:
#   * El valor a pagar por cada automotor que pase por el peaje
#   * Total recaudado por día
#   * Total recaudado por automotor
#   * Cuál es el tipo de automotor que mas transita por el peaje

automotores = ['Autos', 'Camiones', 'Tractomulas']
precios = [3.5, 12.0, 16.0]
count = [0,0,0]
acumu = [0,0,0]
ingreso = int(input("Ingrese el tipo de automotor: "))

while ingreso !=0:

    if (ingreso<=len(automotores)):
        precio=precios[ingreso - 1]         # le resto 1 para identificar el lugar de la lista
        print('El precio que debe pagar es: ${:.2f}'.format(precio))
        count[ingreso-1]+=1                 # lo indexo en la lista de count2
        acumu[ingreso-1]+=precio            # lo indexo en la lista de acumu2
    
    else:
        print('Error de ingreso')

    ingreso = int(input("Ingrese el tipo de automotor: ")) # hago el ingreso de otro vehículo o finalizo el día

for i in range(len(automotores)):
    auto=automotores[i]
    acumuT=acumu[i]
    print('El acumulado de {} es de: ${}'.format(auto, acumuT))

totalDia=sum(acumu)
print('El total acumulado del día es: ${:.2f}'.format(totalDia))
maxV= max(count)                            # saco el maximo de la lista de count
posMax=count.index(maxV)                    # obtengo la posición de la lista
autoMax=automotores[posMax]                 # de la lista de automotores indexado en la posición del max
print('El vehículo que mas paso fue: {}'.format(autoMax))

