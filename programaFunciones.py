# Descripción: Programa que muestra el uso de funciones en Python

#Creamos una función que imprime un mensaje
def imprimeMensaje():
    print("Esto es el curso de Python")
    print("Estamos aprendiendo a programar")
    print("Ahora estamos realizando una función")

#Llamamos a la función
imprimeMensaje()

#Creamos una función que devuelve un valor y recibe dos parámetros
def suma(a, b):
    return a + b

#Llamamos a la función y guardamos el resultado en una variable
print(suma(5, 3))

#Creamos una función que devuelve un valor
def imprimeTexto():
    return "Esto es un texto"

#Creamos una variable que guarda el resultado de la función 
valorMensaje = imprimeTexto()

#Imprimimos el valor de la variable
print(valorMensaje)
      
#Creamos una función que recibe varios parámetros y devuelve un valor
def imprimeMensajePersonalizado(mensaje, valor1, valor2):
    return mensaje + str((valor1+valor2)) + " Esto es un mensaje personalizado"

#Llamamos a la función e imprimimos el resultado
print(imprimeMensajePersonalizado("La suma es: ", 5, 9))

