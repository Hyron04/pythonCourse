a="15"
b="10"

# Convertimos a y b a enteros y los sumamos
print("La suma de", a,"y", b,"es:",int(a)+int(b))

c="15.5"
d="10.5"

# Convertimos c y d a flotantes y los multiplicamos
print("La multiplicación de", c,"y", d,"es:",float(c)*float(d))

edad=34

# Convertimos la edad a cadena y la imprimimos
print("Mi edad es: "+str(edad)+" años")

empleados=["Juan", "María", "Carlos", "Ana"]

#Utilizamos la función join para concatenar los elementos de la lista empleados
#y los separamos por un espacio en blanco
print(" ".join(empleados))

#Creamos una variable con una cadena de texto
estudiantes="Jordi Mario Laura Ana"

#Utilizamos la función split para separar la cadena en palabras
#y las guardamos en una lista, donde eliminamos la coma como separador
print(estudiantes.split())