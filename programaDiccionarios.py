#Creación de un diccionario con los países y sus capitales
lasCapitales={"España":"Madrid","Italia":"Roma","Austria":"Viena","Japón":"Tokio","Bélgica":"Bruselas","Reino Unido":"Londres","Francia":"París","Alemania":"Berlín","Portugal":"Lisboa","Holanda":"Ámsterdam", "Australia":"Sydney","Canadá":"Ottawa","Estados Unidos":"Washington","China":"Pekín","Corea del Sur":"Seúl"}

# Añadir un nuevo país y su capital
lasCapitales["Colombia"]="Bogotá"

# Modificar la capital de Australia
lasCapitales["Australia"]="Camberra"

print(lasCapitales)

# Eliminar un país y su capital
del lasCapitales["China"]
print(lasCapitales)

#Crear un nuevo diccionario con información de los mejores jugadores de baloncesto
mejorJugadores={"Estados Unidos":"Washington", 23:"Michael Jordan", "Deporte":"Baloncesto"}
print(mejorJugadores)

# Crear una lista con las claves de los países
claveCapitales=["España", "Italia", "Austria", "Japón", "Bélgica", "Reino Unido", "Francia", "Alemania", "Portugal", "Holanda", "Australia", "Canadá", "Estados Unidos", "China", "Corea del Sur"]

# Crear un diccionario con los países y sus capitales
capitalesMundo={claveCapitales[0]:"Madrid", claveCapitales[1]:"Roma", claveCapitales[2]:"Viena", claveCapitales[3]:"Tokio", claveCapitales[4]:"Bruselas", claveCapitales[5]:"Londres", claveCapitales[6]:"París", claveCapitales[7]:"Berlín", claveCapitales[8]:"Lisboa", claveCapitales[9]:"Ámsterdam", claveCapitales[10]:"Sydney", claveCapitales[11]:"Ottawa", claveCapitales[12]:"Washington", claveCapitales[13]:"Pekín", claveCapitales[14]:"Seúl"}
print(capitalesMundo)

# Mostrar la capital de España
print(capitalesMundo["España"])

# Mostrar las claves del diccionario
print(capitalesMundo.keys())

# Mostrar los valores del diccionario
print(capitalesMundo.values())

# Mostrar el número de elementos del diccionario
print(len(capitalesMundo))

# Mostrar si un país está en el diccionario
print("España" in capitalesMundo)

# Mostrar si una capital está en el diccionario
print("Madrid" in capitalesMundo.values())

# Crear un diccionario con los datos de Michael Jordan y dentro de él un array con los años en los que ganó el campeonato
datosJordan={23:"Jordan", "Nombre":"Michael",  "Equipo":"C. Bulls", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

# Mostrar las claves del diccionario
print(datosJordan.keys())

# Mostrar los datos de Michael Jordan
print(datosJordan)

# Mostrar los años en los que ganó el campeonato
print(datosJordan["Anillos"]["Temporadas"])