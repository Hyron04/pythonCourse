#Ejemplo de tuplas
misDatos=("Jordi", 4, 4, 1990)
print(misDatos)

#Convertir una tupla en una lista
misDatosLista=list(misDatos) #Aplicamos el método list para convertir la tupla en una lista
print(misDatosLista)

#Convertir una lista en una tupla
misDatosTupla=tuple(misDatosLista) #Aplicamos el método tuple para convertir la lista en una tupla
print(misDatosTupla)

print (1990 in misDatosTupla) #Comprobamos si el valor 1990 está en la tupla donde el resultado será True
print (1991 in misDatosTupla) #Comprobamos si el valor 1991 está en la tupla donde el resultado será False

#Método count para contar cuantas veces aparece un valor en una tupla
print(misDatosTupla.count(4))

#Método len para contar cuantos elementos tiene una tupla
print(len(misDatosTupla))

#Desempaquetar una tupla en variables
name, day, month, year = misDatosTupla #Creamos las variables name, day, month y year y les asignamos los valores de la tupla
print(name)
print(day)
print(month)
print(year)