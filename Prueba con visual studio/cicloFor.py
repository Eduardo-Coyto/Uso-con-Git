tantos = [1,2,3,4,5,6,7,8,9,10,11,12]
palos = ['Oro', 'Copa', 'Basto', 'Espada']
cartas= []

for i in range(0,40,4):
    for j in range(4):
        print ('{}'.format(cartas[i+j]), end='')
