x = 10
y = 1.23
print(type(x))
print(type(y))
print(type(3.14))
print(type("45"))
print(type(2 + 5j))
print("Hola Mundo")


# 1. Imprime "Hola, mundo"

print("Hola, Mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Valeria"
print("Hola,", nombre)  # con una coma
print(f"Hola, {nombre}")  # con un +

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 156
print("Hola,", numero, "!")  # con una coma
print(
    "Hola, " + str(numero) + " !"
)  # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "tacos"
comida2 = "arepas"
print("¡Me encanta comer {} y {}!".format(comida1, comida2))  # con .format()
print(f"¡Me encanta comer {comida1} y {comida2}!")  # con una cadena f
