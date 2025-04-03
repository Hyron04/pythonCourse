import math

print("Este programa encuentra la raíz cuadrada de un número positivo")

numero = int(input("Introduce un número positivo: "))
intentos=1

while numero < 0:
    print("Error: El número debe ser positivo.")
    numero = int(input("Introduce un número positivo: "))
    intentos += 1
    if intentos == 5:
        break

if intentos == 5:
    print("Has superado el número máximo de intentos")
else:
    print(math.isqrt(numero))

# Este programa muestra el uso de un bucle while
## Se inicializa una variable contador en 0
contador = 0

# El bucle while se ejecuta mientras la condición sea verdadera
while contador < 10:
    print("El contador es: ", contador)
    contador += 1
print("Fin del bucle while")

# Se inicializa una variable edad con un valor entero
# En este caso, se pide al usuario que introduzca su edad
edad = int(input("Introduce tu edad: "))

# El bucle while se ejecuta mientras la condición sea verdadera
# En este caso, se ejecuta mientras la edad sea menor que 18
while edad < 18 or edad > 120:
    if edad > 120:
        print("Edad no válida, introduce una edad entre 18 y 120")
        edad = int(input("Introduce tu edad: "))
    elif edad < 18:
        print("Eres menor de edad, no tienes acceso al programa")
        edad = int(input("Introduce tu edad: "))

print("Eres mayor de edad, tienes acceso al programa")
print("Fin del programa")