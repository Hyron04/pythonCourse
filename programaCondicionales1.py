# Condicionales en Python
# Creación de una función que evalúe la nota de un alumno y devuelva su valoración
# La función recibe un parámetro que es la nota del alumno y devuelve una cadena de texto con la valoración correspondiente
def evaluarAlumno(nota):
    valoracion = ""
    if nota >=0 and nota < 5:
        valoracion = "Suspenso"
    elif nota < 7 and nota >= 5:
        valoracion = "Aprobado"
    elif nota < 9 and nota >= 7:
        valoracion = "Notable"
    elif nota < 10 and nota >= 9:
        valoracion = "Sobresaliente"
    elif nota == 10:
        valoracion = "Matrícula de Honor"
    else:
        valoracion = "Nota no válida"
    return valoracion

# Ejemplo de uso de la función evaluarAlumno 
notaAlumno = evaluarAlumno(float(input("Introduce la nota del alumno: ")))
print("La nota del alumno es: ", notaAlumno)

# Definición de una función que calcule el precio del alquiler de un coche según la edad del conductor y el número de días
# La función recibe dos parámetros: la edad del conductor y el número de días que se quiere alquilar el coche
def alquilerCocheEdad(edad, dias):
    precio = 0
    if edad < 18:
        precio = "No se puede alquilar el coche"
    elif edad >= 18 and edad < 25:
        precio = dias * 20 + 50
    elif edad >= 25 and edad < 30:
        precio = dias * 20 + 30
    elif edad >= 30 and edad < 70:
        precio = dias * 20 + 20
    else:
        precio = "No es posible alquilar el coche"
    return precio

alquilarCoche = alquilerCocheEdad(int(input("Introduce la edad del conductor: ")), int(input("Introduce el número de días que se quiere alquilar el coche: ")))
print(f"El precio del alquiler es: {alquilarCoche} euros")

# Definición de una función que calcule el precio del alquiler de un coche según la edad del conductor y el número de días
# La función recibe dos parámetros: la edad del conductor y el número de días que se quiere alquilar el coche
def calcularBeca (nota, ingresos, distanciaCentro, hermanosCentro, familiaNumerosa, discapacidad):
    beca = ""
    if (nota >= 8 and ingresos <= 20000) and (distanciaCentro <= 20 or hermanosCentro >= 1):
        beca = "Beca completa"
    elif (nota >= 7 and ingresos <= 30000) and (distanciaCentro <= 30 or hermanosCentro >= 2):
        beca = "Beca parcial"
    elif (nota >= 6 and ingresos <= 40000) and (distanciaCentro <= 40 or hermanosCentro >= 3):
        beca = "Beca mínima"
    elif familiaNumerosa or discapacidad:
        beca = "Beca especial"
    else:
        beca = "Beca no aprobada"
    return beca

nota = float(input("Introduce la nota del alumno: "))
ingresos = float(input("Introduce los ingresos anuales de la familia: "))
distanciaCentro = float(input("Introduce la distancia al centro educativo: "))
hermanosCentro = int(input("Introduce el número de hermanos en el centro educativo: "))
familiaNumerosa = (input("¿Es familia numerosa? (True/False): "))
discapacidad = (input("¿Tiene discapacidad? (True/False): "))

estadoBeca = calcularBeca(nota, ingresos, distanciaCentro, hermanosCentro, familiaNumerosa == "True", discapacidad == "True")
print("La beca es: ", estadoBeca)

#
def calcularRenta(ingresos):
    renta = 0
    if ingresos <12000:
        renta = 7
    elif ingresos >= 12000 and ingresos <18000:
        renta = 15
    elif ingresos >= 18000 and ingresos <35000:
        renta = 21
    elif ingresos >= 35000 and ingresos <70000:
        renta = 35
    else:
        renta = 45
    return renta

estadoRenta = calcularRenta(float(input("Introduce los ingresos anuales: ")))
print("La renta es: ", estadoRenta, "%") 

# Definición de una lista de trabajadores
trabajadores = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura"]

# Utilización de condicionales "in" para verificar si un trabajador está en la lista
if "Juan" in trabajadores:
    print("Juan está en la lista de trabajadores")
else:
    print("Juan no está en la lista de trabajadores")

if "Luis" not in trabajadores:
    print("Luis no está en la lista de trabajadores")
else:
    print("Luis está en la lista de trabajadores")

trabajadores.append("Luis") # Añadir a Luis a la lista de trabajadores
print("Luis ha sido añadido a la lista de trabajadores")

if "Luis" in trabajadores:
    print("Luis está en la lista de trabajadores")
else:
    print("Luis no está en la lista de trabajadores")

# Creación de un string con varios lenguajes de programación
lenguajesProgramación = "Python, Java, C++, JavaScript, PHP, Ruby"

# Utilización de condicionales "in" para verificar si un lenguaje de programación está en el string
if "PHP" in lenguajesProgramación:
    print("PHP está en la lista de lenguajes de programación")
else:
    print("PHP no está en la lista de lenguajes de programación")

# Utilización de condicionales "not in" para verificar si un lenguaje de programación no está en el string
if "SQL" not in lenguajesProgramación:
    print("SQL no está en la lista de lenguajes de programación")
else:
    print("SQL está en la lista de lenguajes de programación")

