"""
Crea un archivo de Python llamado bucle_for_basico1.py y realiza lo presentado a continuación:

1. Básico: imprime todos los números enteros del 0 al 100.
2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
3. Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
4. Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
5. Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
6. Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
Crea el archivo un Python llamado bucle_for_básico1.py
Codifica el ejercicio 1. Básico
Codifica el ejercicio 2. Múltiples de 2
Codifica el ejercicio 3. Contando Vanilla Ice
Codifica el ejercicio 4. Wow. Número gigante a la vista
Codifica el ejercicio 5. Regrésame al 3
Codifica el ejercicio 6. Contador dinámico
"""

# 1. Básico: imprime todos los números enteros del 0 al 100.

for numero in range(0, 101):
    print(numero)

# 2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for multiplos in range(2, 500, 2):
    print(multiplos)


# 3.Imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”

for num in range(1, 101):
    if num % 10 == 0:
        print("Baby")
    elif num % 5 == 0:
        print("ice ice")
    else:
        print(num)  # Imprime 1-2-3-4-iceice-6-7-8-9- baby ....


# 4. Suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
pares = []

for num in range(0, 5001):
    if num % 2 == 0:
        pares.append(num)
        suma_pares = sum(pares)
        print(
            f"La suma total de los pares es: {suma_pares}"
        )  # tambien podria ser print("La suma total de los pares es:" , sum(pares))

## 5. Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.

for tres in range(2024, -1, -3):
    print(tres)


# 6. Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y
# pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo.
# Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de
# imprimir 4, 6, 8, 10 (en líneas sucesivas).

for pares in range(3, 11):
    if pares % 2 == 0:
        print(pares)
