from xml.etree.ElementTree import C14NWriterTarget


def saludo (usuario):
    bienvenido = ('Bienvenido {}'.format(usuario))
    return (bienvenido)

c1 = str(input('Introduce tu nombre: '))
resultado = saludo(c1)
print(resultado)