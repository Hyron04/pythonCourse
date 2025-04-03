import random

contador = 1
numeroRandom = random.randint(1, 100)
numero = int(input("Introduce un número entre 1 y 100: "))
while numero != numeroRandom:
    if numero < numeroRandom:
        print("El número es mayor")
    elif numero > numeroRandom:
        print("El número es menor")
    numero = int(input("Introduce un número entre 1 y 100: "))
    contador += 1
print("Has acertado el número y lo has encontrado en ", contador, " intentos")