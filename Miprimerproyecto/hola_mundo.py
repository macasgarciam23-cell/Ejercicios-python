"""
1. Crea un nuevo archivo y nómbralo hola_mundo.py
2. Escribe el código para que se imprima la cadena “Hola, mundo” (1)
3.Ejecuta el archivo
4. Reemplaza el texto que aparece en la variable nombre con tu nombre y usa la variable para imprimir la cadena “Hola, {{tu nombre}}” utilizando la concatenación con coma (2a)
5. Ejecuta el archivo
6. Reemplaza el texto que aparece en la variable nombre con tu nombre y usa la variable para imprimir la cadena “Hola, {{tu nombre}}” utilizando la concatenación con + (2b)
7. Ejecuta el archivo
8. Almacena tu número de la suerte en la variable numero y usa la variable para imprimir la cadena “Hola {{número}} !” utilizando la concatenación con coma (3a)
9. Almacena tu número de la suerte en la variable numero y usa la variable para imprimir la cadena “Hola {{número}}!” utilizando la concatenación con + (3b)
10. Ejecuta el archivo

11. BONUS NINJA: resuelve el error de arriba utilizando conversión
12. Guarda dos de tus comidas favoritas en las variables comida1 y comida2 y úsalas para imprimir la cadena “¡Me encanta comer {{comida1}} y {{comida2}}!” con el método format (4a)
13. Ejecuta el archivo
14. Guarda dos de tus comidas favoritas en las variables comida1 y comida2 y úsalas para imprimir la cadena “¡Me encanta comer {{comida1}} y {{comida2}}!” con cadena “f” (4b)
Ejecuta el archivo BONUS NINJA: Busca otros métodos de cadena y utilízalos en el archivo. ¡Existen muchísimas opciones para esto!"""

# 2.Escribe el código para que se imprima la cadena “Hola, mundo” (1)
print("Hola Mundo")

# 4. Reemplaza el texto que aparece en la variable nombre con tu nombre y usa la variable para imprimir la cadena “Hola, {{tu nombre}}”
#  utilizando la concatenación con coma (2a)
nombre = "Macarena"
print("Hola", nombre)

# 6. Reemplaza el texto que aparece en la variable nombre con tu nombre y usa la variable para imprimir la cadena “Hola, {{tu nombre}}”
# utilizando la concatenación con + (2b)
print("Hola " + (nombre))

# 8. Almacena tu número de la suerte en la variable numero y usa la variable para imprimir la cadena “Hola {{número}} !”
# utilizando la concatenación con coma (3a)
numero = 23
print("Hola", numero, "!")

# 9. Almacena tu número de la suerte en la variable numero y usa la variable para imprimir la cadena “Hola {{número}}!”
#  utilizando la concatenación con + (3b)
print(
    "Hola " + str(numero) + " !"
)  # 11. BONUS NINJA: resuelve el error utilizando conversión

# Guarda dos de tus comidas favoritas en las variables comida1 y comida2 y úsalas para imprimir la cadena
# “¡Me encanta comer {{comida1}} y {{comida2}}!” con el método format (4a)

comida1 = "Pasteles"
comida2 = "Milanesa"

print("¡Me encanta comer {} y {}!".format(comida2, comida1))


# 14. Guarda dos de tus comidas favoritas en las variables comida1 y comida2 y úsalas para imprimir la cadena
# “¡Me encanta comer {{comida1}} y {{comida2}}!” con cadena “f” (4b)
print(f"¡Me encanta comer {comida1} y {comida2}")


"""Busca otros métodos de cadena y utilízalos en el archivo. ¡Existen muchísimas opciones para esto!
upper () todo en mayusculas
lower () todo el texto en minusculas 
strip () quita los epacios
help () explica metodos
capitalize () primera letra en mayusculas
"""

print("¡Me encanta comer {} y {}!".format(comida2.upper(), comida1.upper()))
print(f"¡Me encanta comer {comida1.lower()} y {comida2.lower()}!")
print(f"¡Me encanta comer {comida1.strip()} y {comida2.strip()}!")
