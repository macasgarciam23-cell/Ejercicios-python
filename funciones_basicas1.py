# 1
def cantidad_de_vocales():
    return 5


print(cantidad_de_vocales())  # Imprime lo que dice el return

"""
#2
def cantidad_de_glaciares_argentina():
    return 16968
print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())

no esta definida la funcion cantidad_de_dias_o_meses_ generando un error
"""


# 3
def anio_independencia_chile():
    return 1810
    return 1851


print(anio_independencia_chile())
# Imprime un solo return y siempre el primer return 1810


# 4
def cantidad_de_departamentos_colombia():
    return 32
    print(33)


print(cantidad_de_departamentos_colombia())
# Imprime el return 32. Llegando a return sale de la funcion no imprimiendo el 33


# 5
def altura_machu_picchu():
    print(2438)


x = altura_machu_picchu()
print(x)
# imprime 2438 y none porque al no tener return no devuelve un valor y lo indica con None


# 6
def suma(a, b):
    print(a + b)


print(suma(10, 5) + suma(4, 3))
# imprime 15 y 7 y error porque al no tener return genera un none para la funcion (10,5)
# y y genera otro none con el par (4,3) y dos none no puede haber generando error type


# 7
def concatenar(a, b):
    return str(b) + str(a)


print(concatenar(7, 15))
# el return indica el orden entonces imprime 157


# 8
def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21


print(paises_latinoamerica_o_lenguas_indigenas())
# Imprime por print 560 y por return 46 y se termian la funcion


# 9
def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52


print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))  # imprime 365
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4))  # Imprime 12
print(
    cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4)
    + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3)
)  # imprime 377 se suma por ser numeros y no texto


# 10
def sumatoria(a, b):
    return a + b
    return 157


print(sumatoria(3, 4))
# imprime 7


# 11
a = 150
print(a)  # Imprime 150


def funcion():
    a = 350
    print(a)


print(a)  # Imprime 150
funcion()  # Imprime 350 y None
print(a)  # Imprime 150
# 150   150  350   150


# 12
a = 150
print(a)  # 150


def funcion():
    a = 350
    print(a)
    return a


print(a)  # imprime 150
funcion()  # imprime 350
print(a)  # Imprime 150


# 13
a = 150
print(a)  # Imprime 150


def funcion():
    a = 350
    print(a)
    return a


print(a)  # 150
a = funcion()  # Imprime 350
print(a)  # 350


# 14
def funcion1():
    print(3)  # imprime 3
    funcion2()
    print(2)  # imprime 2


def funcion2():
    print(1)  # imprime 1


funcion1()  # imprime 3-1-2


# 15
def funcion1():
    print(3)  # imprime 3
    a = funcion2()  # imprime 1
    print(a)  # imprime 0
    return 4


def funcion2():
    print(1)
    return 0


b = funcion1()  # imprime 3-1-0
print(b)  # Imprime 4
