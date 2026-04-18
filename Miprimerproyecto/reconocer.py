numero1 = 70  # Declaracion de variable. Tipo de dato numerico entero
numero2 = 3.14  # Declaracion de variable. Tipo de dato numerico decimal- float
booleano = False  # Declaracion de variable. Tipo de dato booleano
cadena = "Hola Mundo"  # Declaración de variable. Tipo de datos string

# Declaracion de variable tipo lista []
ingredientes_pastel = [
    "Harina",
    "Leche",
    "Huevos",
    "Vainilla",
    "Chocolate",
]

# Declaracion de variable tipo diccionario{}
persona = {
    "nombre": "Patricio",
    "pais": "México",
    "edad": 35,
    "soltero": False,
}

# Declaracion de variable tipo tupla
frutas = (
    "guayaba",
    "fresa",
    "papaya",
)


print(
    type(frutas)
)  # print es una funcion y type dice que tipo de dato es = class tuple

print(ingredientes_pastel[2])  # funcion que muestra lo que esta en el indice 2 = huevos
ingredientes_pastel.append(
    "Mantequilla"
)  # append metodo de una lista. incorpora mantequilla al final de una lista

print(persona["nombre"])  # Imprime el valor de la clave nombre

persona["nombre"] = "Kevin"  # modifica el valor de la clave nombre:

persona["color_ojos"] = "cafe"  # agrega una nueva clave valor al diccionario de persona

print(frutas[2])  # Muestra papaya


# Condicional if Ejecuta si es verdadero
if numero1 > 45:
    print("Numero mayor")
else:
    print("Numero menor")


# Condicional if
if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")


# Bucle for (Es finito)

for x in range(8):
    print(x)
for x in range(2, 8):
    print(x)
for x in range(2, 8, 2):
    print(x)
x = 0


# Bucle While infinito
while x < 8:
    print(x)
    x += 1


# Metodo pop
ingredientes_pastel.pop()  # pop metodo que elimina el último elemento de la lista
ingredientes_pastel.pop(1)  # pop metodo que elimina el elemnto en la posición 1 "Leche"


"""
#metodo pop
print(persona) Muestra todos los elementos de un diccionario
persona.pop("color_ojos") Elimina la clave color_ojos y por ende su valor
print(persona) imprime el diccionario
"""

# Bucle con uso de continuar la iteracion y termino del bucle
for ingrediente in ingredientes_pastel:
    if ingrediente == "Harina":
        continue  # salta la impresion
    print("Después de la primera sentencia")
    if ingrediente == "Chocolate":
        break  # detener


# Funcion llamada imprime_hol_10_veces
def imprime_hola_10_veces():
    for numero in range(10):
        print("Hola")  # se imprimira 10 veces porque el range lo determinaste en 10


imprime_hola_10_veces()  # Aqui llamas a la funcion para que se ejecute 10 veces hola


# Función con parametros que determina las veces que hara la repeticion el range(n)
def imprime_hola_n_veces(n):
    for numero in range(n):
        print("Hola")


imprime_hola_n_veces(5)  # Llamas a la funcion para que repita 5 veces hola


def imprime_hola_n_o_diez_veces(n=10):
    for numero in range(n):
        print("Hola")


imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3) Debe existir la variable antes de ejecutar el print porque dara error
# numero3 = 86 Recuerda que el nombre de las variables no llevan espacio
# frutas[0] = 'naranja' # Genera un error por ser una tupla
# print(persona['hobbies']) No existe la clave Hobbies genrara un error keyError
# print(ingredientes_pastel[11]) No tiene ese index generará un error IndexError
#   print(booleano) # Imprime False porque asi esta definido
# frutas.append('manzana') es una tupla no se puede modificar
# frutas.pop(1) AttributeError: 'tuple' object has no attribute 'pop'
