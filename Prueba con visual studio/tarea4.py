def concatenar (cadena1, cadena2, veces):
    return (cadena1 + cadena2) * veces

c1 = str(input('1er Palabra: '))
c2 = str(input('2da Palabra: '))
v = int(input('cantidad de veces: '))

resultado = concatenar(c1,c2,v)
print(resultado)