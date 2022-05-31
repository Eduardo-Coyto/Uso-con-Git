def calcular_nota(aciertos):
    nota = aciertos * 0.25
    return(nota)

num_de_aciertos = int(input('Ingrese en numero de aciertos del alumno: '))
resultado_final = calcular_nota(num_de_aciertos)
print('Obtuviste {} puntos45'.format(resultado_final))
